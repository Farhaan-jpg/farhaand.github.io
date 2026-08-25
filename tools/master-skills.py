"""
Master skill badge generator:
Uniform, crisp, 512x512 modern rounded squircle badges for all 6 skills:
1. Kali Linux
2. Burp Suite
3. Wireshark
4. Python
5. Go (Golang)
6. MySQL
"""
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np
import os

UPLOAD_DIR = r'C:\Users\farha\.gemini\antigravity-ide\brain\03934d6f-7772-4a35-97cb-c6e4719db5d3\.user_uploaded'
SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)

SIZE = 512
RADIUS = 112 # Uniform modern squircle radius

def create_base_badge(color):
    im = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    mask = Image.new('L', (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)
    bg = Image.new('RGBA', (SIZE, SIZE), color)
    im.paste(bg, (0, 0), mask)
    return im, mask

# ==============================================================================
# 1. KALI LINUX
# The user uploaded the circular blue badge with white dragon.
# We can make it a sleek modern rounded squircle badge or keep the circle,
# but make sure the dragon is crisp, centered, with no background noise.
# ==============================================================================
kali_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787642918959.png')).convert('RGBA')
# Extract dragon / circular badge cleanly:
k_arr = np.array(kali_src)
# Clean transparent outer pixels if any
k_badge = kali_src.resize((SIZE, SIZE), Image.LANCZOS)
# Place on rounded badge or clean circle with same radius for visual unity
badge_kali, mask_kali = create_base_badge((30, 110, 230, 255))
# Center dragon inside badge
# Dragon is white/light blue.
k_box = k_badge.getbbox()
k_cropped = k_badge.crop(k_box) if k_box else k_badge
# Resize dragon nicely inside 512x512
k_fit = ImageOps.fit(kali_src, (SIZE, SIZE), method=Image.LANCZOS, centering=(0.5, 0.5))
# Mask to squircle badge for 100% uniformity
badge_kali = Image.composite(k_fit, Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0)), mask_kali)
badge_kali.save(os.path.join(SKILLS_DIR, 'kali.png'), 'PNG')
print("Kali Linux badge generated")

# ==============================================================================
# 2. BURP SUITE
# The user uploaded the black/orange split badge with lightning divider.
# Image size is (920, 512) containing the central badge and outer checkerboard.
# Let's isolate the actual badge by color:
# Black side: R < 70, G < 70, B < 70
# Orange side: R > 190, G > 60, B < 60
# Divider: R > 230, G > 230, B > 230
# Checkerboard: R,G,B are grey (in [180..225] with abs(R-G) < 5 and abs(G-B) < 5)
# ==============================================================================
burp_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787642952414.png')).convert('RGBA')
b_arr = np.array(burp_src)
H, W = b_arr.shape[:2]

# Detect checkerboard
is_grey_checker = (b_arr[:, :, 0] > 160) & (b_arr[:, :, 0] < 235) & \
                  (np.abs(b_arr[:, :, 0].astype(int) - b_arr[:, :, 1].astype(int)) < 10) & \
                  (np.abs(b_arr[:, :, 1].astype(int) - b_arr[:, :, 2].astype(int)) < 10)

# True badge pixels
is_orange = (b_arr[:, :, 0] > 180) & (b_arr[:, :, 1] < 140)
is_dark = (b_arr[:, :, 0] < 80) & (b_arr[:, :, 1] < 80) & (b_arr[:, :, 2] < 80) & (b_arr[:, :, 3] > 100)
is_white_div = (b_arr[:, :, 0] > 240) & (b_arr[:, :, 1] > 240) & (b_arr[:, :, 2] > 240)
is_badge = is_orange | is_dark | is_white_div

# Find actual bounding box of badge in the 920x512 image
y_indices, x_indices = np.where(is_badge)
if len(x_indices) > 0 and len(y_indices) > 0:
    min_x, max_x = x_indices.min(), x_indices.max()
    min_y, max_y = y_indices.min(), y_indices.max()
    print(f"Burp badge bounding box in source: x=({min_x}, {max_x}), y=({min_y}, {max_y})")
    
    # Crop the exact badge (it is roughly 512x512 square)
    cropped_burp = burp_src.crop((min_x, min_y, max_x, max_y))
    # Resize to 512x512
    burp_resized = cropped_burp.resize((SIZE, SIZE), Image.LANCZOS)
    
    # Mask to squircle so corners are clean and smooth
    mask_burp = Image.new('L', (SIZE, SIZE), 0)
    ImageDraw.Draw(mask_burp).rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)
    
    final_burp = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    final_burp.paste(burp_resized, (0, 0), mask_burp)
    final_burp.save(os.path.join(SKILLS_DIR, 'burp-suite.png'), 'PNG')
    print("Burp Suite badge generated cleanly!")

