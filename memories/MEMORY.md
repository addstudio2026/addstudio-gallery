Prompt Gen Workflow: Product Img -> Ref Proposal + Image -> Approval -> YAML Read -> Prompt.
§
⚠️ TAGGING: Full 11-section YAML per ref in /tags/. No skips. R{NNN}_{cat}_{brand}_{layout}.jpg. Load product-shot-prompts skill FIRST.
§
Backup to GitHub (https://github.com/addstudio2026/ADDSTUDIOhERMES): script at /data/hermes-backup/backup.sh. ⚠️ backup.sh only stages; MUST follow with `git commit` and `git push`. Use `terminal(cat <path>)` for YAML to avoid line numbers. To recover tags: search `tool_calls` in session JSON.
§
Always deliver ONE best prompt, not multiple options. ALWAYS visually analyze hero reference images first — do NOT just read SKILL.md text alone. References are style anchors. The prompt must stand alone. ⚠️ CRITICAL: NEVER describe product details (colors, text, materials, label) in prompts — the product image is already provided to the image model. Only write: composition, lighting, mood, STATE/POSITION. Identity Lock = just "product remains 100% unchanged".
§
User requires strict adherence to YAML reference data; visual analysis secondary. R039: Neo-Minimalism. User also uses ComfyUI (Qwen 2.5 VL + RMBG-2.0 + LoRA Lightning) for person-placement workflows.
§
User explicitly abandoned password system (2026-08-09). Do NOT ask for passwords. `hermes send --to telegram:chat_id msg` sends messages to other users. Available: Ali, Alireza Emtiaz, m4dsi.
§
User requires strict adherence to the 11-section forensic standard for tagging; shortened YAMLs are unacceptable. Quality/detail over speed.
§
TMA Gallery (Vercel): Root Dir=root, images in 'img/', metadata in 'manifest.json'. Prefers minimal header chips (categories only, no brands).
§
User has zero tolerance for repeated references; once rejected, do NOT propose again in session. Every reference proposal MUST include the image in the same message.
§
Zero tolerance for empty/missing YAMLs; zero-byte files = failure.
§
User expects 'Hard-Verify' protocol for gallery: 1) Disk check, 2) INDEX.md sync, 3) Git verify, 4) Link test.