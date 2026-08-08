# Reference Image Collection & Tagging Format (v2.0)

### Step 0 — File naming
```
R{NNN}_{category}_{brand-or-unknown}_{layout}.jpg
مثال: R014_skincare_skin1004_hero-center-nature.jpg
```
`R{NNN}` کلید یکتاست و هرگز تغییر نمی‌کنه.

### Step 1 — Save behavior

**REFERENCE** (brand style bootstrapping) → auto-save + tag در همون پیام.
**PRODUCT** (محصول خود کاربر) → **save نکن**، اول prompt بنویس، فقط با درخواست صریح ذخیره کن.

> اگر نوع تصویر مبهم بود: یک سؤال کوتاه بپرس، auto-save نکن.

### Step 2 — Dual output (اجباری)

هر تصویر **دو خروجی** می‌گیره:

**A) One-liner برای اسکن سریع (فارسی مجاز، تگ‌ها انگلیسی):**
```
- `R014` — SKIN1004 Centella Ampoule | amber glass dropper, warm peach seamless gradient, upright center, real centella leaves, soft diffused key + subtle rim, glossy reflective surface, centered 4:5, "natural / clinical-botanical" 🌿
```

**B) YAML block (منبع حقیقت برای ایجنت):**

```yaml
id: R014
file: R014_skincare_skin1004_hero-center-nature.jpg

# --- 1. PRODUCT IDENTITY ---
brand: SKIN1004            # or: unknown
product_name: Madagascar Centella Ampoule
category: skincare         # skincare|haircare|makeup|fragrance|supplement|beverage|food|homecare|tech
subcategory: serum
container_type: dropper_bottle   # dropper_bottle|pump|airless|jar|tube|spray|stick|sachet|can|carton|ampoule
container_material: amber_glass  # clear_glass|frosted_glass|amber_glass|matte_plastic|glossy_plastic|aluminum|paper
label_style: minimal_white_typographic

# --- 2. COLOR ---
palette_product: ["#C68A4B amber", "#FFFFFF white"]
palette_scene:   ["#F3D9C6 peach", "#7FA05C leaf green"]
color_temperature: warm      # warm|neutral|cool|mixed
contrast: medium             # low|medium|high
saturation: medium           # muted|medium|vivid
accent_color: leaf_green

# --- 3. PLACEMENT & CAMERA ---
placement: upright_centered  # upright_centered|upright_offset|tilted|lying_flat|floating|submerged|held_in_hand|stacked|embedded|leaning
camera_angle: eye_level      # eye_level|low_angle|high_angle|top_down_flatlay|three_quarter|macro
product_scale: medium        # extreme_closeup|closeup|medium|wide_environment
depth_of_field: shallow      # deep|medium|shallow|tilt_shift
product_count: 1

# --- 4. PROPS & VFX ---
props: [centella_leaves, water_droplets]
prop_placement: "leaves lower-left, leaning against bottle base"
vfx: [dew_droplets]          # splash|mist|smoke|powder_burst|ice|dew_droplets|floating_particles|glow|light_leak|none
human_presence: none         # none|hand|half_face|full_model

# --- 5. LIGHTING ---
lighting_quality: soft_diffused   # soft_diffused|hard_direct|mixed
key_direction: front_left_45      # front|front_left_45|side|back|top|top_down_spot
rim_light: subtle_warm            # none|subtle|strong|colored
fill: high                        # none|low|high
shadow_type: soft_short           # none|soft_short|soft_long|hard_sharp|dramatic_cast|gobo_leaf_pattern
light_temperature_k: 4500

# --- 6. BACKGROUND & SURFACE ---
background_type: seamless_gradient  # solid|seamless_gradient|studio_sweep|textured_wall|natural_env|water|sky|abstract_3d|fabric
background_color: peach_beige
gradient_direction: top_light_to_bottom_dark
surface: glossy_reflective          # none|matte_paper|glossy_reflective|stone_slab|marble|wood|sand|water|fabric_folds|acrylic_riser
reflection: soft_mirror

# --- 7. COMPOSITION & LAYOUT ---
layout_archetype: hero_center_pedestal  # hero_center_pedestal|rule_of_thirds_offset|flatlay_grid|diagonal_dynamic|split_screen|floating_cluster|macro_texture|lifestyle_in_use|before_after
crop: medium_tight
negative_space: top          # top|bottom|left|right|around|minimal
symmetry: symmetrical
aspect_ratio: "4:5"

# --- 8. TYPOGRAPHY & COPY (poster-specific) ---
has_text: false
text_zones: []               # e.g. [headline_top, price_badge_topright, cta_bottom]
script_direction: n/a        # ltr|rtl|n/a

# --- 9. STYLE & MOOD ---
render_style: photoreal_studio   # photoreal_studio|cgi_3d_render|hyperreal_macro|editorial_lifestyle|film_analog|collage|illustration
post_processing: clean_glossy     # clean|film_grain|high_contrast|pastel_soft|glossy_specular|hazy_bloom
mood: "clean, botanical, clinical-calm"
season_occasion: none             # none|summer|winter|ramadan|nowruz|valentine|black_friday

# --- 10. REUSE / RETRIEVAL ---
concept_idea: "Product as a botanical specimen — ingredient placed physically beside bottle to prove origin."
fits_product_types: [serum, ampoule, toner, essence, oil]
fits_container: [dropper_bottle, glass_bottle, ampoule]
swap_difficulty: easy        # easy|medium|hard
strength: "ingredient storytelling + premium simplicity"
avoid_if: "product is opaque plastic or has busy multi-color packaging"

# --- 11. PROMPT SEED (with placeholders) ---
prompt_seed: >
  Studio product photograph of {PRODUCT} standing upright, centered, eye-level,
  on a glossy reflective surface with a soft mirror reflection.
  Seamless warm {BG_COLOR} gradient background, light falling from top.
  Fresh {INGREDIENT} leaves with dew droplets leaning at the lower-left base.
  Soft diffused key light from front-left 45°, subtle warm rim on the bottle edge,
  high fill, short soft shadow. Warm 4500K, medium contrast, shallow depth of field.
  Clean glossy commercial retouching, photoreal, 4:5.
negative_prompt: "harsh shadows, cluttered props, visible studio equipment, text, watermark, distorted label"

emoji: 🌿
notes_fa: "ترکیب برگ واقعی + بطری کهربایی، حس ارگانیک اما تمیز."
```

