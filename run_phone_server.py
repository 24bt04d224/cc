# -*- coding: utf-8 -*-
import http.server
import socket
import socketserver
import webbrowser
import os

PORT = 8000

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

local_ip = get_local_ip()
phone_url = f"http://{local_ip}:{PORT}"

# Create a small, elegant QR helper page
qr_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Connect Phone - Cloud Computing Portal</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0b0f19;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
      text-align: center;
    }}
    .card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 30px;
      max-width: 480px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}
    h1 {{
      font-size: 1.5rem;
      margin-bottom: 8px;
      color: #38bdf8;
    }}
    p {{
      color: #94a3b8;
      font-size: 0.95rem;
      line-height: 1.5;
    }}
    .qr-container {{
      background: white;
      padding: 16px;
      border-radius: 12px;
      display: inline-block;
      margin: 20px 0;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .qr-container img {{
      display: block;
      width: 220px;
      height: 220px;
    }}
    .url-badge {{
      display: inline-block;
      background: #0f172a;
      border: 1px solid #0284c7;
      color: #38bdf8;
      font-size: 1.15rem;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: 8px;
      letter-spacing: 0.5px;
      margin-top: 10px;
      user-select: all;
    }}
    .step {{
      background: #0f172a;
      border-left: 3px solid #10b981;
      text-align: left;
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      margin: 12px 0;
      font-size: 0.88rem;
    }}
    .step strong {{ color: #f8fafc; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>📱 Scan to Open on Your Phone</h1>
    <p>Point your phone camera at the QR code below to open the study portal instantly.</p>
    
    <div class="qr-container">
      <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&data={phone_url}" alt="QR Code">
    </div>

    <div>Or type this directly into your phone's browser:</div>
    <div class="url-badge">{phone_url}</div>

    <div style="margin-top: 25px; text-align: left;">
      <div class="step">
        <strong>Step 1:</strong> Ensure your phone and laptop are on the <strong>same Wi-Fi network</strong> or Mobile Hotspot.
      </div>
      <div class="step">
        <strong>Step 2:</strong> Scan the QR code or type the link into Chrome/Safari on your phone.
      </div>
      <div class="step">
        <strong>Step 3:</strong> Keep this terminal window open on your laptop while studying on your phone.
      </div>
    </div>
  </div>
</body>
</html>
"""

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("phone_qr.html", "w", encoding="utf-8") as f:
    f.write(qr_html)

print("=" * 65)
print("  📱 CLOUD COMPUTING STUDY PORTAL — WIRELESS PHONE ACCESS")
print("=" * 65)
print()
print(f"  👉 Phone URL:   {phone_url}")
print(f"  👉 Active IP:   {local_ip}")
print(f"  👉 Server Port: {PORT}")
print()
print("  INSTRUCTIONS:")
print("  1. Make sure your Phone & Laptop are on the SAME Wi-Fi / Hotspot.")
print("  2. A QR Code scanner window is opening on your laptop screen.")
print("  3. Scan the QR code with your phone camera (or type the URL into Chrome/Safari).")
print()
print("  [Press Ctrl + C in this window to stop the server when done]")
print("=" * 65)

# Open QR code helper in laptop browser
webbrowser.open(os.path.abspath("phone_qr.html"))

Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
