# Session Learnings — 2026-08-08

## Key Corrections

### Visual Analysis First (CRITICAL)
- User explicitly corrected: "باید اول رفرنس عکس رو بدیه و بعد مطابق با اون رفرنس پرامپت بنویسی"
- **LESSON:** Never write a prompt based ONLY on Section A text. Always visually analyze hero reference images first using delegate_task with vision subagent. Text gives data; vision gives the soul.

### Load Skills FIRST (CRITICAL)
- User explicitly said: "اسکیل واست نوشتم که احمق"
- **LESSON:** ALWAYS load product-shot-prompts and poster-addstudio-v01 skills BEFORE doing any work.

### Product Description in Prompt (NEVER)
- User corrected: "فقط به صورت کلی بگو محصول خودش باشه بدن تغییر"
- **LESSON:** Image model sees the product. Don't describe colors, text, materials. Just "the product". Focus on composition, lighting, mood, STATE/POSITION.

### Visual Analysis Must Be FORENSIC
- User corrected R020: "پشتش ژل هست!" — I had written `props: [none]` when gel blobs were visible.
- **LESSON:** When tagging references, describe EVERY visible element. If you can see it, tag it.

## Reference Tagging v2.0
- File naming: `R{NNN}_{category}_{brand}_{layout}.jpg`
- Dual output: one-liner + YAML block (11 sections, 18 required fields)
- Disk write MANDATORY: references.yaml + INDEX.md + image file
- Every save = 3 locations minimum

## Cross-Reference Patterns
- Warm color temperature (except SYNSKIN: cool clinical)
- Smooth gradient backgrounds, slightly low angle, soft diffused light
- Sporty shots: hard direct light, high contrast
- Shallow DOF for cinematic feel
