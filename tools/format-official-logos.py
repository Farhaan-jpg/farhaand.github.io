import os

SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)

# 1. Kali Linux Official Dragon Logo
kali_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#0d1117"/>
  <path fill="#2777c5" d="M88.5 24.2c-3.1 1.2-6.5 2.1-9.9 2.6 1.8-1.5 3.3-3.4 4.3-5.6-2.9 1.7-6.1 2.9-9.5 3.6-2.7-2.9-6.6-4.7-10.9-4.7-8.3 0-15 6.7-15 15 0 1.2.1 2.3.4 3.4-12.5-.6-23.5-6.6-30.9-15.7-1.3 2.2-2 4.8-2 7.5 0 5.2 2.6 9.8 6.6 12.5-2.5-.1-4.8-.8-6.8-1.9v.2c0 7.3 5.2 13.3 12.1 14.7-1.3.4-2.6.5-4 .5-1 0-1.9-.1-2.9-.3 1.9 6 7.5 10.3 14.1 10.4-5.2 4.1-11.7 6.5-18.8 6.5-1.2 0-2.4-.1-3.6-.2 6.7 4.3 14.7 6.8 23.2 6.8 27.9 0 43.1-23.1 43.1-43.1v-2c3-2.1 5.5-4.8 7.6-7.9z" opacity="0"/>
  <path fill="#2a82da" d="M22 64c0-23.2 18.8-42 42-42 9.5 0 18.2 3.2 25.2 8.5l-6.2 6.2C77.4 32.3 71 30 64 30c-18.8 0-34 15.2-34 34s15.2 34 34 34c14.2 0 26.3-8.7 31.4-21H64V65h42c.6 3 1 6.1 1 9.4 0 23.2-18.8 42-42 42C40.8 116 22 97.2 22 74v-10z" opacity="0"/>
  <g transform="translate(18, 18) scale(0.72)">
    <path fill="#2f7fd3" d="M118.5 18.2C104.1 8.8 86.8 3.5 68.2 3.5 32.4 3.5 3.5 32.4 3.5 68.2c0 23.8 12.8 44.6 32 55.8 4.2-7.5 9.1-14.7 14.6-21.5-11.2-8.2-18.5-21.6-18.5-36.6 0-24.8 20.1-44.9 44.9-44.9 14.9 0 28.1 7.2 36.3 18.3 5.4-3.8 10.3-6.9 15.7-10.4z"/>
    <path fill="#55a5f5" d="M124.5 42.8c-12.8 9.5-24.8 18.4-36.3 28.6 3.1 6.8 4.8 14.4 4.8 22.3 0 28.6-23.2 51.8-51.8 51.8-8.2 0-16-1.9-22.9-5.3 12.9 8.2 28.3 13 44.8 13 44.7 0 81-36.3 81-81 0-10.5-2-20.5-5.6-29.4h-14z"/>
    <path fill="#ffffff" d="M96.4 53.6c-4.9-6.3-12.4-10.4-20.9-10.4-14.6 0-26.4 11.8-26.4 26.4 0 7.8 3.4 14.8 8.8 19.6 4.8-5.7 10.1-11.2 15.8-16.3 7.8-6.9 15.6-13.4 22.7-19.3z"/>
    <circle cx="82" cy="48" r="3.5" fill="#111827"/>
  </g>
</svg>'''

# 2. Burp Suite Official Flame/Hexagon Logo
burp_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#ff6633"/>
  <g transform="translate(24, 20) scale(0.625)">
    <path fill="#ffffff" d="M64 0L8 28v72l56 28 56-28V28L64 0zm0 18l40 20v52L64 110 24 90V38L64 18z"/>
    <path fill="#ffffff" d="M48 38h32v12H62l18 18v6H48v-12h18L48 44V38z"/>
    <path fill="#ffffff" d="M48 80h32v12H48z"/>
  </g>
</svg>'''

# 3. Wireshark Official Shark Fin Logo
wireshark_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#0d529c"/>
  <g transform="translate(18, 22) scale(0.72)">
    <path fill="#ffffff" d="M12 76c24-1 46-12 60-32 3 14 12 42 44 44-24 16-64 18-104-12z"/>
    <path fill="#0d529c" d="M24 74c20-2 38-11 50-26 2 11 9 32 34 35-18 12-50 14-84-9z"/>
  </g>
