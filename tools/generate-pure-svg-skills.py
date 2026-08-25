"""
Pristine high-fidelity vector SVGs for Skills:
1. Kali Linux (Official sharp dragon on deep blue)
2. Burp Suite (Official PortSwigger split dark/orange with lightning bolt)
3. Wireshark (Official shark fin waveform on vibrant blue)
4. Python (Official dual snake on dark navy)
5. Go (Golang) (Official Gopher speed branding on cyan)
6. MySQL (Official dolphin + MySQL typography on deep blue)
"""
import os

SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)
RADIUS = 112

# 1. KALI LINUX (Official sharp dragon on blue squircle)
kali_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="kali-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2885e5"/>
      <stop offset="100%" stop-color="#1460ad"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="{RADIUS}" fill="url(#kali-bg)"/>
  <g transform="translate(64, 60) scale(3.0)">
    <!-- Main Dragon Body and Wings in Crisp White -->
    <path fill="#ffffff" d="M118.5 18.2C104.1 8.8 86.8 3.5 68.2 3.5 32.4 3.5 3.5 32.4 3.5 68.2c0 23.8 12.8 44.6 32 55.8 4.2-7.5 9.1-14.7 14.6-21.5-11.2-8.2-18.5-21.6-18.5-36.6 0-24.8 20.1-44.9 44.9-44.9 14.9 0 28.1 7.2 36.3 18.3 5.4-3.8 10.3-6.9 15.7-10.4z"/>
    <path fill="#ffffff" d="M124.5 42.8c-12.8 9.5-24.8 18.4-36.3 28.6 3.1 6.8 4.8 14.4 4.8 22.3 0 28.6-23.2 51.8-51.8 51.8-8.2 0-16-1.9-22.9-5.3 12.9 8.2 28.3 13 44.8 13 44.7 0 81-36.3 81-81 0-10.5-2-20.5-5.6-29.4h-14z"/>
    <path fill="#e2eeff" d="M96.4 53.6c-4.9-6.3-12.4-10.4-20.9-10.4-14.6 0-26.4 11.8-26.4 26.4 0 7.8 3.4 14.8 8.8 19.6 4.8-5.7 10.1-11.2 15.8-16.3 7.8-6.9 15.6-13.4 22.7-19.3z"/>
    <circle cx="82" cy="48" r="3.5" fill="#1460ad"/>
  </g>
</svg>'''

# 2. BURP SUITE (Official PortSwigger lightning divider: dark grey #333333 left, orange #ff6633 right)
burp_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <clipPath id="burp-clip">
      <rect width="512" height="512" rx="{RADIUS}" />
    </clipPath>
  </defs>
  <g clip-path="url(#burp-clip)">
    <!-- Base Left Dark, Right Orange -->
    <rect x="0" y="0" width="256" height="512" fill="#2e2e2e"/>
    <rect x="256" y="0" width="256" height="512" fill="#ff6633"/>
    
    <!-- Lightning divider profiles -->
    <path fill="#2e2e2e" d="M256,0 L256,170 L196,195 L256,195 L256,335 L196,335 L256,435 L256,512 L0,512 L0,0 Z"/>
    <path fill="#ff6633" d="M256,0 L256,170 L196,195 L256,195 L256,335 L196,335 L256,435 L256,512 L512,512 L512,0 Z"/>
    
    <!-- Crisp White Interlocking Ribbon -->
    <polyline points="256,0 256,170 196,195 256,195 256,335 196,335 256,435 256,512" 
              fill="none" stroke="#ffffff" stroke-width="22" stroke-linecap="square" stroke-linejoin="miter"/>
  </g>
</svg>'''

# 3. WIRESHARK (Official shark fin on blue squircle)
wireshark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="ws-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#218de8"/>
      <stop offset="100%" stop-color="#0c5caa"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="{RADIUS}" fill="url(#ws-bg)"/>
  <g transform="translate(64, 88) scale(3.0)">
    <!-- White Shark Fin + Waveform Line -->
    <path fill="#ffffff" d="M8 82c32-2 56-18 72-42 4 18 16 52 56 54-32 20-82 22-128-12z"/>
    <!-- Blue Interior Depth -->
    <path fill="#0c5caa" d="M22 80c26-2 46-14 59-33 3 14 11 40 43 43-24 15-64 17-102-10z"/>
  </g>
