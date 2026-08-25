"""
Perfect background cutout for Farhaan D:
- Eliminates any stray white background triangle near shoulders/neck
- Perfectly preserves white shirt collar & tie inside the suit
- Clean anti-aliased silhouette with zero rogue alpha pixels
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import os
from collections import deque

SRC = 'reference/farhaan-photo.jpg'
OUT_CUTOUT = 'public/assets/name-cutout.webp'
OUT_PORTRAIT = 'public/assets/farhaan-portrait.webp'
OUT_AVATAR = 'public/assets/avatar.webp'

src = Image.open(SRC).convert('RGB')
W, H = src.size
C = np.array(src).astype(np.float32)

# Define subject bounding hull / shoulder geometry
# Farhaan is vertically centered around x=512.
# Head top: y ~ 230
# Chin: y ~ 540
# Collar: y ~ 560..680, x ~ 400..620
# Left Shoulder: x=140 to 400, y=690 to 600
# Right Shoulder: x=620 to 880, y=600 to 690

# Let's create an exact classification mask:
# A pixel is background if:
# 1. It is neutral bright (min(RGB) > 175 and max(RGB)-min(RGB) < 35) AND it is outside the inner shirt/body polygon.
# 2. It is connected to the image border.

# Inner shirt/collar protection mask (protect collar from being eaten):
shirt_polygon = [
    (410, 560), (490, 560), (512, 570), (534, 560), (614, 560),
    (605, 680), (545, 780), (480, 780), (415, 680)
]
shirt_mask_img = Image.new('L', (W, H), 0)
ImageDraw.Draw(shirt_mask_img).polygon(shirt_polygon, fill=255)
shirt_protected = np.array(shirt_mask_img) > 0

# Jacket & skin & hair detection
is_dark_hair = (C[:, :, 0] < 100) & (C[:, :, 1] < 100) & (C[:, :, 2] < 100) & (np.arange(H)[:, None] < 560)
is_jacket = (C[:, :, 0] < 170) & (C[:, :, 1] < 170) & (C[:, :, 2] < 185) & (np.arange(H)[:, None] >= 580)
is_skin = (C[:, :, 0] > 115) & (C[:, :, 0] > C[:, :, 2] + 12) & (np.arange(H)[:, None] < 620)
is_tie = (np.arange(H)[:, None] >= 630) & (np.abs(np.arange(W)[None, :] - 512) < 65)

# Combined solid subject features
solid_subject = is_dark_hair | is_jacket | is_skin | is_tie | shirt_protected

# Everything else that is pale/neutral is background
neutral_pale = (C.min(2) > 165) & ((C.max(2) - C.min(2)) < 40)
bg_raw = neutral_pale & ~solid_subject

# Add flood-fill from edges
SENT = (255, 0, 255)
f = src.copy()
px = f.load()

for x in range(0, W, 4):
    for y in (0, 1, 2, H - 3, H - 2, H - 1):
        if px[x, y] != SENT and (bg_raw[y, x] or min(px[x, y]) > 160):
            ImageDraw.floodfill(f, (x, y), SENT, thresh=28)

for y in range(0, H, 4):
    for x in (0, 1, 2, W - 3, W - 2, W - 1):
        if px[x, y] != SENT and (bg_raw[y, x] or min(px[x, y]) > 160):
            ImageDraw.floodfill(f, (x, y), SENT, thresh=28)

# Specifically seed the triangular shoulder dip areas to ensure flood cleans them
# Left shoulder dip: x=340..390, y=560..600
# Right shoulder dip: x=620..680, y=560..640
for sx, sy in [(360, 560), (370, 580), (640, 580), (650, 600), (660, 620)]:
    if px[sx, sy] != SENT and bg_raw[sy, sx]:
        ImageDraw.floodfill(f, (sx, sy), SENT, thresh=26)

bg_flooded = np.all(np.array(f) == np.array(SENT), axis=2)

# Combine: background is anything flooded or (pale and not solid subject and connected to top/sides)
final_bg = bg_flooded | (bg_raw & ~solid_subject)

# Invert to get subject alpha
alpha = np.where(final_bg, 0.0, 1.0).astype(np.float32)

# Clean morph: dilate then erode subject to close any tiny hair notches
def dil(m, r):
    for _ in range(r):
        o = m.copy()
        o[1:, :] |= m[:-1, :]; o[:-1, :] |= m[1:, :]
        o[:, 1:] |= m[:, :-1]; o[:, :-1] |= m[:, 1:]
        m = o
    return m
def ero(m, r): return ~dil(~m, r)

subj_bool = alpha > 0.5
subj_bool = ero(dil(subj_bool, 2), 2)

# Keep only largest connected component (Farhaan's body)
visited = np.zeros_like(subj_bool, dtype=bool)
components = {}
comp_id = 1
for y in range(H):
    for x in range(W):
        if subj_bool[y, x] and not visited[y, x]:
            q = deque([(y, x)])
            visited[y, x] = True
            pixels = []
            while q:
                cy, cx = q.popleft()
                pixels.append((cy, cx))
                for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
                    if 0 <= ny < H and 0 <= nx < W and subj_bool[ny, nx] and not visited[ny, nx]:
                        visited[ny, nx] = True
                        q.append((ny, nx))
            components[comp_id] = pixels
            comp_id += 1

if components:
    largest_k = max(components.keys(), key=lambda k: len(components[k]))
    clean_subj = np.zeros_like(subj_bool, dtype=bool)
    for cy, cx in components[largest_k]:
        clean_subj[cy, cx] = True
    alpha = np.where(clean_subj, 1.0, 0.0)

# Fill holes inside body
holes = alpha < 0.5
seen = np.zeros_like(holes)
q = deque()
for x in range(W):
    for y in (0, H - 1):
        if holes[y, x] and not seen[y, x]:
            seen[y, x] = True; q.append((y, x))
for y in range(H):
    for x in (0, W - 1):
        if holes[y, x] and not seen[y, x]:
            seen[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for ny, nx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
        if 0 <= ny < H and 0 <= nx < W and holes[ny, nx] and not seen[ny, nx]:
            seen[ny, nx] = True; q.append((ny, nx))

enclosed = holes & ~seen
alpha = np.where(enclosed, 1.0, alpha)

# Subtle anti-aliased edge smoothing
alpha_smooth = np.array(
    Image.fromarray((alpha * 255).astype(np.uint8), 'L').filter(ImageFilter.GaussianBlur(0.8))
).astype(np.float32) / 255.0

# Zero out anything truly background so feMorphology doesn't create red blocks
alpha_final = np.where(alpha_smooth < 0.08, 0.0, alpha_smooth)

# Despill against backdrop
BACKDROP = np.array([242.0, 242.0, 242.0])
a3 = np.dstack([alpha_final] * 3)
F = np.clip(np.where(a3 > 0.02, (C - (1.0 - a3) * BACKDROP) / np.maximum(a3, 0.02), C), 0, 255)

rgba = np.dstack([F, alpha_final * 255]).astype(np.uint8)
img_full = Image.fromarray(rgba, 'RGBA')
bbox = img_full.split()[3].getbbox()

# 1. Section 02 Frame Portrait (540 x 750 framing on paper)
if bbox:
    cropped = img_full.crop(bbox)
    pad_x = 40
    p_w = cropped.width + pad_x * 2
    p_h = int(p_w * 1.55)
    portrait_canvas = Image.new('RGBA', (p_w, p_h), (0, 0, 0, 0))
    paste_y = max(0, p_h - cropped.height - 30)
    portrait_canvas.paste(cropped, (pad_x, paste_y), cropped)
    portrait_canvas.save(OUT_PORTRAIT, quality=95, method=6)
    print(f"Saved {OUT_PORTRAIT} {portrait_canvas.size}")

# 2. Section 03 Name Cutout (tight bounding box)
if bbox:
    cutout_img = img_full.crop(bbox)
    cutout_img.save(OUT_CUTOUT, quality=95, method=6)
    print(f"Saved {OUT_CUTOUT} {cutout_img.size}")

# 3. Avatar
head_size = int(min(W, H) * 0.52)
cx, cy = int(W * 0.505), int(H * 0.38)
av_left = max(0, cx - head_size // 2)
av_top = max(0, cy - head_size // 2)
av_crop = src.crop((av_left, av_top, av_left + head_size, av_top + head_size)).resize((256, 256), Image.LANCZOS)
av_crop.save(OUT_AVATAR, quality=95, method=6)
print(f"Saved {OUT_AVATAR} 256x256")
