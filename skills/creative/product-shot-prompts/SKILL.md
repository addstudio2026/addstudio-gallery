---
name: product-shot-prompts
description: Locked-style product photography prompts for image gen.
---

# Product Photography Prompt Engineer

Takes a new product image and produces an image-generation prompt matching a permanently locked brand visual style.

## Two-Layer Memory

L1: Style as technical/numeric data in Section A (persists in .md). L2: 3 hero reference images (only passed to image model at generation time).

## Section A — LOCKED STYLE MEMORY

Permanent brand DNA. Derived once, now immutable. Every value is a hard constraint.

Fields: camera (angle, height, distance, lens_equiv, aperture, perspective), lighting (key, fill, rim, shadow_direction, shadow_softness, shadow_opacity, specular_behavior), background (type, colors_hex, gradient_direction, texture, surface, contact_shadow), color_grading (white_balance, contrast, saturation, black_point, highlight_rolloff, dominant_palette_hex), composition (product_scale_percent, framing, headroom, aspect_ratio, negative_space), rendering (sharpness, grain, finish), mood_keywords, always_avoid.

If fields are empty, refuse to generate and tell user to run BOOTSTRAP first.

## Modes

BOOTSTRAP: Study reference images, fill Section A with forensic numeric values, output updated file, stop. GENERATE: Write prompt using the model-style format below. VARIANTS: Change only product position/placement. CRITIQUE: Score 0-10 per axis, revise if below 7.

## ⚠️ CRITICAL — Workflow Checkpoint (MUST do before ANY action)

**Before doing anything else in a session, ALWAYS:**
1. **Load this skill** (product-shot-prompts) with `skill_view`
2. **Load `poster-addstudio-v01`** if generating prompts
3. **Check `references/reference-tagging-format.md`** for latest tagging format
4. **THEN start working**

User explicitly corrected: "اسکیل واست نوشتم که احمق" — do NOT skip skill loading. The skill contains corrections and workflows that prevent repeated mistakes.

---

## ⚠️ CRITICAL — Prompt Writing Rules (learned from user corrections)

1. **NEVER describe product details in the prompt text.** The product image is already provided to the image model. Just say "the product" or "the uploaded product". Colors, text, materials, shape — all invisible to the prompt. The model sees the image.
2. **BUT always describe product STATE/POSITION.** Whether it's floating, tilted, standing, lying, suspended, cradled, leaning — this IS composition and must be in the prompt.
3. **Focus on: composition, lighting, mood/style.** That's it. Not f-stops, not mm, not hex codes for the product.
4. **Keep it SHORT.** ~80-120 words. 3 clean conceptual sections, not a technical spec sheet.
5. **Match reference image style.** Mention "styled exactly like [reference image name]" as the visual bible.
6. **Use poetic metaphors, NOT technical descriptions.** "wisps of light curl like smoke" ✅ not "ribbon of translucent material" ❌. "glowing particles drift lazily" ✅ not "scattered light elements" ❌. Image models respond to MOVEMENT and FEELING, not shapes and materials. Every visual element should have a simile or metaphor that makes it feel alive.
7. **Don't save images until user explicitly says so.** When user sends a product image for prompt writing, write the prompt first. Only save if user says "ذخیره کن" or similar. HOWEVER: REFERENCE images (from other brands, for style bootstrapping) ARE auto-saved immediately — the user sends many and expects auto-save. DISTINCTION: product images = wait for command. Reference images = save now.

## Prompt Format (Model-Style — the ONLY format to use)

```
A photorealistic [category] campaign image of the product [STATE/POSITION description].

[BACKGROUND — what surrounds it, surface, environment]

[LIGHTING — direction, warmth, mood, shadows]

[STYLE LINE — aesthetic keywords, reference to matching hero image, aspect ratio]
```

~80-120 words total. No product details. Only composition + lighting + mood.

**Why this format:** User explicitly rejected longer technical prompts (350+ words with f-stops, mm, hex codes). Short conceptual prompts produce better results because the image model makes better creative decisions when given concepts rather than specs. "Less is more" — every word must earn its place.

## Output

Prompt (80-120 words, flowing English, Model-Style format) + Identity Lock.

**Identity Lock format (MANDATORY):**
```
## Identity Lock
- Product remains 100% unchanged, no modifications to shape, color, label, or branding
- Preserve label artwork exactly as in the reference image, do not regenerate or re-typeset any text
```

