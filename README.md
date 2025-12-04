# Steadfast Digital

A quiet manifesto.

## Running on iPhone

### Option 1: Local Server (Recommended for Testing)

1. Unzip this folder on your Mac
2. Open Terminal and navigate to the folder:
   ```
   cd ~/Downloads/steadfast-pwa
   ```
3. Run the server:
   ```
   python3 serve.py
   ```
4. On your iPhone (same WiFi network), open Safari and go to the Network URL shown in Terminal
5. Tap **Share → Add to Home Screen** to install as an app

### Option 2: Host Online (For Permanent Use)

Upload the contents to any static host:

- **GitHub Pages**: Free, push to a repo and enable Pages
- **Netlify**: Drag and drop the folder at netlify.com/drop
- **Vercel**: Similar drag-and-drop deploy
- **Your own server**: Just serve the files

Then visit the URL on your iPhone and add to Home Screen.

## What's Included

- `index.html` — The page itself
- `manifest.json` — PWA configuration
- `sw.js` — Service worker for offline support
- `icon-192.png` / `icon-512.png` — App icons
- `serve.py` — Simple local server

## Features

- Works offline once loaded
- Respects light/dark mode
- Gyroscope-responsive paper texture on mobile
- Subtle haptic feedback on section reveals
- Time-of-day aware color temperature
- Proper safe area handling for notched devices

---

*"The people who need to find this will find it."*
