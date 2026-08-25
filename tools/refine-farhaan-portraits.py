"""
High-precision extraction for Farhaan's portraits:
1. name-cutout.webp (Section 03: moving poster cutout)
2. farhaan-portrait.webp (Section 02: intro section standing portrait frame)
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
print(f"Processing {SRC} ({W}x{H})")

C = np.array(src).astype(np.float32)

# Analyze background vs foreground
# Background is the textured white/cream wall (mean RGB > 210, low saturation)
# Subject: Dark hair (very low RGB), blue tweed jacket (RGB ~ (70, 90, 110)), white collar, patterned tie, skin (high red/warm).

# 1. Flood fill from boundary seeds
SENT = (255, 0, 255)
f = src.copy()
px = f.load()

# Boundary seeds with smart color thresholding
for x in range(0, W, 8):
    for y in (0, 1, 2, H - 3, H - 2, H - 1):
        c = px[x, y]
        if c != SENT:
            # check if backdrop-like
            if min(c) > 170 and max(c) - min(c) < 35:
                ImageDraw.floodfill(f, (x, y), SENT, thresh=24)

for y in range(0, H, 8):
    for x in (0, 1, 2, W - 3, W - 2, W - 1):
        c = px[x, y]
        if c != SENT:
            if min(c) > 170 and max(c) - min(c) < 35:
                ImageDraw.floodfill(f, (x, y), SENT, thresh=24)

bg_flood = np.all(np.array(f) == np.array(SENT), axis=2)

# 2. Refined backdrop mask
neutral_bg = (C.max(2) - C.min(2)) < 30
bright_bg = (C.min(2) > 195) & neutral_bg

# Expand flood into bright neutral backdrop regions connected to exterior
def dil(m, r):
    for _ in range(r):
        o = m.copy()
        o[1:, :] |= m[:-1, :]; o[:-1, :] |= m[1:, :]
        o[:, 1:] |= m[:, :-1]; o[:, :-1] |= m[:, 1:]
        m = o
    return m

def ero(m, r): return ~dil(~m, r)

# Combine flood with bright backdrop that is connected within 30px of exterior flood
bg_mask = bg_flood | (bright_bg & dil(bg_flood, 30))

# 3. Guard subject regions (protect hair, jacket, collar)
# Jacket has blue/grey texture (R < 160 or (G-R > 5 and B-R > 5))
# Hair has R < 90, G < 90, B < 90
# Skin has R > G > B
is_hair = (C[:, :, 0] < 95) & (C[:, :, 1] < 95) & (C[:, :, 2] < 95)
is_jacket = (C[:, :, 0] < 160) & (C[:, :, 1] < 160)
is_skin = (C[:, :, 0] > 110) & (C[:, :, 0] > C[:, :, 2] + 15)

subject_core = is_hair | is_jacket | is_skin
bg_mask = bg_mask & ~subject_core

# 4. Generate pristine matte
inner = ero(~bg_mask, 2)
outer = dil(~bg_mask, 2)
band = outer & ~inner

dist = np.abs(C - 240.0).max(2)
alpha = np.where(inner, 1.0, 0.0)
alpha[band] = np.clip(dist[band] / 60.0, 0.0, 1.0)
alpha[~outer] = 0.0

# 5. Connected component filter on body (keep only the main human body, remove any loose floating noise)
solid = alpha > 0.15
labeled = np.zeros_like(solid, dtype=int)
component_id = 1
components = {}

# BFS for largest connected component
visited = np.zeros_like(solid, dtype=bool)
for y in range(H):
    for x in range(W):
        if solid[y, x] and not visited[y, x]:
            q = deque([(y, x)])
            visited[y, x] = True
            size = 0
            pixels = []
            while q:
                cy, cx = q.popleft()
                size += 1
                pixels.append((cy, cx))
                for ny, nx in ((cy+1, cx), (cy-1, cx), (cy, cx+1), (cy, cx-1)):
                    if 0 <= ny < H and 0 <= nx < W and solid[ny, nx] and not visited[ny, nx]:
                        visited[ny, nx] = True
                        q.append((ny, nx))
            components[component_id] = (size, pixels)
            component_id += 1

if components:
    largest_id = max(components.keys(), key=lambda k: components[k][0])
    main_body_mask = np.zeros_like(solid, dtype=bool)
    for cy, cx in components[largest_id][1]:
        main_body_mask[cy, cx] = True
        
    # Strictly zero out anything not in main body
    alpha = np.where(main_body_mask, alpha, 0.0)

# Fill holes inside body
holes = alpha < 0.2
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

# HARD CLAMP: absolutely NO non-zero alpha noise in background (< 0.05 -> 0.0)
alpha = np.where(alpha < 0.05, 0.0, alpha)

# Despill against white/cream backdrop
BACKDROP = np.array([238.0, 238.0, 238.0])
a3 = np.dstack([alpha] * 3)
F = np.clip(np.where(a3 > 0.02, (C - (1.0 - a3) * BACKDROP) / np.maximum(a3, 0.02), C), 0, 255)

# Build RGBA image
rgba = np.dstack([F, alpha * 255]).astype(np.uint8)
img_full = Image.fromarray(rgba, 'RGBA')

# 1. Save Section 02 Frame Portrait (Full framing 540x720 / aspect ~144:335)
portrait_img = img_full.copy()
bbox = portrait_img.split()[3].getbbox()
if bbox:
    cropped = portrait_img.crop(bbox)
    # Give a tiny padding around shoulders/hair
    pad_w = 40
    new_w = cropped.width + pad_w * 2
    new_h = int(new_w * (1000 / 600))
    canvas = Image.new('RGBA', (new_w, new_h), (0, 0, 0, 0))
    # Place subject anchored toward bottom
    paste_y = max(0, new_h - cropped.height - 20)
    canvas.paste(cropped, (pad_w, paste_y), cropped)
    canvas.save(OUT_PORTRAIT, quality=94, method=6)
    print(f"Saved {OUT_PORTRAIT} {canvas.size}")

# 2. Save Section 03 Name Cutout (tight bounding box)
if bbox:
    cutout_cropped = img_full.crop(bbox)
    cutout_cropped.save(OUT_CUTOUT, quality=94, method=6)
    print(f"Saved {OUT_CUTOUT} {cutout_cropped.size} (aspect {cutout_cropped.width/cutout_cropped.height:.3f})")

# 3. Save Avatar (256x256)
head_size = int(min(W, H) * 0.52)
cx, cy = int(W * 0.505), int(H * 0.38)
av_left = max(0, cx - head_size // 2)
av_top = max(0, cy - head_size // 2)
av_crop = src.crop((av_left, av_top, av_left + head_size, av_top + head_size)).resize((256, 256), Image.LANCZOS)
av_crop.save(OUT_AVATAR, quality=94, method=6)
print(f"Saved {OUT_AVATAR} 256x256")
