# Reference Archive — Telegram Mini App

A dark, editorial "archive plate" gallery for browsing product-photography
references (R001, R002…) inside Telegram, with search, mood/brand filtering,
a full-screen detail view, one-tap **Copy ID** (with a bottom toast
confirmation), and a Select action that sends the chosen reference ID back
to your bot.

## Files

- `index.html` — the whole app (HTML + CSS + JS, no build step)
- `manifest.json` — generated data (91 real references, see below)
- `references/` — the original per-photo `.yaml` tag files (source of truth)
- `moods.yaml` — the closed set of mood slugs used for the top filter chips
- `mood-guide.md` — the algorithm an agent follows to derive `mood` from a
  reference's yaml tags
- `build/build_manifest.py` — regenerates `manifest.json` from `references/*.yaml`

## 1. Replace the sample image URLs

`manifest.json` was generated from your real `references/*.yaml` tag files,
so `id`, `brand`, `category`, `mood`, and `style` are already correct.
The only placeholder left is `url` — it currently points at picsum.photos
so you can preview the layout. Each entry looks like:

```json
{ "id": "R083", "url": "https://your-cdn.com/references/R083.jpg", "brand": "KORFF", "category": "skincare", "mood": "luxury-premium", "style": "Vitamin C Serum" }
```

Swap `url` for your real hosted HTTPS image (Telegram requires HTTPS
everywhere) — either by hand, or by editing `placeholder_url()` in
`build/build_manifest.py` and re-running it:

```bash
cd build
python3 build_manifest.py
```

## Mood tagging pipeline

- `moods.yaml` defines 9 fixed mood slugs (8 real moods + `unknown` as an
  honest fallback) — don't add new slugs without updating this file, the
  JS `MOOD_TAXONOMY` mirror in `index.html`, and `mood-guide.md` together.
- `mood-guide.md` documents exactly how a mood is derived from a reference's
  `mood` / `style` / `concept_idea` fields (keyword scoring, tie-break order,
  confidence, fallback to `unknown`).
- Re-running `build/build_manifest.py` after adding/editing files in
  `references/` regenerates both `manifest.json` and `mood_report.json`
  (a list of any reference whose mood needs manual review — currently 10
  references with `needs_review: true` because their yaml had no usable
  mood/style text; see the printed list after running the script).

## 2. Host it over HTTPS

Telegram Mini Apps must be served over HTTPS from a public URL — `file://`
won't work (the browser blocks `fetch('manifest.json')` from local files).
Easiest free options:

- **GitHub Pages**: push this folder to a repo, enable Pages on the `main`
  branch, you'll get a URL like `https://yourname.github.io/tma-gallery/`
- **Vercel / Netlify**: drag-and-drop the folder in their dashboard for an
  instant HTTPS URL
- **Cloudflare Pages**: same idea, also free

To test locally before deploying, run a local server (plain `file://`
won't allow the JSON fetch):

```bash
cd tma-gallery
python3 -m http.server 8000
# open http://localhost:8000
```

(Telegram-specific bits like `sendData` won't fire outside Telegram — the
app shows a browser-preview `alert()` fallback instead so you can still
click through the UI.)

## 3. Connect it to your bot via BotFather

1. Open a chat with **@BotFather** in Telegram.
2. If you don't have a bot yet: `/newbot` and follow the prompts.
3. Attach the Mini App:
   - Send `/newapp`
   - Choose your bot
   - Give it a title, description, and icon (640×360 for the app photo)
   - When asked for the **Web App URL**, paste your hosted HTTPS URL
     (e.g. `https://yourname.github.io/tma-gallery/`)
4. To open it from inside the bot, either:
   - Set it as the bot's **Menu Button**: `/mybots` → your bot →
     *Bot Settings* → *Menu Button* → paste the same URL, or
   - Send a message with an inline **Web App button** from your bot's
     backend (see below).

## 4. Receive the selected reference in your bot

When the user taps **Select this Reference**, the app calls
`Telegram.WebApp.sendData(id)` and closes. Your bot receives this as a
`web_app_data` update. Example (python-telegram-bot style):

```python
async def on_web_app_data(update, context):
    reference_id = update.effective_message.web_app_data.data  # e.g. "R083"
    await update.message.reply_text(f"Reference {reference_id} selected.")
```

To open the app from a message with an inline button:

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

keyboard = InlineKeyboardMarkup([[
    InlineKeyboardButton("Browse references", web_app=WebAppInfo(url="https://yourname.github.io/tma-gallery/"))
]])
```

## Notes

- **Copy ID**: every plate has a small copy icon (top-right corner), and the
  detail sheet has a "Copy ID" button next to the reference number. Both use
  the Clipboard API with a `document.execCommand('copy')` fallback for older
  in-app browsers, and show a bottom toast ("Copied R083") for ~1.6s.
- **Mood filter chips**: the top row is built from `moods.yaml` — only moods
  actually present in `manifest.json` are shown, each chip using its own
  accent color when active. Brand chips remain as a secondary filter after
  the separator.
- Images lazy-load via `IntersectionObserver`, with a shimmer skeleton
  shown until each one decodes.
- The masonry grid uses CSS columns (2 on phones, 3 from ~480px up) — no
  JS layout library needed.
- Header/background colors are set to match the app's dark theme via
  `Telegram.WebApp.setHeaderColor` / `setBackgroundColor`.
- The in-app Telegram **Back button** is wired to close the detail sheet
  when it's open.
