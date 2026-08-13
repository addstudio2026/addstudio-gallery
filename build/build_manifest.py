#!/usr/bin/env python3
"""
build_manifest.py — ساخت manifest.json نهایی از فایل‌های references/*.yaml
با استفاده از تاکسونومی moods.yaml (طبق مستندسازی mood-guide.md).

اجرا:  python3 build_manifest.py
ورودی: ../all_tags_backup/*.yaml  (یا مسیر --src)
خروجی: ../manifest.json + ../mood_report.json (گزارش نیازمند بازبینی)
"""
import os, re, json, argparse, sys
import yaml
from collections import defaultdict

PRIORITY = ['luxury-premium','moody-dramatic','clinical-fresh','natural-botanical',
            'dreamy-ethereal','energetic-bold','playful-fun','warm-intimate','unknown']

EXTRA_KEYWORDS = {
    'clinical-fresh': ['minimalist', 'minimal', 'sterile', 'pureness'],
    'energetic-bold': ['vibrant', 'commercial'],
    'warm-intimate': ['feminine'],
}

def load_taxonomy(path):
    moods_def = yaml.safe_load(open(path, encoding='utf-8'))['moods']
    kw_map = {m['slug']: [k.lower() for k in m.get('keywords', [])] for m in moods_def}
    for slug, extra in EXTRA_KEYWORDS.items():
        kw_map.setdefault(slug, []).extend(extra)
    label_map = {m['slug']: m for m in moods_def}
    return kw_map, label_map

def robust_load(text):
    """Try normal YAML parse; on failure, quote plain-scalar lines that contain
    a stray ':' (the most common cause of parse errors in this dataset), then retry."""
    try:
        return yaml.safe_load(text), None
    except yaml.YAMLError as e:
        fixed = []
        for line in text.splitlines():
            m = re.match(r'^(\s*)([A-Za-z0-9_]+):\s(.*)$', line)
            if m and ':' in m.group(3) and not m.group(3).strip()[:1] in ('"', "'", '[', '{', '>', '|'):
                indent, key, val = m.groups()
                fixed.append(f'{indent}{key}: "{val.replace(chr(34), chr(92)+chr(34))}"')
            else:
                fixed.append(line)
        try:
            return yaml.safe_load('\n'.join(fixed)), None
        except yaml.YAMLError as e2:
            return None, str(e2).splitlines()[0]

def find_field(data, key, depth=4):
    """Recursively search a (possibly nested) parsed yaml dict for `key`."""
    if not isinstance(data, dict) or depth < 0:
        return None
    if key in data and data[key]:
        return data[key]
    for v in data.values():
        if isinstance(v, dict):
            found = find_field(v, key, depth - 1)
            if found:
                return found
    return None

def stringify(val):
    if val is None:
        return ''
    if isinstance(val, list):
        return ' '.join(str(x) for x in val)
    return str(val)

def tokenize(text):
    return [t for t in re.split(r'[,\-\s]+', text.lower()) if len(t) > 2]

def kw_match(tok, kw):
    if tok == kw:
        return True
    return len(tok) >= 4 and len(kw) >= 4 and (tok in kw or kw in tok)

def score_mood(text, kw_map):
    tokens = tokenize(text)
    scores, evidence = defaultdict(int), defaultdict(list)
    for tok in tokens:
        for slug, kws in kw_map.items():
            if any(kw_match(tok, kw) for kw in kws):
                scores[slug] += 1
                evidence[slug].append(tok)
    if not scores:
        return 'unknown', 0.0, [], len(tokens)
    best = sorted(scores.items(), key=lambda kv: (-kv[1], PRIORITY.index(kv[0])))[0][0]
    conf = round(min(1.0, scores[best] / max(1, len(tokens)) * 2), 2)
    return best, conf, evidence.get(best, []), len(tokens)

def placeholder_url(ref_id):
    # NOTE: replace with your real hosted HTTPS image URL before deploying —
    # see README.md "1. Replace the sample data".
    return f"https://picsum.photos/seed/{ref_id}/600/{750 if int(re.sub('[^0-9]','',ref_id) or 0) % 2 else 600}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', default='../all_tags_backup')
    ap.add_argument('--taxonomy', default='../moods.yaml')
    ap.add_argument('--out', default='../manifest.json')
    ap.add_argument('--report', default='../mood_report.json')
    args = ap.parse_args()

    kw_map, label_map = load_taxonomy(args.taxonomy)

    files = sorted(
        [f for f in os.listdir(args.src) if f.endswith('.yaml')],
        key=lambda x: int(re.search(r'\d+', x).group())
    )

    manifest, report = [], []
    counts = defaultdict(int)

    for fname in files:
        raw = open(os.path.join(args.src, fname), encoding='utf-8').read()
        data, err = robust_load(raw)
        data = data or {}

        ref_id = find_field(data, 'id') or fname.replace('.yaml', '')
        brand = find_field(data, 'brand') or 'Unknown'
        category = find_field(data, 'category') or 'skincare'
        product_name = find_field(data, 'product_name')
        style_field = find_field(data, 'style')
        mood_field = find_field(data, 'mood')
        concept = find_field(data, 'concept_idea')
        reuse = find_field(data, 'reuse')
        file_name = find_field(data, 'file') or ''

        # priority order for the text we score against
        if mood_field:
            src_text, src_name = stringify(mood_field), 'mood'
        elif style_field:
            src_text, src_name = stringify(style_field), 'style'
        elif concept or reuse:
            src_text, src_name = f"{stringify(concept)} {stringify(reuse)}", 'concept/reuse'
        else:
            src_text, src_name = file_name.replace('.jpg', '').replace('.png', ''), 'filename'

        if err:
            mood, conf, evidence, n_tokens = 'unknown', 0.0, [], 0
            src_name = 'parse_error'
        else:
            mood, conf, evidence, n_tokens = score_mood(src_text, kw_map)

        needs_review = conf < 0.4 or bool(err)
        counts[mood] += 1

        headline = product_name or (style_field if isinstance(style_field, str) else None) or ref_id

        manifest.append({
            'id': ref_id,
            'url': placeholder_url(ref_id),   # TODO: replace with real hosted image URL
            'brand': brand,
            'category': category,
            'mood': mood,
            'style': headline,
        })

        report.append({
            'id': ref_id, 'mood': mood, 'confidence': conf, 'source_field': src_name,
            'evidence': evidence, 'needs_review': needs_review, 'parse_error': err,
        })

    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    with open(args.report, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"{len(manifest)} آیتم نوشته شد → {args.out}")
    print("\nتوزیع mood:")
    for slug in PRIORITY:
        if counts.get(slug):
            print(f"  {slug}: {counts[slug]}")
    flagged = [r for r in report if r['needs_review']]
    print(f"\nneeds_review: {len(flagged)} مورد → جزئیات در {args.report}")
    for r in flagged:
        tag = f" [PARSE ERROR: {r['parse_error']}]" if r['parse_error'] else ""
        print(f"  - {r['id']} (source={r['source_field']}){tag}")

if __name__ == '__main__':
    main()
