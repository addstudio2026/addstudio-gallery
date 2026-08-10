Prompt Gen Workflow: Product Img -> Match R001-R046 Ref -> User Approval -> Read .yaml tag (Source of Truth) -> Final Prompt.
§
⚠️ TAGGING IS PRIMARY: Every reference = full YAML tag on disk (references.yaml + INDEX.md + individual .yaml file in /tags/). NEVER skip. Batch images = individual tags each. R{NNN}_{category}_{brand}_{layout}.jpg format. 11 sections, 18 required fields. ⚠️ ALWAYS load product-shot-prompts skill FIRST.
§
Backup to GitHub (https://github.com/addstudio2026/ADDSTUDIOhERMES) is manual only. Script at /data/hermes-backup/backup.sh. Port 22 blocked, HTTPS only. ⚠️ backup.sh only stages (git add), NEVER commits. After running it: 1) show what changed, 2) `git commit`, 3) `git push origin main`. False "Everything up-to-date" = files weren't committed. When reading YAML for processing: use `terminal(cat <path>)` NOT `read_file` (line-numbered output breaks parsers). To recover tags from history: search `tool_calls` in session JSON, not message content.
§
Always deliver ONE best prompt, not multiple options. ALWAYS visually analyze hero reference images first — do NOT just read SKILL.md text alone. References are style anchors. The prompt must stand alone. ⚠️ CRITICAL: NEVER describe product details (colors, text, materials, label) in prompts — the product image is already provided to the image model. Only write: composition, lighting, mood, STATE/POSITION. Identity Lock = just "product remains 100% unchanged".
§
CRITICAL BUG: MIMO2.5 enters infinite loops calling same tool 100+ times. Stop after 5 identical calls, max 10 per response. Added LOOP SAFETY RULE to SOUL.md.
§
User requires strict adherence to YAML reference data; visual analysis secondary. R039: Neo-Minimalism. User also uses ComfyUI (Qwen 2.5 VL + RMBG-2.0 + LoRA Lightning) for person-placement workflows.
§
User explicitly abandoned password system (2026-08-09). Do NOT ask for passwords. `hermes send --to telegram:chat_id msg` sends messages to other users. Available: Ali, Alireza Emtiaz, m4dsi.
§
User requires strict adherence to the 11-section standard for reference tagging; shortened YAMLs are unacceptable. Quality always takes priority over speed.