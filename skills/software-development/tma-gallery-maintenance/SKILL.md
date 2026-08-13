---
name: tma-gallery-maintenance
description: Use for managing the TMA reference gallery.
---

# TMA Gallery Maintenance

This skill governs the synchronization of reference images and metadata between the local project workspace, the gallery repository, and the live Vercel deployment.

## Core Workflow
1. **Physical Sync**: Ensure images exist in `tma/images/Rxxx.jpg`. Check both project directories and agent cache.
2. **Manifest Sync**: Generate/Update `manifest_v3.json` using `INDEX.md` as the source of truth.
3. **Git Deployment**: Use a Personal Access Token (PAT) for authentication to push changes to the public gallery repo.
4. **Verification**: Check if missing IDs in the gallery correspond to missing files on disk or missing entries in the manifest.

## Critical Pitfalls & Lessons
- **Deep Linking Limitation**: `t.me/bot?start=ID` only works for first-time users. For returning users, the `start` parameter is ignored.
- **Mini App Data**: `tg.sendData` only works if the app was opened via a Keyboard Button.
- **Best UX for Copying**: Avoid `alert()` popups. Use a transient 'Toast' notification and a 'Copy ID' button with a hover effect.
- **Git Auth**: Standard `git push` often fails in isolated environments; use the token in the remote URL: `https://<token>@github.com/user/repo.git`.
- **Manifest Consistency**: Always ensure the `url` field in the manifest matches the actual filename on disk (e.g., `images/R001.jpg`).

## Verification Protocol
- **Disk Check**: `ls tma/images` should match the count in `INDEX.md`.
- **Manifest Check**: `manifest_v3.json` must contain all IDs from `INDEX.md`.
- **Live Test**: Verify that clicking 'Copy ID' triggers the clipboard and toast, and that images load without 404s.