**NEVER list product details in Identity Lock.** No colors, no fonts, no label elements, no materials. The user explicitly corrected this. The image model sees the product — it doesn't need you to describe it.

No 11-slot template. No technical specs in the prompt body. No reference file names in the output. Just concept + composition + lighting + mood. The prompt must stand alone — the user feeds it directly to the image model.

## Hard Rules

Product fidelity absolute. Never invent label text. No props unless asked. Prompt in English always. No hedging. Under 220 words.

## Reference Image Collection Protocol (v2.1)

**File naming:** `R{NNN}_{category}_{brand-or-unknown}_{layout}.jpg` — `R{NNN}` is the unique key, never changes.

### Save behavior
- **REFERENCE** (brand style bootstrapping) → auto-save + tag in the same message.
- **PRODUCT** (user's own product) → **do NOT save**. Write prompt first. Only save if user explicitly says "ذخیره کن" or similar.
- **Ambiguous?** Ask one short question. Do not auto-save.

**Storage Strategy (Individual Tags):**
To ensure maximum reliability and avoid corruption of large central files, every reference MUST have its own individual YAML file in the `tags/` directory (e.g., `/data/workspace/addstudio-v01/tags/R031.yaml`). While a central `references.yaml` may exist for legacy/quick-scan reasons, the **individual files are the primary source of truth**.

### Dual output (mandatory)
Every image gets TWO outputs:

**A) One-liner for quick scanning:**
```
- `R027` — SYNSKIN Acnes Toner | matte white tube, cool teal gradient, floating 15° tilt, water bubbles, soft diffused key + cold rim, 9:16 story, "clinical / aquatic-fresh" 🔵
```

**B) Individual YAML file:** Create a separate `.yaml` file for the reference in the `tags/` directory following the 11-section format. Update `INDEX.md` with the one-liner.


## ⚠️ CRITICAL VERIFICATION RULE
Before confirming a tagging task is complete, the agent MUST verify that the resulting files are NOT empty and contain all 11 required forensic sections. NEVER rely on the output of a script that only checks for file existence or counts lines; physically read a sample of the files to ensure they aren't just stubs or truncated summaries.

## 🛠️ DATA INTEGRITY WORKFLOW
When splitting a central `references.yaml` into individual `Rxxx.yaml` files:
1. Read the source file using a method that preserves all content (e.g., `cat` via terminal) to avoid line-number prefixes or truncation.
2. Use explicit markers (e.g., `---`) to split blocks.
3. Write each block to its own file.
4. **Verify:** Read back a random sample of created files to confirm full content (11 sections) is present before reporting success to the user.
5. **GitHub Sync:** Ensure the `git add` command specifically targets the directory containing the new files to prevent 'nothing to commit' errors when files were already present but empty.
6. **Forensic Restoration:** If data is lost or truncated in the files, the agent MUST reconstruct it manually from the conversation history (History) rather than relying on corrupted disk states.
7. **Atomic Commits:** When syncing to GitHub, ensure files are staged (`git add`) and committed before pushing to avoid 'Everything up-to-date' false positives when files are missing from the index.

### Retrieval (for product prompts)
When user sends their own product image:
1. Extract: category, container_type, container_material, dominant colors, opacity, label busyness
2. Match against index (container_type 30%, category 20%, fits 20%, color 15%, difficulty 10%, mood 5%)
3. Return top 3 references with id, thumbnail, why-it-fits
4. Take chosen prompt_seed → fill placeholders → adapt to product's palette → output final prompt

### Acceptance criteria
A tag is REJECTED if:
- Any `required` field is empty or `TBD`
- `props` present but `prop_placement` missing
- `concept_idea` < 8 words
- `prompt_seed` has no placeholders (= generic)
- Brand guessed without evidence → must be `unknown`

**18 required fields:** category, container_type, palette_product, palette_scene, color_temperature, placement, camera_angle, product_scale, props, lighting_quality, key_direction, shadow_type, background_type, surface, layout_archetype, negative_space, mood, concept_idea, prompt_seed

## Pitfalls

