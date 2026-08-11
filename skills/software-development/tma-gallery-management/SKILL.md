---
name: tma-gallery-management
description: Use when managing the ADDSTUDIO Reference Gallery TMA.
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
- **Toast Feedback**: Use a temporary, self-vanishing toast notification for copy confirmation.
- **Bot Integration**: Use direct deep-links (`https://t.me/addstudiobot?start=ID`) for the 'Send to Bot' functionality.
- **Filtering**: Prioritize Style/Look clusters over product categories.

## Pitfalls & Troubleshooting

- **Vercel Cache**: Changes to `manifest.json` or images often require a manual **Redeploy** in the Vercel dashboard to take effect.
- **Bot Start Parameter**: The `?start=` parameter only works for users who haven't started the bot before. For existing users, a 'Copy ID' button is the only reliable flow.
- **Git Auth**: When deploying to the public gallery repo, ensure the correct Personal Access Token (PAT) is used in the remote URL to avoid `fatal: could not read Username` errors.
- **Path Mismatches**: Always verify the exact location of the `tma/` folder relative to the git root before running `git add`.
