# Session Learnings — 2026-08-07

## Products Tested

| # | Product | Type | Color | Concept That Worked |
|---|---------|------|-------|-------------------|
| 20 | Lá farterr Anti Spot Tinted SPF 40+ | Adult sunscreen | Burgundy | Wave form (LOWE reference) |
| 21 | Lá farterr Anti Spot SPF 30 | Adult sunscreen (oily skin) | Yellow-orange | Morning dew/droplets |
| 22 | Lá farterr Anti Spot SPF 30 | Adult sunscreen (applied on skin) | Yellow-orange | Low angle, hands applying |
| 23 | Lá farterr Kids SPF 30+ | Kids sunscreen | White + blue cap | Cloud + sun glow protection |
| 24 | Lá farterr Mineral SPF 40+ | Adult sunscreen | White + peach cap | Wave form (LOWE reference) |
| 25 | Lá farterr Tinted Bronze SPF 40+ | Adult sunscreen (tinted) | Burgundy | Monochrome blocks (Clarins reference) |
| 26 | SYNDA^GE Age-Defense SPF 50 | Sunscreen | Dark forest green | Floating + light wisps like smoke |
| AURUM | Golden Glow Face Oil (fictional) | Face oil | Amber glass + gold | Ribbon of light + golden particles (La Roche-Posay ref) |

## User Corrections (Chronological)

1. **"اصلا خوب نیست و شبیه به عکس ها نشده"** — First prompt was too technical, didn't match reference images. Led to "Creative Director Mode" rewrite.

2. **"لازم نیست محصول رو توی پرامپتت توضیح بدی"** — Stop describing product details. The image model sees the product. Only composition + lighting + mood.

3. **"روی کامپوزیشن و نور پردازی تمرکز کن کلا"** — Focus exclusively on composition and lighting.

4. **"محصول نباید هیچ تغییر یبکنه"** — Product must remain 100% unchanged. Identity Lock handles this.

5. **"پرامپت هایی که نوشتی هبطی ربطی به ان عکس ها نداره"** — Prompts must STRUCTURALLY match reference images, not just borrow mood.

6. **"سعی کن کلا یه پرامپت حرفه ایی و خوب بدی"** — Give ONE best prompt, not multiple options. User trusts your judgment.

7. **"صرفا یه خوشکلی توجه نکن"** — Don't just make it visually beautiful. The concept must SERVE the product. Golden liquid rejected for sunscreen because it's irrelevant to the product's function.

8. **"عکسی که ازش رفرنس گرفتی رو لازم نیست توی پرامپت بنویسی"** — Reference file names are the agent's tool, not part of the deliverable output.

9. **"ای پرامپتت خیلی بده"** (about green tube with wisps) — Technical descriptions like "ribbon of translucent material" are dead language. Use poetic metaphors: "like smoke", "like light trails", "drift lazily". Image models respond to movement and feeling.

10. **Don't save images until user says so** — User sent green tube for prompt writing, I saved it without asking. Only save when user explicitly requests.

## Concepts Tried

| Concept | Product | Result | Lesson |
|---------|---------|--------|--------|
| Camera specs (f-stops, mm, hex) | SPF 40+ white tube | ❌ Rejected | Camera technician, not creative director |
| Monochrome orange blocks | SPF 40+ white tube | ⚠️ OK | Good structure but too similar to reference |
| Hands cradling + reference match | SPF 40+ white tube | ✅ Good | Structure match + reference = success |
| Cloud floating (kids) | Kids SPF 30+ | ✅ Good | Softness + protection concept |
| Wave form (LOWE ref) | SPF 40+ white tube | ✅ Good | Strong reference backbone |
| Organic curves (SHREDA ref) | SPF 40+ white tube | ✅ Good | Different mood, same structure |
| Liquid gold pool | SPF 30 yellow tube | ❌ Rejected | Visually beautiful but irrelevant to product |
| Morning dew + golden light | SPF 30 yellow tube | ✅ Good | Product-relevant: sunscreen = morning ritual |
| Low angle on skin | SPF 30 yellow tube | ✅ Good | State/position focus, product-relevant |
| Cloud + sun glow | Kids SPF 30+ | ✅ Good | Dual concept: softness + protection |
| Monochrome blocks (Clarins ref) | Tinted Bronze SPF 40+ | ✅ Good | Clean geometry, product-matched color |
| Light wisps like smoke | SYNDA^GE green tube | ⚠️ OK first try | Needed poetic language, not technical |
| Light wisps + smoke metaphor | SYNDA^GE green tube | ✅ Good | "like smoke caught in gentle breeze" |
| Ribbon of light + golden particles | AURUM face oil | ✅ Good | Glass + light refraction = inner glow |

## Key Patterns

- **Tube products** → LOWE wave form (#19) works best as reference backbone
- **Kids products** → Cloud/airy concept with subtle protection element
- **On-skin application** → Low angle makes product heroic
- **Burgundy/dark products** → Wave form or monochrome blocks with color-matched tint
- **Yellow/bright products** → Morning/warmth concepts match the color psychology
- **Green/dark products** → Light wisps + smoke metaphor + thin beam of light
- **Glass/transparent products** → Light passing through, inner glow, refraction
- **POETIC LANGUAGE IS MANDATORY** — "like smoke", "like light trails", "drift lazily" > "ribbon", "translucent element", "curves around"