- **⚠️ ALWAYS load this skill FIRST.** Before doing any product photography work, call `skill_view(name='product-shot-prompts')` and `skill_view(name='poster-addstudio-v01')`. The user explicitly said: "اسکیل واست نوشتم که احمق" — skipping skill loading causes repeated mistakes that are already solved in the skill files.
- **⚠️ `backup.sh` does NOT auto-commit.** The script at `/data/hermes-backup/backup.sh` only stages files (`git add`). After running it, you MUST manually run `git commit` and `git push`. Failing to do this causes "Everything up-to-date" false positives when files are missing from the remote. Always: `backup.sh` → `git commit` → `git push`.
- **⚠️ `read_file` returns line-numbered output (`1|content`).** This breaks YAML parsing in scripts. When reading `references.yaml` or any YAML file for processing, use `terminal(command="cat <path>")` instead of `read_file` to get clean unnumbered content. The `execute_code` tool's `read_file` also returns structured data — access raw content via `terminal('cat ...')` for reliable text extraction.
- **⚠️ Session history tag recovery requires searching `tool_calls`.** When forensic tags were written via `write_file` tool calls (not displayed in chat messages), you must search the session JSON's `tool_calls` array, not just message content. Use `json.loads(func.get("arguments", "{}"))` to extract the `content` field from `write_file` calls.
- Always keep `locked: true`. Once bootstrap is done, Section A is immutable.
- 5 well-matched references beat 20 inconsistent ones. If bootstrap must average between two conflicting lighting setups, the result will be lifeless.
- Version your files: use `version: X.Y` in frontmatter. When you want to change style, create a new version and keep the old one — sometimes the previous version was better.
- **Outlier identification**: During BOOTSTRAP, identify images that deviate from the dominant pattern (e.g., hard sporty lighting, collage format, non-warm palette). Exclude them from the locked-style derivation. Note them in the output so the user knows which references were excluded and why. \n- **Symmetry and Architectural Balance**: When tagging architectural props (stairs, arches, geometric blocks), explicitly capture the balance between rigid lines and organic accents. Ensure the `layout_archetype` reflects the architectural nature (e.g., `hero_center_pedestal` for stairs/plinths).
- **⚠️ CRITICAL — Creative Director, NOT Camera Technician**: The user explicitly corrected a prompt written as camera specs with no creative concept. User said: "اصلا خوب نیست و شبیه به عکس ها نشده" (not good, doesn't look like the images). A technically correct prompt without a story/concept is worthless. See "Creative Director Mode" below.
- **⚠️ CRITICAL — Never include reference file names in prompt output.** The reference is the agent's thinking tool, not part of the deliverable. The prompt must stand alone.
- **⚠️ CRITICAL — Concept must serve the product.** A visually beautiful concept that has nothing to do with the product is a failure. Always ask: "What does this product DO and does this image tell THAT story?" Sunscreen → protection/morning. Serum → luxury/precious. Cleanser → freshness/clarity. Match concept to function.
- **User may request product material/finish changes**: If user says "cream should be visible" or "liquid should be white" or "tilt the product", update Identity Lock to include those modifications. Core brand elements (logo, text, shape, colors) stay locked; user-requested material/finish/pose changes are part of the new product identity.
- **⚠️ CRITICAL — Disk Persistence**: Every save must be atomic across BOTH `references.yaml` and `INDEX.md`. Showing tags in chat without writing them to disk is an INCOMPLETE save. Verify that both files are updated and pushed to the backup repository to prevent data loss between sessions.
- **⚠️ CRITICAL — Batch images = individual tags.** When user sends multiple images at once, each image gets its OWN full YAML tag (one-liner + complete YAML block). Never batch them together or skip individual tagging. User explicitly corrected: "ببین باید همه رو تگ گذاری کنی جدا جدا".
- **⚠️ CRITICAL — Visual analysis must be FORENSIC.** When tagging references, describe EVERY visible element: props, VFX, textures, surface details. MISS NOTHING. Missing a prop (e.g., gel shapes behind a bottle) means the tag is wrong and the user will correct you. Use a multi-step forensic breakdown (Product, Props, VFX, Background, Lighting, Palette). If you can see it, tag it.

---

## Creative Director Mode (MANDATORY for GENERATE)

**Load `poster-addstudio-v01` skill alongside this skill during GENERATE.**

The 11-slot template provides the TECHNICAL foundation. But a prompt without a creative concept is a lifeless spec sheet. Before filling slots 1-11, you MUST:

### Step 0 — Think Like a Creative Director

1. **Pick a REFERENCE IMAGE** from hero references that best matches the product CATEGORY (tube → Clarins-style, bottle → MI×IT-style, dropper → La Roche-Posay-style).
2. **SHOW the reference to the user first** — send the image, wait for approval. Do NOT write the prompt until the user confirms the reference.
3. **What is the PRODUCT'S STORY?** Not "what is it" but "what does it MEAN to the user?" (e.g., sunscreen = protection, serum = luxury ritual, cleanser = fresh start)
4. **What VISUAL METAPHOR communicates that story?** (e.g., shield in sunlight, monument in light, wave of cream, hands cradling something precious)
5. **What will the viewer FEEL in 3 seconds?** (trust, aspiration, calm, power, tenderness)
6. **What is the SINGLE FOCAL POINT?** (product = hero, always)

### Step 1 — Write the Concept Line

Before the prompt, write ONE sentence in Persian explaining the creative concept:

```
**کانسپت:** [one-line concept in Persian]
**رفرنس:** [which hero reference image you're basing it on]
```

### Step 2 — Then Write the Prompt

Use the Model-Style format (3 sections, ~100 words). Every clause should SERVE the concept. Never describe product details — the image model sees the product. Only describe: product STATE/POSITION, composition, lighting, mood. Section A values (lighting, background, color grade) inform the concept but are NOT listed as specs in the prompt.

### Step 3 — ONE Best Prompt (Default)

**DEFAULT: Deliver exactly ONE best prompt.** Not three options. Not a menu. The strongest creative concept, confidently. The user trusts your judgment — prove it.

**When to give multiple:** ONLY when user explicitly asks ("ایده بده", "چند تا ایده بده", "alternatives"). Then give 2-3 genuinely different concepts with distinct visual metaphors and different reference backbones.

**Reference images are ALWAYS used** unless the user explicitly says not to. Never write a prompt without anchoring it to a specific hero reference image. The reference provides the structural backbone — composition, lighting setup, spatial relationships. The prompt must MATCH the reference image's structure, not just borrow its mood. If the reference has a wave form, the prompt must describe a wave form. If the reference has hands cradling, the prompt must describe hands cradling. NEVER use a reference for mood only while inventing a completely different composition.

**⚠️ CRITICAL — Reference files are YOUR tool, not the deliverable.** Never include reference image file names (e.g., "19-lowe-advanced-lotion-wave.jpg") in the prompt output. The user corrected this explicitly. The reference shapes your thinking; the prompt stands alone. If the user asks for the source, then provide it.

**⚠️ CRITICAL — Structure Match Test:** Before outputting, ask yourself: "If someone looked at the reference image and this prompt side by side, would the PROMPT describe the SAME composition?" If the reference has a wave form, the prompt must describe a wave form. If the reference has hands cradling, the prompt must describe hands cradling. NEVER use a reference for mood only while inventing a completely different composition.

**⚠️ CRITICAL — Product-Concept Alignment Test:** Before outputting, ask: "What IS this product, and does this image SERVE it?" A concept that is visually beautiful but irrelevant to the product is a failure. The golden liquid pool was rejected for a sunscreen-on-oily-skin because honey-like viscosity has nothing to do with lightweight mineral protection. Every concept must answer: What does this product DO for the user? How does the visual tell THAT story? Sunscreen → morning ritual, protection, light. Serum → luxury ritual, preciousness. Cleanser → freshness, clarity. Match the concept to the product's function and the user's need.

### Example of BAD vs GOOD

**BAD (camera technician):**
> "A vertical product photo with 85mm lens at f/2.8, key light upper-left at 45 degrees, soft fill from right, gradient background #FDF5E6 to #E2C4A3..."

**BAD (correct concept, wrong language):**
> "...a translucent ribbon of soft warm light curls around the product..." — technical, mechanical, dead.

**GOOD (creative director + poetic language):**
> "A photorealistic luxury skincare campaign image of the product floating weightlessly at a slight tilt in a soft pale sage-green environment, thin wisps of warm white light curl around the product like smoke caught in a gentle breeze, glowing particles drift lazily through the air catching the light as they pass, a narrow focused beam of warm white light strikes the tube from above at a slight angle creating a crisp luminous highlight along its surface..."
