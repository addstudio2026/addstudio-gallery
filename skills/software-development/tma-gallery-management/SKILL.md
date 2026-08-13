---
name: tma-gallery-management
description: Use when managing the ADDSTUDIO Gallery TMA. Syncs images, manifests, and UI.
---

# TMA Gallery Management

This skill governs the maintenance and deployment of the ADDSTUDIO Reference Gallery, a Telegram Mini App used for visual reference selection.

## Workflow

1. **Metadata Sync**: Ensure `INDEX.md` (Source of Truth) is up-to-date before regenerating `manifest.json`.
2. **Manifest Generation**:
   - Use `manifest_v3.json` for enhanced metadata (lighting, composition, props).
   - Group references into **Clusters** (Clinical, Luxury, Nature, Surreal) to prevent UI clutter.
3. **Asset Deployment**:
   - Store images as `Rxxx.jpg` in `tma/images/`.
   - Use `git add -f` for images to bypass `.gitignore` if necessary.
   - Force push (`git push -f origin main`) when rebuilding the gallery from scratch.

## UX Standards

- **Silent Copy**: Copying an ID must be a silent operation. No `alert()` or confirmation dialogs.
- **Toast Feedback**: Use a temporary, self-vanishing toast notification (e.g., centered bottom, fade-out) for copy confirmation.
- **Button Aesthetics**: 
    - "Copy ID" buttons must be `width: fit-content` and centered to avoid a "blocky" look.
    - Implement subtle hover effects to provide tactile feedback.
- **Bot Integration**: Use direct deep-links (`https://t.me/addstudiobot?start=ID`) for the 'Send to Bot' functionality.
- **Filtering**: Prioritize Style/Look clusters over product categories.

## Pitfalls & Recovery

- **Recovery from State Loss**: If the local `tma/` folder is corrupted or missing:
    1. Sync all `Rxxx.jpg` from project root and cache.
    2. Regenerate `manifest_v3.json` by parsing `INDEX.md`.
    3. Restore `index.html` from the latest stable template.
- **Git Auth**: To avoid `fatal: unable to auto-detect email address`, always set local identity:
  `git config user.email "you@example.com" && git config user.name "Your Name"`
- **Vercel Cache**: Changes to `manifest.json` or images often require a manual **Redeploy** in the Vercel dashboard.
- **Bot Start Parameter**: The `?start=` parameter only works for users who haven't started the bot before. For existing users, "Copy ID" is the only reliable flow.

## Verification (Hard-Verify)
1. **Physical Check**: `ls tma/images/` to ensure images exist.
2. **Sync Check**: Verify `manifest_v3.json` matches `INDEX.md`.
3. **Git Verify**: Check `git log` to confirm the commit landed.
4. **Link Test**: Verify the deployed Vercel URL.