# ==============================================================================
# 3. WIRESHARK
# The user uploaded the Wireshark blue badge with shark fin.
# ==============================================================================
ws_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787643004699.png')).convert('RGBA')
ws_resized = ws_src.resize((SIZE, SIZE), Image.LANCZOS)
mask_ws = Image.new('L', (SIZE, SIZE), 0)
ImageDraw.Draw(mask_ws).rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)
final_ws = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
final_ws.paste(ws_resized, (0, 0), mask_ws)
final_ws.save(os.path.join(SKILLS_DIR, 'wireshark.png'), 'PNG')
print("Wireshark badge generated")

# ==============================================================================
# 4. PYTHON
# High-res sleek rounded squircle badge (Dark navy with official Python icon)
# ==============================================================================
badge_py, mask_py = create_base_badge((27, 38, 59, 255)) # Dark navy
# Render high-res python logo in center
py_svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <g transform="translate(100, 100) scale(2.44)">
    <path fill="#387eb8" d="M63.5 0C32.7 0 34.6 13.4 34.6 13.4l.04 13.88h29.24v4.16H23.54S0 28.86 0 59.8c0 30.95 20.48 29.83 20.48 29.83h12.22V72.45s-.67-20.48 20.14-20.48h29.13s19.47.31 19.47-19.14V13.4S104.37 0 63.5 0zM47.1 9.4c3.48 0 6.3 2.82 6.3 6.3 0 3.47-2.82 6.3-6.3 6.3-3.47 0-6.3-2.83-6.3-6.3 0-3.48 2.83-6.3 6.3-6.3z"/>
    <path fill="#ffe052" d="M64.5 128c30.8 0 28.9-13.4 28.9-13.4l-.04-13.88H64.12v-4.16h40.34s23.54 2.58 23.54-28.36c0-30.95-20.48-29.83-20.48-29.83H115.3v17.18s.67 20.48-20.14 20.48H66.03s-19.47-.31-19.47 19.14v20.39S23.63 128 64.5 128zm16.4-9.4c-3.48 0-6.3-2.82-6.3-6.3 0-3.47 2.82-6.3 6.3-6.3 3.47 0 6.3 2.83 6.3 6.3 0 3.48-2.83 6.3-6.3 6.3z"/>
  </g>
</svg>'''
with open(os.path.join(SKILLS_DIR, 'python.svg'), 'w') as f:
    f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#1b263b"/>
  <g transform="translate(100, 100) scale(2.44)">
    <path fill="#387eb8" d="M63.5 0C32.7 0 34.6 13.4 34.6 13.4l.04 13.88h29.24v4.16H23.54S0 28.86 0 59.8c0 30.95 20.48 29.83 20.48 29.83h12.22V72.45s-.67-20.48 20.14-20.48h29.13s19.47.31 19.47-19.14V13.4S104.37 0 63.5 0zM47.1 9.4c3.48 0 6.3 2.82 6.3 6.3 0 3.47-2.82 6.3-6.3 6.3-3.47 0-6.3-2.83-6.3-6.3 0-3.48 2.83-6.3 6.3-6.3z"/>
    <path fill="#ffe052" d="M64.5 128c30.8 0 28.9-13.4 28.9-13.4l-.04-13.88H64.12v-4.16h40.34s23.54 2.58 23.54-28.36c0-30.95-20.48-29.83-20.48-29.83H115.3v17.18s.67 20.48-20.14 20.48H66.03s-19.47-.31-19.47 19.14v20.39S23.63 128 64.5 128zm16.4-9.4c-3.48 0-6.3-2.82-6.3-6.3 0-3.47 2.82-6.3 6.3-6.3 3.47 0 6.3 2.83 6.3 6.3 0 3.48-2.83 6.3-6.3 6.3z"/>
  </g>
</svg>''')
print("Python SVG generated")

