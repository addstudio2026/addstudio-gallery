---
name: tma-deployment
description: Deploy Telegram Mini Apps and reference galleries.
---

# Telegram Mini App (TMA) Deployment

This skill governs the process of deploying a visual gallery and a Mini App for product photography references, ensuring seamless connectivity between the Telegram bot, the hosting provider, and the reference database.

## Workflow

1. **Data Preparation**:
   - Ensure a `manifest.json` exists. This file acts as the bridge between the UI and the assets.
   - Structure: `[ { "id": "R001", "url": "images/R001.jpg", "brand": "...", "category": "...", "style": "..." }, ... ]`
2. **Asset Hosting**:
   - All images must be hosted on a public HTTPS server (e.g., GitHub Pages, Vercel, Netlify) to be accessible by the Telegram WebView.
   - Recommended structure: `/images/*.jpg` for assets and `/tma/` or root for the app logic.
3. **TMA Integration**:
   - Include the Telegram Web App SDK: `<script src=\"https://telegram.org/js/telegram-web-app.js\"></script>`.
   - Use `Telegram.WebApp.sendData(id)` to return the selected reference ID to the bot.
   - Call `Telegram.WebApp.ready()` and `Telegram.WebApp.expand()` on load.
4. **Deployment Strategy**:
   - For private repositories, use Vercel or Netlify to maintain repository privacy while providing a public HTTPS endpoint.
   - For public repositories, GitHub Pages is the preferred lightweight option.
   - **Verification Step**: Before pushing the `manifest.json`, the agent MUST:
     1. Run `ls tma/images/` to confirm all referenced files physically exist.
     2. Run `git status` to ensure no critical images are in 'Untracked' state.
     3. Use `git add -f tma/images/` if files are present but not tracked.
     4. Confirm the push was successful via `git log -1` or checking the remote status.
   - **Vercel Sync**: If the UI doesn't update despite a successful push, trigger a dummy commit (e.g., `touch update.txt`) or advise the user to perform a manual 'Redeploy' in the Vercel dashboard.

## Pitfalls & Lessons

- **UI Update Safety (Crucial):** When making "small" changes to `index.html` (e.g., adding a button, changing a style), avoid partial patches. In single-file HTML/JS apps, a single missing closing tag or syntax error in a script block can crash the entire render loop, resulting in a blank screen/no images. 
  - **FIX:** Prefer rewriting the entire file with the change integrated over using `patch` for critical JS logic.
  - **Verification:** After any UI change, you MUST verify that the core functionality (e.g., "do the images still load?") is intact before reporting success. If the grid disappears, immediately rollback to the last known-good version.
- **Private Repo Visibility:** GitHub Pages on private repos is restricted. Use Vercel/Netlify to keep the source private but the endpoint public.
- **Git Identity**: When initializing new repositories for deployment, ensure `git config user.email` and `user.name` are set locally to avoid authentication errors during the first push.
- **The `push -f` Danger Zone**: Never use `git push -f` unless you have a verified local backup of the `.git` directory or a separate backup branch. Force-pushing rewrites remote history and destroys the ability to perform a `git reset --hard` to a known-good state on the server.
- **Connectivity Probe (The 'Ping File')**: When debugging deployment, upload a simple text file (e.g., `ping.txt`) to the root. If `domain.com/ping.txt` is inaccessible, the issue is Vercel-to-Git connectivity or a wrong branch, not the app's internal logic.
- **The Vercel Root Trap**: If the Vercel `Root Directory` is set to a specific folder (e.g., `/tma`), Vercel will NOT deploy any files located outside that folder.
  - **FIX:** Move the `images/` directory INSIDE the root directory specified in Vercel (e.g., `/tma/images/`).
- **Path Resolution**: When images are co-located in the root folder with `index.html`, use relative paths (e.g., `images/ref.jpg`). Avoid absolute paths if the app is deployed as a sub-project on a shared domain.
- **Bot Interaction (The 'Send' Problem)**: `tg.sendData()` only functions when the TMA is launched via a `KeyboardButton`. For users who open the app via other means, `tg.sendData` will fail silently.
  - **FIX:** Implement a "Copy ID" button as the primary action. If a redirect to the bot is needed, use the pattern: `Copy ID` $\\rightarrow$ `Redirect to Bot via https://t.me/bot?start=ID` $\\rightarrow$ `User Pastes`. This is the only universal flow that works for all users.
- **The 'Nothing to Commit' Trap**: If `git add` reports no changes but images are missing from the gallery, verify if the files actually exist in the target directory via `ls`. Do not trust `git status` alone; binary assets can be missed if not explicitly added.
- **Manifest-Image Mismatch**: Always verify that image filenames on disk match exactly the `url` entries in `manifest.json`. A single character difference or casing issue results in 404s.
- **Vercel Cache (Versioned Manifests)**: Major changes to `manifest.json` or filenames often require a manual 'Redeploy' in Vercel. To force a refresh without a manual redeploy, version the filename (e.g., `manifest_v2.json`) and update the `fetch()` call in `index.html` to the new version.
- **The Manifest-Source Gap**: Never generate the manifest from memory. The mandatory sequence is: `Update INDEX.md` $\\rightarrow$ `Copy Images to tma/images/` $\\rightarrow$ `Generate manifest.json FROM INDEX.md` $\\rightarrow$ `Git Push`. If `INDEX.md` is not updated, the UI will not reflect new additions regardless of whether images were pushed.
- **Remote Authentication**: When pushing to a new public repo via CLI, using a Personal Access Token (PAT) in the remote URL (`https://<token>@github.com/...`) is the most reliable way to bypass interactive login prompts in headless environments.

## Verification
- Open the deployed URL in a browser $\\rightarrow$ Check if images load.
- Open the URL inside Telegram $\\rightarrow$ Select a reference $\\rightarrow$ Verify the ID is sent to the bot.
