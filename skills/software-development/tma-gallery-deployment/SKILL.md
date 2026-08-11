---
name: tma-gallery-deployment
description: Use for TMA galleries with split Private/Public repos.
---

# TMA Gallery Deployment

Use this skill when setting up a visual reference gallery for a Telegram Mini App where the source data (YAML/Logic) must remain private, but the assets (Images/UI) must be public for hosting.

## Architecture Pattern
- **Private Repository**: Stores the "Source of Truth" (YAML tags, prompt logic, INDEX.md).
- **Public Repository**: Stores the "Distribution Layer" (Images folder, `manifest.json`, and the `/tma` folder containing `index.html`).
- **Hosting**: Vercel or GitHub Pages pointing to the public repository.

## Deployment Workflow

### 1. Initial Setup
- Create a Public Repository (e.g., `addstudio-gallery`).
- Create an `images/` folder for assets.
- Create a `tma/` folder for the frontend code.

### 2. Asset Synchronization
- Copy images from local/private storage to the public `images/` folder.
- Generate a `manifest.json` in the `tma/` folder (or root) that maps IDs to the public image paths.
- **CRITICAL**: Use absolute paths (e.g., `/images/R001.jpg`) in the manifest to ensure images load regardless of the HTML file's depth.

### 3. Vercel Configuration
- Connect the public repository to Vercel.
- Set the **Root Directory** to `tma` (if the HTML is inside that folder).
- Ensure the `images/` folder is accessible from the root of the deployed domain.

## User Experience (UX) Lessons
- **Avoid Modals**: For fast selection, place "Copy ID" buttons directly under the images in the grid.
- **Clipboard over sendData**: Use the Clipboard API (`document.execCommand('copy')`) instead of `tg.sendData` to ensure compatibility across Menu Buttons and Inline Buttons.
- **Visual Feedback**: Provide immediate visual confirmation (e.g., changing button text to "Copied!") when a reference ID is captured.

## Troubleshooting
- **404 on Images**: Occurs when relative paths (e.g., `images/...`) are used inside a subfolder like `/tma`. **Fix**: Use absolute paths starting with `/`.
- **Vercel Root Errors**: If the Root Directory is set to `tma`, Vercel ignores files outside that folder. **Fix**: Either move everything to the root or use absolute paths and ensure assets are included in the build.
