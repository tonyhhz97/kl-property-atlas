# KL Projects Atlas — source files

This folder has everything needed to rebuild `index.html` (the KL Projects
Atlas landing page) on your own computer, and to push it to GitHub so
Netlify can auto-deploy on every change.

## What's in here

- `build.py` — generates `index.html` from the template + data below.
- `projects_embed.json` — offline fallback project data (used only if a
  visitor's browser can't reach the live Google Sheet).
- `*.b64` — base64-encoded images baked into the page (logo, your profile
  photo, the About/Hero background photos, testimonial photos).

## Rebuilding locally

Requires Python 3 (no extra packages needed).

```
python3 build.py
```

This writes `index.html` into this same folder. Open it in a browser to
check it, then it's ready to deploy.

## One-time GitHub + Netlify setup

1. Create a new repo on GitHub (e.g. `kl-property-atlas`).
2. From this folder, run:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/kl-property-atlas.git
   git push -u origin main
   ```
3. In Netlify: Site configuration → Build & deploy → Link repository (or
   "Import from Git" for a brand new site) → pick this repo → authorize.
4. Build settings:
   - **Build command:** `python3 build.py`
   - **Publish directory:** `.` (this same folder, since `index.html` is
     written right here)

After that, every `git push` triggers a fresh Netlify deploy automatically.

## Going forward

Any time Claude helps you make a change to `build.py`, come back to this
folder, `git add . && git commit -m "..." && git push`, and Netlify will
pick it up — no manual drag-and-drop needed anymore.
