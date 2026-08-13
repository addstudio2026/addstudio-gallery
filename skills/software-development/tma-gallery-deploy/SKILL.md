---
name: tma-gallery-deploy
description: Deploy and restore TMA galleries on Vercel via GitHub.
---

# TMA Gallery Deployment & Recovery

Guidelines for deploying and restoring product photography reference galleries for a TMA.

## Trigger
Use when deploying, updating, or recovering a reference gallery for a TMA.

## Deployment Standard (Vercel Root)
To avoid deployment failures where the app loads but content is missing:
1. **Root-Level Architecture:** All core files MUST be in the root directory.
   - `/index.html` (Root)
   - `/manifest.json` (Root)
   - `/img/` (Root folder for all Rxxx.jpg files)
2. **Vercel Config:** Ensure 'Root Directory' in Vercel Project Settings is set to `./` (Root), NOT a subdirectory like `/tma`.
3. **Manifest Sync:** The `manifest.json` must use relative paths starting with `img/` (e.g., `"url": "img/R001.jpg"`).

## Luxury UI Requirements
When implementing or restoring the gallery, ensure these "Luxury" features are present:
- **Layout:** Masonry Grid (column-count: 2 or 3).
- **Loading:** Skeleton screens with shimmer animation during image load.
- **Interaction:** Modal Sheets (sliding from bottom) instead of alerts for reference details.
- **Copy Utility:** A "Copy ID" button in the modal that copies the reference ID to the clipboard and triggers a centered Toast notification at the bottom of the screen.
- **Minimalism:** Filter chips should only show Categories, not Brands, to keep the header clean.

## Pitfalls
- **Nested Folders:** Avoid placing the project inside a folder named `tma/` or `addstudio-gallery/` within the repo; this often leads to 404s on Vercel unless the Root Directory setting is explicitly changed.
- **Image Path Mismatch:** Never use `/images/` if the folder is named `img/`. Consistency between `manifest.json` and the folder name is mandatory.
- **Branch Mismatch:** Using `master` locally but pushing to `main` on remote can cause deployment failures. Always ensure `git branch -m main` is called before pushing.
- **Case Sensitivity:** Ensure image extensions (.jpg vs .JPG) match the manifest exactly.

## Verification
- Check direct file access via `https://<app-url>/manifest.json`.
- Verify image access via `https://<app-url>/img/Rxxx.jpg`.
