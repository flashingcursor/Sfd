# Steadfast Digital

A quiet manifesto.

## Deploy to GitHub Pages

### Step 1: Create Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it `steadfastdigital.io` (or any name you like)
3. Keep it **Public** (required for free GitHub Pages)
4. Click **Create repository**

### Step 2: Upload Files

**Option A: Upload via GitHub.com**

1. In your new empty repo, click **"uploading an existing file"**
2. Drag all 5 files from this folder:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `icon-192.png`
   - `icon-512.png`
3. Click **Commit changes**

**Option B: Use Git**

```bash
cd steadfast-github
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repo's **Settings** tab
2. Click **Pages** in the left sidebar
3. Under "Source", select **Deploy from a branch**
4. Select **main** branch and **/ (root)** folder
5. Click **Save**

### Step 4: Wait & Visit

- GitHub will build your site (1-2 minutes)
- Your site will be live at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`
- If you named the repo `YOUR_USERNAME.github.io`, it'll be at: `https://YOUR_USERNAME.github.io/`

### Step 5: Add to iPhone

1. Open the URL in Safari on your iPhone
2. Tap **Share → Add to Home Screen**
3. Done—it works offline now

---

## Custom Domain (Optional)

If you own `steadfastdigital.io`:

1. In repo **Settings → Pages**, enter your custom domain
2. Add these DNS records at your registrar:
   - **A records** pointing to GitHub's IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - **CNAME** for `www`: `YOUR_USERNAME.github.io`
3. Check "Enforce HTTPS" once DNS propagates

---

## Features

- Works offline once loaded
- Respects light/dark mode
- Gyroscope-responsive paper texture on mobile
- Subtle haptic feedback on section reveals
- Time-of-day aware color temperature
- Proper safe area handling for notched devices

### Experimental Effects

- **Breathing** — The page has an imperceptible brightness oscillation on a 12-second cycle, as if the document is alive
- **Ink pooling** — Text darkens letter by letter where your cursor rests, as if ink is pooling where attention gathers
- **Ambient particles** — Occasionally, a single letter-shaped particle drifts off the page and dissolves into nothing
- **Gravitational tilt** — Text subtly shifts toward your cursor position, as if attracted to attention

---

*"The people who need to find this will find it."*
