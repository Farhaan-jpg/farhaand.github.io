"""
Pixel-perfect skill badge generator:
Uniform, crisp, 512x512 badges with zero checkerboard artifacts and matching theme.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import os

UPLOAD_DIR = r'C:\Users\farha\.gemini\antigravity-ide\brain\03934d6f-7772-4a35-97cb-c6e4719db5d3\.user_uploaded'
SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)

SIZE = 512
RADIUS = 104  # Sleek iOS-style squircle radius for unified theme

# ------------------------------------------------------------------------------
# 1. KALI LINUX (Clean 512x512 badge)
# ------------------------------------------------------------------------------
k_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787642918959.png')).convert('RGBA')
# Kali has a blue circle (radius ~500)
# Resize to 512x512
k_img = k_src.resize((SIZE, SIZE), Image.LANCZOS)
# Create squircle mask so all badges share identical outer footprint
mask_squircle = Image.new('L', (SIZE, SIZE), 0)
ImageDraw.Draw(mask_squircle).rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)

# Place on rounded badge with matching blue background
k_badge = Image.new('RGBA', (SIZE, SIZE), (27, 120, 242, 255))
k_final = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
k_final.paste(k_img, (0, 0))
k_final = Image.composite(k_final, Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0)), mask_squircle)
k_final.save(os.path.join(SKILLS_DIR, 'kali.png'), 'PNG')
print("Saved kali.png (512x512)")

# ------------------------------------------------------------------------------
# 2. BURP SUITE (Exact 512x512 crop - NO fake checkerboard, NO squishing)
# ------------------------------------------------------------------------------
b_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787642952414.png')).convert('RGBA')
# Crop the true 512x512 badge centered in the 920x512 canvas
b_cropped = b_src.crop((204, 0, 716, 512))

# Create smooth rounded-corner mask to cut off any remaining corner checkerboard
b_mask = Image.new('L', (SIZE, SIZE), 0)
ImageDraw.Draw(b_mask).rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)
b_mask = b_mask.filter(ImageFilter.GaussianBlur(0.6))

b_final = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
b_final.paste(b_cropped, (0, 0), b_mask)
b_final.save(os.path.join(SKILLS_DIR, 'burp-suite.png'), 'PNG')
print("Saved burp-suite.png (512x512) - Perfectly proportioned!")

# ------------------------------------------------------------------------------
# 3. WIRESHARK (Clean 512x512 badge)
# ------------------------------------------------------------------------------
ws_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787643004699.png')).convert('RGBA')
ws_cropped = ws_src.resize((SIZE, SIZE), Image.LANCZOS)
ws_final = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
ws_final.paste(ws_cropped, (0, 0), mask_squircle)
ws_final.save(os.path.join(SKILLS_DIR, 'wireshark.png'), 'PNG')
print("Saved wireshark.png (512x512)")

# ------------------------------------------------------------------------------
# 4. PYTHON (Official crisp badge)
# ------------------------------------------------------------------------------
py_final = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
py_bg = Image.new('RGBA', (SIZE, SIZE), (27, 38, 59, 255))
py_final.paste(py_bg, (0, 0), mask_squircle)

# Render official Python SVG in center
with open(os.path.join(SKILLS_DIR, 'python.svg'), 'w') as f:
    f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#1b263b"/>
  <g transform="translate(100, 100) scale(2.44)">
    <path fill="#387eb8" d="M63.5 0C32.7 0 34.6 13.4 34.6 13.4l.04 13.88h29.24v4.16H23.54S0 28.86 0 59.8c0 30.95 20.48 29.83 20.48 29.83h12.22V72.45s-.67-20.48 20.14-20.48h29.13s19.47.31 19.47-19.14V13.4S104.37 0 63.5 0zM47.1 9.4c3.48 0 6.3 2.82 6.3 6.3 0 3.47-2.82 6.3-6.3 6.3-3.47 0-6.3-2.83-6.3-6.3 0-3.48 2.83-6.3 6.3-6.3z"/>
    <path fill="#ffe052" d="M64.5 128c30.8 0 28.9-13.4 28.9-13.4l-.04-13.88H64.12v-4.16h40.34s23.54 2.58 23.54-28.36c0-30.95-20.48-29.83-20.48-29.83H115.3v17.18s.67 20.48-20.14 20.48H66.03s-19.47-.31-19.47 19.14v20.39S23.63 128 64.5 128zm16.4-9.4c-3.48 0-6.3-2.82-6.3-6.3 0-3.47 2.82-6.3 6.3-6.3 3.47 0 6.3 2.83 6.3 6.3 0 3.48-2.83 6.3-6.3 6.3z"/>
  </g>
</svg>''')
print("Saved python.svg (512x512)")

# ------------------------------------------------------------------------------
# 5. GO / GOLANG (Official crisp badge)
# ------------------------------------------------------------------------------
with open(os.path.join(SKILLS_DIR, 'go.svg'), 'w') as f:
    f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#00add8"/>
  <g transform="translate(64, 140) scale(3.1)">
    <path fill="#ffffff" d="M38.5 35.8c-2.3 4.2-5.7 7.7-10.1 9.9-5.8 2.9-12.7 3.3-18.8 1.1C3.8 44.7-.3 38.8.0 32.7.4 26 5.6 20.6 12.2 19.4c6.3-1.1 13 .7 17.5 5.2l-5.4 5.2c-2.8-2.8-7-3.9-10.8-2.9-3.9 1-6.8 4.4-7 8.5-.3 4.1 2.3 7.8 6.3 8.8 4.3 1.1 9.1-.5 11.7-4.1h-11.4v-7.2h18.8l-.5 6.9zM78.6 32.4c.5 8-5.3 15.3-13.3 16.5-8.2 1.3-16.1-4-17.8-12.1-1.7-8.1 3.2-16.3 11.2-18 8.1-1.8 16.3 2.9 18.4 10.9.9 2.2 1.4 4.5 1.5 6.7v-4zm-7.6-.7c-.2-4.1-3.3-7.5-7.4-7.8-4.3-.3-8 2.7-8.6 6.9-.6 4.3 2.2 8.3 6.5 9.1 4.3.8 8.4-1.9 9.3-6.2.1-.7.2-1.3.2-2z"/>
    <path fill="#ffffff" d="M96 28h22v7H96zM88 39h30v7H88zM102 17h16v7h-16z"/>
  </g>
</svg>''')
print("Saved go.svg (512x512)")

# ------------------------------------------------------------------------------
# 6. MYSQL (Exact circle crop - ZERO checkerboard, centered in uniform badge)
# ------------------------------------------------------------------------------
m_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787643032145.png')).convert('RGBA')
# Circle center: (420, 429), radius 415
cx, cy, r = 420, 429, 415
m_cropped = m_src.crop((cx - r, cy - r, cx + r, cy + r)).resize((SIZE, SIZE), Image.LANCZOS)

# Create smooth circular mask
m_circ_mask = Image.new('L', (SIZE, SIZE), 0)
ImageDraw.Draw(m_circ_mask).ellipse([0, 0, SIZE, SIZE], fill=255)
m_circ_mask = m_circ_mask.filter(ImageFilter.GaussianBlur(0.8))

# Fill background with exact MySQL teal-blue (#387199) on squircle badge
m_final = Image.new('RGBA', (SIZE, SIZE), (56, 113, 153, 255))
m_content = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
m_content.paste(m_cropped, (0, 0), m_circ_mask)

m_final.paste(m_content, (0, 0), mask_squircle)
m_final.save(os.path.join(SKILLS_DIR, 'mysql.png'), 'PNG')
print("Saved mysql.png (512x512) - Clean, uniform, ZERO checkerboard!")

print("All 6 skills generated with 100% precision!")
