When user sends reference images for a project library: save immediately, tag with sequential number + rich description, reply with confirmation. When user sends product images just for prompt writing: do NOT save until user explicitly asks.
§
Saved PRODUCT_SHOT_SKILL.md (v1.0, locked style memory bootstrapped from 19 reference images) at /data/workspace/addstudio-v01/PRODUCT_SHOT_SKILL.md. Hero refs: 01, 04, 05, 12, 16, 18. Outliers excluded: 08, 09 (hard sport light), 02 (collage), 14 (pink palette). poster-addstudio-v01 skill also saved in Hermes skills (creative category).
§
Use vivid metaphors and similes (like smoke, like light trails) instead of technical descriptions (ribbon, translucent element). Poetic movement language guides image models better than shapes. Always describe product's STATE/POSITION. Focus on composition + lighting + mood.
§
Backup to GitHub (https://github.com/addstudio2026/ADDSTUDIOhERMES) is manual only — NO cron job. When user asks for backup: 1) run backup.sh, 2) show what changed, 3) ask for confirmation before pushing. Token stored in remote URL. Script at /data/hermes-backup/backup.sh. Port 22 blocked, using HTTPS only.
§
Always deliver ONE best prompt, not multiple options, unless user explicitly asks for alternatives. Always use reference images from the library as style anchors unless user says otherwise. Give the strongest creative direction confidently.
§
Reference image file names should NOT appear in the prompt output. The reference is the agent's tool for shaping the prompt, not part of the deliverable. Only include "Style Source" or reference file names if the user explicitly asks. The prompt itself should stand alone.
§
SYNSKIN ACNES line: Toner (seboregulating), Gel-Cleanser (purifying), Gel-Cream Step3 (restoring). Visual language: cool blue, clinical clean, gel textures, foam, droplets.