#!/usr/bin/env python3
"""
Simple server to test Steadfast Digital PWA locally.

Usage:
  1. Unzip steadfast-pwa.zip
  2. cd into the folder
  3. Run: python3 serve.py
  4. Open http://localhost:8000 on your computer
  5. Or find your Mac's IP and open http://YOUR_IP:8000 on iPhone
     (Both devices must be on same WiFi network)
"""

import http.server
import socketserver
import os
import socket

PORT = 8000

# Get local IP for convenience
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

Handler = http.server.SimpleHTTPRequestHandler

# Add proper MIME types
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.png': 'image/png',
    '.html': 'text/html',
})

print(f"""
╔═══════════════════════════════════════════════════════════╗
║                   Steadfast Digital                       ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Server running at:                                       ║
║                                                           ║
║    Local:   http://localhost:{PORT}                        ║
║    Network: http://{get_local_ip()}:{PORT}                     ║
║                                                           ║
║  On iPhone:                                               ║
║    1. Connect to same WiFi as this computer               ║
║    2. Open Safari and go to the Network URL above         ║
║    3. Tap Share → Add to Home Screen                      ║
║                                                           ║
║  Press Ctrl+C to stop                                     ║
╚═══════════════════════════════════════════════════════════╝
""")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
