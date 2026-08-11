---
name: tma-gallery-sync
description: Use when syncing images and manifests for the TMA gallery.
---

# TMA Gallery Synchronization

This skill governs the process of syncing product reference images and their corresponding metadata (manifest.json) between a local project directory and a public GitHub repository used for Vercel deployments.

## 🛠 Workflow

### 1. Image Sync
- **Pathing**: Images must be placed in `tma/images/`.
- **Naming Convention**: Use a simple, consistent ID-based naming scheme (e.g., `R001.jpg`, `R002.jpg`) to avoid encoding issues and cache mismatches.
- **Verification**: Always run `ls -la tma/images/` to physically verify files exist on disk before committing.

### 2. Manifest Generation
- **Source of Truth**: The `INDEX.md` or individual `.yaml` files in the `tags/` directory are the authoritative sources.
- **Metadata Extraction**:
    - Basic: `id`, `brand`, `category`, `url`.
    - Advanced: `lighting`, `composition`, `props`, `cluster` (grouped looks).
- **Logic**:
    - Group similar styles into **Clusters** (e.g., Clinical, Luxury, Nature, Surreal) to prevent UI clutter and improve UX.
    - Ensure `url` matches the simplified filename (e.g., `images/R001.jpg`).

### 3. Deployment & Verification
- **Git Flow**: `git add .` $\rightarrow$ `git commit` $\rightarrow$ `git push origin main`.
- **Vercel Cache**: Vercel often caches the `manifest.json`. If updates aren't visible:
    - Change the manifest filename (e.g., `manifest_v2.json`) and update `index.html`.
    - Trigger a **Manual Redeploy** via the Vercel Dashboard.
- **Verification**: Test a direct URL to a new image (e.g., `https://<app>.vercel.app/images/R115.jpg`) to confirm upload success before debugging JS.

## ⚠️ Pitfalls & Lessons
- **Silent Failures**: `git commit` may return "nothing to commit" if files are untracked or paths are slightly off. Always verify the file exists in the target folder first.
- **Bot Integration**: 
    - `tg.sendData` only works when the app is opened via a Keyboard Button.
    - Use Deep Linking (`https://t.me/bot?start=ID`) as a fallback for all other entry points.
- **Look-based Filtering**: Users prefer filtering by "Overall Look" (Clusters) rather than specific product categories.

## 📋 Verification Checklist
- [ ] All images exist in `tma/images/` with simple names.
- [ ] `manifest.json` contains all references up to the latest ID.
- [ ] Bot link is exactly `@addstudiobot` (case-sensitive, no underscores).
- [ ] Vercel Redeploy triggered after major manifest changes.
