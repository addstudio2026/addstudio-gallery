# Reference Image Collection & Tagging Format

## Step 1: Save behavior (depends on image type)

### REFERENCE images (from other brands, for style bootstrapping):
1. Save to the project folder with sequential naming: `01-brand-product.jpg`, `02-brand-product.jpg`, etc.
2. Reply in ONE message: "ذخیره شد ✅" + the rich tag below.
3. Do NOT wait for explicit instruction. The user sends many and expects auto-save.

### PRODUCT images (user's own products, for prompt writing):
1. Do NOT save until user explicitly says "ذخیره کن" or similar.
2. Write the prompt first. Only save if user requests it.
3. The image was sent for prompt writing, not for archiving.

## Step 2: Rich tagging (all 9 axes mandatory)

Each image MUST be tagged with a description covering ALL of these axes. Brief tags ("#01 — Brand Name Product") are NOT acceptable.

### Required Axes

1. **Product identity**: brand, product name, type (serum/cream/spray/etc.)
2. **Color palette**: dominant colors of product AND scene, with temperature (warm/cool)
3. **Product placement & positioning**: upright/lying/tilted/floating, angle, relation to other objects
4. **Props & accessories**: hands, tools, natural elements, sports equipment — what and where
5. **Lighting style & direction**: key direction, quality (hard/soft/diffused), temperature, rim/key/fill presence
6. **Background & surface**: color, gradient direction, texture, reflectivity
7. **Composition & framing**: crop tightness, centering, negative space, aspect ratio
8. **Mood & aesthetic**: one-line mood descriptor (e.g., "minimalist and earthy", "cinematic and dramatic")
9. **Emoji tag**: single emoji for quick visual scanning

### Format

```
- `#NN` — Brand Product Name | color palette, product placement, props, lighting, background, composition, mood 🔖
```

### Example (good)

```
- `#05` — SKIN1004 Centella Ampoule | بطری شیشه‌ای کهربایی طلایی، قطره‌چکان سفید، برچسب سفید ساده، ساقه و برگ سنتلا سبز کنار بطری، بازتاب شفاف روی سطح، پس‌زمینه بژ مایل به هلویی، نور دیفیوز گرم، سنترا کامپوزیشن 🌿
```

### Example (bad — rejected by user)

```
- `#05` — SKIN1004 Centella Ampoule 🌿
```

## Pitfall

User said: "خیلی کمه بیشتر باید توصیفشون‌کنی رنگ و نحوه قرار کیری محصول و ایده پستر‌مهمه"
Translation: Color, product placement, and poster idea are important — describe more.