</svg>'''

# 4. Python Official Dual Snake Logo
python_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#1e293b"/>
  <g transform="translate(20, 20) scale(0.6875)">
    <path fill="#387eb8" d="M63.5 0C32.7 0 34.6 13.4 34.6 13.4l.04 13.88h29.24v4.16H23.54S0 28.86 0 59.8c0 30.95 20.48 29.83 20.48 29.83h12.22V72.45s-.67-20.48 20.14-20.48h29.13s19.47.31 19.47-19.14V13.4S104.37 0 63.5 0zM47.1 9.4c3.48 0 6.3 2.82 6.3 6.3 0 3.47-2.82 6.3-6.3 6.3-3.47 0-6.3-2.83-6.3-6.3 0-3.48 2.83-6.3 6.3-6.3z"/>
    <path fill="#ffe052" d="M64.5 128c30.8 0 28.9-13.4 28.9-13.4l-.04-13.88H64.12v-4.16h40.34s23.54 2.58 23.54-28.36c0-30.95-20.48-29.83-20.48-29.83H115.3v17.18s.67 20.48-20.14 20.48H66.03s-19.47-.31-19.47 19.14v20.39S23.63 128 64.5 128zm16.4-9.4c-3.48 0-6.3-2.82-6.3-6.3 0-3.47 2.82-6.3 6.3-6.3 3.47 0 6.3 2.83 6.3 6.3 0 3.48-2.83 6.3-6.3 6.3z"/>
  </g>
</svg>'''

# 5. Go (Golang) Official Logo
go_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#00add8"/>
  <g transform="translate(14, 34) scale(0.78)">
    <path fill="#ffffff" d="M38.5 35.8c-2.3 4.2-5.7 7.7-10.1 9.9-5.8 2.9-12.7 3.3-18.8 1.1C3.8 44.7-.3 38.8.0 32.7.4 26 5.6 20.6 12.2 19.4c6.3-1.1 13 .7 17.5 5.2l-5.4 5.2c-2.8-2.8-7-3.9-10.8-2.9-3.9 1-6.8 4.4-7 8.5-.3 4.1 2.3 7.8 6.3 8.8 4.3 1.1 9.1-.5 11.7-4.1h-11.4v-7.2h18.8l-.5 6.9zM78.6 32.4c.5 8-5.3 15.3-13.3 16.5-8.2 1.3-16.1-4-17.8-12.1-1.7-8.1 3.2-16.3 11.2-18 8.1-1.8 16.3 2.9 18.4 10.9.9 2.2 1.4 4.5 1.5 6.7v-4zm-7.6-.7c-.2-4.1-3.3-7.5-7.4-7.8-4.3-.3-8 2.7-8.6 6.9-.6 4.3 2.2 8.3 6.5 9.1 4.3.8 8.4-1.9 9.3-6.2.1-.7.2-1.3.2-2z"/>
    <path fill="#ffffff" d="M96 28h22v7H96zM88 39h30v7H88zM102 17h16v7h-16z"/>
  </g>
</svg>'''

# 6. MySQL Official Dolphin Logo
mysql_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128">
  <rect width="128" height="128" rx="28" fill="#00618a"/>
  <g transform="translate(18, 16) scale(0.72)">
    <!-- Dolphin Body in Orange & White -->
    <path fill="#e48e00" d="M102.5 38.8c-1.4-3.7-4-8.8-8.2-12.6-4.1-3.7-8.7-5.5-13.8-5.4-10.3.2-17.1 7.8-19.2 10.2-3.8-2.9-8.5-4.8-13.7-5.3-13.4-1.2-25.1 7-26.2 18.3-1.1 11.3 8.9 21.4 22.3 22.6 5 .4 9.8-.5 14-2.4 3.1 4.3 7.9 7.8 14 9.6 11.7 3.4 23.5-1.5 26.5-11.1 3-9.6-4.1-20.1-15.8-23.6-3-.9-6.1-1.2-9.1-.9 2.1-3.5 5.9-6.6 10.9-6.6 3 0 5.7 1 8.1 3.2 2.4 2.2 4 5.3 5 8.1l7.2-5.1z"/>
    <!-- MySQL Crisp Text -->
    <text x="6" y="106" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="28" letter-spacing="1">MySQL</text>
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
    print(f"Written {path}")

print("All 6 official skill SVGs updated!")
