When user sends images to save: save immediately without asking, tag with sequential number + short label, reply with confirmation. Don't wait for explicit "save" command.
§
addstudio-v01 reference images being collected in /data/workspace/addstudio-v01/. Currently 5 images (01-05): MI×IT serum, O'GULIA collage, hand cream, O'GULIA cleansing gel, SKIN1004 centella. More expected.
§
Saved PRODUCT_SHOT_SKILL.md (v1.0, locked style memory bootstrapped from 19 reference images) at /data/workspace/addstudio-v01/PRODUCT_SHOT_SKILL.md. Hero refs: 01, 04, 05, 12, 16, 18. Outliers excluded: 08, 09 (hard sport light), 02 (collage), 14 (pink palette). poster-addstudio-v01 skill also saved in Hermes skills (creative category).
§
When writing image-generation prompts for product photography: never describe product details (colors, text, materials) — the image is already provided. BUT always describe the product's STATE/POSITION: floating, standing, tilted, lying, suspended, cradled, leaning, etc. This is composition, not description. Focus the prompt on: 1) product position/state, 2) composition, 3) lighting, 4) mood/style.
§
Backup to GitHub (https://github.com/addstudio2026/ADDSTUDIOhERMES) is manual only — NO cron job. When user asks for backup: 1) run backup.sh, 2) show what changed, 3) ask for confirmation before pushing. Token stored in remote URL. Script at /data/hermes-backup/backup.sh. Port 22 blocked, using HTTPS only.
§
Always deliver ONE best prompt, not multiple options, unless user explicitly asks for alternatives. Always use reference images from the library as style anchors unless user says otherwise. Give the strongest creative direction confidently.
§
Reference image file names should NOT appear in the prompt output. The reference is the agent's tool for shaping the prompt, not part of the deliverable. Only include "Style Source" or reference file names if the user explicitly asks. The prompt itself should stand alone.