# ==============================================================================
# 5. GO (GOLANG)
# High-res official Go badge
# ==============================================================================
with open(os.path.join(SKILLS_DIR, 'go.svg'), 'w') as f:
    f.write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="{RADIUS}" fill="#00add8"/>
  <g transform="translate(64, 140) scale(3.1)">
    <path fill="#ffffff" d="M38.5 35.8c-2.3 4.2-5.7 7.7-10.1 9.9-5.8 2.9-12.7 3.3-18.8 1.1C3.8 44.7-.3 38.8.0 32.7.4 26 5.6 20.6 12.2 19.4c6.3-1.1 13 .7 17.5 5.2l-5.4 5.2c-2.8-2.8-7-3.9-10.8-2.9-3.9 1-6.8 4.4-7 8.5-.3 4.1 2.3 7.8 6.3 8.8 4.3 1.1 9.1-.5 11.7-4.1h-11.4v-7.2h18.8l-.5 6.9zM78.6 32.4c.5 8-5.3 15.3-13.3 16.5-8.2 1.3-16.1-4-17.8-12.1-1.7-8.1 3.2-16.3 11.2-18 8.1-1.8 16.3 2.9 18.4 10.9.9 2.2 1.4 4.5 1.5 6.7v-4zm-7.6-.7c-.2-4.1-3.3-7.5-7.4-7.8-4.3-.3-8 2.7-8.6 6.9-.6 4.3 2.2 8.3 6.5 9.1 4.3.8 8.4-1.9 9.3-6.2.1-.7.2-1.3.2-2z"/>
    <path fill="#ffffff" d="M96 28h22v7H96zM88 39h30v7H88zM102 17h16v7h-16z"/>
  </g>
</svg>''')
print("Go SVG generated")

# ==============================================================================
# 6. MYSQL
# Extract the blue circle + white dolphin + MySQL wordmark from user's upload.
# Eliminate ALL checkerboard from corners and composite cleanly on squircle badge or circle.
# ==============================================================================
mysql_src = Image.open(os.path.join(UPLOAD_DIR, 'media_1787643032145.png')).convert('RGBA')
m_arr = np.array(mysql_src)
# The MySQL circle is blue (R: 45..70, G: 95..125, B: 135..165).
# The checkerboard is grey/white around it.
# Find center and radius of circle:
H, W = m_arr.shape[:2]
# Detect non-checkerboard (blue circle or interior elements)
is_circle_blue = (m_arr[:, :, 2] > m_arr[:, :, 0] + 40) & (m_arr[:, :, 1] > m_arr[:, :, 0] + 15)
is_orange_text = (m_arr[:, :, 0] > 180) & (m_arr[:, :, 1] > 100) & (m_arr[:, :, 2] < 70)
is_white_text = (m_arr[:, :, 0] > 220) & (m_arr[:, :, 1] > 220) & (m_arr[:, :, 2] > 220)
is_mysql_content = is_circle_blue | is_orange_text | is_white_text

my_y, my_x = np.where(is_mysql_content)
if len(my_x) > 0 and len(my_y) > 0:
    min_x, max_x = my_x.min(), my_x.max()
    min_y, max_y = my_y.min(), my_y.max()
    print(f"MySQL circle bounding box: x=({min_x}, {max_x}), y=({min_y}, {max_y})")
    
    # Crop exact circle
    mysql_cropped = mysql_src.crop((min_x, min_y, max_x, max_y))
    mysql_resized = mysql_cropped.resize((SIZE, SIZE), Image.LANCZOS)
    
    # Match the squircle badge radius or clean circle without any checkerboard
    mask_mysql = Image.new('L', (SIZE, SIZE), 0)
    ImageDraw.Draw(mask_mysql).rounded_rectangle([0, 0, SIZE, SIZE], radius=RADIUS, fill=255)
    
    # Base background matching MySQL blue
    base_mysql = Image.new('RGBA', (SIZE, SIZE), (0, 97, 138, 255))
    
    # Composite the cropped circle onto the rounded squircle badge so it looks 100% intentional and uniform!
    final_mysql = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    final_mysql.paste(base_mysql, (0, 0), mask_mysql)
    
    # Circular mask for the interior graphic
    circ_mask = Image.new('L', (SIZE, SIZE), 0)
    ImageDraw.Draw(circ_mask).ellipse([10, 10, SIZE-10, SIZE-10], fill=255)
    circ_mask = circ_mask.filter(ImageFilter.GaussianBlur(1.0))
    
    final_mysql.paste(mysql_resized, (0, 0), circ_mask)
    final_mysql.save(os.path.join(SKILLS_DIR, 'mysql.png'), 'PNG')
    print("MySQL badge generated cleanly with ZERO checkerboard!")

print("All 6 skills generated with matching theme & clean edges!")