---

## قانون Retrieval

وقتی کاربر عکس محصول خودش رو می‌فرسته، ایجنت باید:

```
1. Extract product features → category, container_type, container_material,
   dominant colors, opacity, label busyness
2. Match against index with weights:
   container_type      0.30
   category            0.20
   fits_product_types  0.20
   color harmony       0.15
   swap_difficulty     0.10
   mood match (user)   0.05
3. Return top 3 references, each with: id, thumbnail, why-it-fits (1 line)
4. Take chosen prompt_seed → fill {PRODUCT}/{BG_COLOR}/{INGREDIENT}
   → adapt colors to product's actual palette → output final prompt
```

---

## معیار پذیرش

یک تگ **رد می‌شه** اگر:
- هر فیلد `required` خالی یا `TBD` باشه
- `props` پر باشه ولی `prop_placement` نه
- `concept_idea` کمتر از ۸ کلمه باشه
- `prompt_seed` placeholder نداشته باشه (یعنی generic نیست)
- برند حدس زده شده باشه بدون شواهد → باید `unknown` بشه

**required (۱۸ فیلد):** `category, container_type, palette_product, palette_scene, color_temperature, placement, camera_angle, product_scale, props, lighting_quality, key_direction, shadow_type, background_type, surface, layout_archetype, negative_space, mood, concept_idea, prompt_seed`

---

## نگهداری ایندکس

```
/addstudio-v01/
  ├── INDEX.md            ← جدول one-liner همه رفرنس‌ها (اسکن سریع انسانی)
  ├── references.yaml     ← همه YAML blockها (منبع ایجنت)
  └── /images
```
بعد از هر save، **هر دو** فایل آپدیت می‌شن. اگر آپدیت نشد، ذخیره ناقصه.

---

## نمونهٔ Bad / Good

**❌ Bad**
```
- `R014` — SKIN1004 Centella Ampoule 🌿
```
**❌ Bad هم هست** (توصیفی ولی بدون ساختار و بدون prompt_seed):
```
- `R014` — بطری کهربایی با برگ سبز، نور نرم، پس‌زمینه بژ 🌿
```
**✅ Good** = one-liner انگلیسی + YAML کامل + prompt_seed با placeholder.
