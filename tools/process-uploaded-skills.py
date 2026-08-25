"""
Process user-uploaded skill badges:
1. Kali Linux (media_1787642918959.png)
2. Burp Suite (media_1787642952414.png)
3. Wireshark (media_1787643004699.png)
4. MySQL (media_1787643032145.png)
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import os

UPLOAD_DIR = r'C:\Users\farha\.gemini\antigravity-ide\brain\03934d6f-7772-4a35-97cb-c6e4719db5d3\.user_uploaded'
SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)

# 1. Kali Linux
kali_src_path = os.path.join(UPLOAD_DIR, 'media_1787642918959.png')
kali_img = Image.open(kali_src_path).convert('RGBA')
# Crop transparent bounds
k_bbox = kali_img.getbbox()
if k_bbox:
    kali_cropped = kali_img.crop(k_bbox)
    # Save as 512x512
    kali_out = kali_cropped.resize((512, 512), Image.LANCZOS)
    kali_out.save(os.path.join(SKILLS_DIR, 'kali.png'), 'PNG')
    print("Processed kali.png")

# 2. Burp Suite
# Check if there is a fake checkerboard background
burp_src_path = os.path.join(UPLOAD_DIR, 'media_1787642952414.png')
burp_img = Image.open(burp_src_path).convert('RGBA')
b_arr = np.array(burp_img)
# The checkerboard is grey/white on the outside. The badge itself is rounded square with dark grey (#333) and orange (#e85d26) with white divider.
# Let's clean the outer background around the rounded square badge
H, W = b_arr.shape[:2]
# Detect badge by looking for non-neutral checkerboard pixels or creating clean mask
# Let's find badge center & size
# In Burp image, the badge corners have checkerboard (pixels with R~G~B in [180..240]).
# Let's find the bounding box of the actual icon badge:
# The dark side has R < 80, G < 80, B < 80; The orange side has R > 180, G < 120
is_badge = (b_arr[:, :, 0] < 80) | (b_arr[:, :, 0] > 180) | (b_arr[:, :, :3].max(2) - b_arr[:, :, :3].min(2) > 30)
# Outer checkerboard is neutral grey/white (max-min < 10)
# Let's flood fill or mask out the outer checkerboard from corners:
f_burp = Image.fromarray(b_arr[:, :, :3])
px = f_burp.load()
SENT = (0, 255, 0)
for y in (0, 1, 2, H-3, H-2, H-1):
    for x in (0, 1, 2, W-3, W-2, W-1):
        if px[x, y] != SENT:
            ImageDraw.floodfill(f_burp, (x, y), SENT, thresh=35)

bg_mask = np.all(np.array(f_burp) == np.array(SENT), axis=2)
burp_alpha = np.where(bg_mask, 0, 255).astype(np.uint8)

# Anti-alias mask
mask_im = Image.fromarray(burp_alpha, 'L').filter(ImageFilter.GaussianBlur(0.6))
burp_clean = Image.fromarray(b_arr[:, :, :3], 'RGB')
burp_clean.putalpha(mask_im)
b_bbox = burp_clean.getbbox()
if b_bbox:
    burp_cropped = burp_clean.crop(b_bbox).resize((512, 512), Image.LANCZOS)
    burp_cropped.save(os.path.join(SKILLS_DIR, 'burp-suite.png'), 'PNG')
    print("Processed burp-suite.png")

# 3. Wireshark
ws_src_path = os.path.join(UPLOAD_DIR, 'media_1787643004699.png')
ws_img = Image.open(ws_src_path).convert('RGBA')
ws_bbox = ws_img.getbbox()
if ws_bbox:
    ws_cropped = ws_img.crop(ws_bbox).resize((512, 512), Image.LANCZOS)
    ws_cropped.save(os.path.join(SKILLS_DIR, 'wireshark.png'), 'PNG')
    print("Processed wireshark.png")

# 4. MySQL
# Check if there is a fake checkerboard background
mysql_src_path = os.path.join(UPLOAD_DIR, 'media_1787643032145.png')
mysql_img = Image.open(mysql_src_path).convert('RGBA')
m_arr = np.array(mysql_img)
H, W = m_arr.shape[:2]
# The circle has color #33678c / #3e739d (blue).
# Flood fill the outer corner checkerboard
f_mysql = Image.fromarray(m_arr[:, :, :3])
px = f_mysql.load()
SENT = (0, 255, 0)
for y in (0, 1, 2, H-3, H-2, H-1):
    for x in (0, 1, 2, W-3, W-2, W-1):
        if px[x, y] != SENT:
            ImageDraw.floodfill(f_mysql, (x, y), SENT, thresh=45)

m_bg_mask = np.all(np.array(f_mysql) == np.array(SENT), axis=2)
mysql_alpha = np.where(m_bg_mask, 0, 255).astype(np.uint8)

# Anti-alias mask
m_mask_im = Image.fromarray(mysql_alpha, 'L').filter(ImageFilter.GaussianBlur(0.8))
mysql_clean = Image.fromarray(m_arr[:, :, :3], 'RGB')
mysql_clean.putalpha(m_mask_im)
m_bbox = mysql_clean.getbbox()
if m_bbox:
    mysql_cropped = mysql_clean.crop(m_bbox).resize((512, 512), Image.LANCZOS)
    mysql_cropped.save(os.path.join(SKILLS_DIR, 'mysql.png'), 'PNG')
    print("Processed mysql.png")

# 5. Python & Go (generate crisp high-res badges matching 512x512)
# For Python & Go, render crisp badges
print("All user skills processed successfully!")