</svg>'''

# 4. PYTHON (Official Python dual snake)
python_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#1b263b"/>
  <g transform="translate(100, 100) scale(2.44)">
    <path fill="#387eb8" d="M63.5 0C32.7 0 34.6 13.4 34.6 13.4l.04 13.88h29.24v4.16H23.54S0 28.86 0 59.8c0 30.95 20.48 29.83 20.48 29.83h12.22V72.45s-.67-20.48 20.14-20.48h29.13s19.47.31 19.47-19.14V13.4S104.37 0 63.5 0zM47.1 9.4c3.48 0 6.3 2.82 6.3 6.3 0 3.47-2.82 6.3-6.3 6.3-3.47 0-6.3-2.83-6.3-6.3 0-3.48 2.83-6.3 6.3-6.3z"/>
    <path fill="#ffe052" d="M64.5 128c30.8 0 28.9-13.4 28.9-13.4l-.04-13.88H64.12v-4.16h40.34s23.54 2.58 23.54-28.36c0-30.95-20.48-29.83-20.48-29.83H115.3v17.18s.67 20.48-20.14 20.48H66.03s-19.47-.31-19.47 19.14v20.39S23.63 128 64.5 128zm16.4-9.4c-3.48 0-6.3-2.82-6.3-6.3 0-3.47 2.82-6.3 6.3-6.3 3.47 0 6.3 2.83 6.3 6.3 0 3.48-2.83 6.3-6.3 6.3z"/>
  </g>
</svg>'''

# 5. GO (GOLANG) (Official Cyan Gopher speed logo)
go_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#00add8"/>
  <g transform="translate(64, 140) scale(3.1)">
    <path fill="#ffffff" d="M38.5 35.8c-2.3 4.2-5.7 7.7-10.1 9.9-5.8 2.9-12.7 3.3-18.8 1.1C3.8 44.7-.3 38.8.0 32.7.4 26 5.6 20.6 12.2 19.4c6.3-1.1 13 .7 17.5 5.2l-5.4 5.2c-2.8-2.8-7-3.9-10.8-2.9-3.9 1-6.8 4.4-7 8.5-.3 4.1 2.3 7.8 6.3 8.8 4.3 1.1 9.1-.5 11.7-4.1h-11.4v-7.2h18.8l-.5 6.9zM78.6 32.4c.5 8-5.3 15.3-13.3 16.5-8.2 1.3-16.1-4-17.8-12.1-1.7-8.1 3.2-16.3 11.2-18 8.1-1.8 16.3 2.9 18.4 10.9.9 2.2 1.4 4.5 1.5 6.7v-4zm-7.6-.7c-.2-4.1-3.3-7.5-7.4-7.8-4.3-.3-8 2.7-8.6 6.9-.6 4.3 2.2 8.3 6.5 9.1 4.3.8 8.4-1.9 9.3-6.2.1-.7.2-1.3.2-2z"/>
    <path fill="#ffffff" d="M96 28h22v7H96zM88 39h30v7H88zM102 17h16v7h-16z"/>
  </g>
</svg>'''

# 6. MYSQL (Official deep blue squircle + jumping dolphin + "MySQL" typography)
mysql_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="mysql-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#387199"/>
      <stop offset="100%" stop-color="#225375"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="{RADIUS}" fill="url(#mysql-bg)"/>
  
  <!-- Jumping Dolphin in White -->
  <g transform="translate(300, 100) scale(1.65)">
    <path fill="#ffffff" d="M78 88c-1.5-4-4.5-9.5-9-13.5-4.5-4-9.5-6-15-5.8-11.2.2-18.6 8.5-20.8 11.2-4.1-3.1-9.3-5.2-15-5.8-14.5-1.3-27.3 7.6-28.5 19.9-1.2 12.3 9.7 23.3 24.2 24.6 5.5.5 10.7-.5 15.2-2.7 3.4 4.7 8.6 8.5 15.3 10.5 12.7 3.7 25.6-1.6 28.8-12.1 3.2-10.5-4.5-22-17.2-25.7-3.3-1-6.6-1.3-9.9-1 2.3-3.8 6.5-7.2 11.9-7.2 3.3 0 6.2 1.1 8.8 3.5 2.6 2.4 4.3 5.8 5.4 8.8l7.8-5.5z"/>
  </g>

  <!-- "My" (White) + "SQL" (Golden Orange) -->
  <g transform="translate(68, 385)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="122" font-weight="900" letter-spacing="-1">
      <tspan fill="#ffffff">My</tspan><tspan fill="#e48e00">SQL</tspan>
    </text>
  </g>
</svg>'''

files = {
    'kali.svg': kali_svg,
    'burp-suite.svg': burp_svg,
    'wireshark.svg': wireshark_svg,
    'python.svg': python_svg,
    'go.svg': go_svg,
    'mysql.svg': mysql_svg,
}

for filename, content in files.items():
    path = os.path.join(SKILLS_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Generated {path}")

print("All 6 pure SVG logos created successfully!")
