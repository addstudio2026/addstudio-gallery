---
name: vercel-static-deploy
description: Use when deploying static galleries or TMA to Vercel.
---

# Vercel Static Site Deployment (TMA/Gallery)

Use when deploying simple static galleries or Telegram Mini Apps (TMA) to Vercel via GitHub. This skill ensures correct folder structures and pathing to avoid common "folder not found" or "empty page" errors during deployment.

## 🚀 Workflow

1. **Verify Root Directory Setting**: Determine if Vercel is configured to look at the repository root or a specific subdirectory (e.g., `/tma`).
2. **Structure Alignment**:
   - **Root Deployment**: `index.html` and `manifest.json` must be in the root. Images should be in `/img` or `/images`.
   - **Subfolder Deployment**: All assets must be inside the designated folder (e.g., `/tma/index.html`, `/tma/manifest_v3.json`, `/tma/img/...`).
3. **Path Consistency**: Ensure `manifest_v3.json` URLs match the physical folder structure relative to `index.html`.
4. **Git Push**: Use `git push -f origin main` only when a hard reset of the remote state is required to clear nested folder artifacts.

## ⚠️ Pitfalls & Lessons

- **The "Nested Folder" Trap**: Avoid pushing a local folder (e.g., `addstudio-gallery/`) into a repository of the same name. This creates a `repo/repo/tma` structure that breaks Vercel's root detection. Always `cd` into the target directory before `git init` or `git add`.
- **Vercel Build Cache**: If files are pushed but not visible, the issue is often Vercel's build queue or browser cache. Use a "ping file" (e.g., `ping.txt`) in the root to verify live connectivity.
- **Case Sensitivity**: Vercel/Linux environments are case-sensitive. `Img/` is not the same as `img/`.
- **Git Identity**: When automating pushes in a new environment, remember to set `git config user.email` and `git config user.name` to avoid commit failures.

## ✅ Verification Protocol
- Run `git ls-tree -r main --name-only` to verify the actual paths on the remote server.
- Test direct URLs to assets (e.g., `domain.com/manifest_v3.json`) before checking the UI.
