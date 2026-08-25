"""
Extract Farhaan's portrait from the reference photo into a transparent cut-out and avatar.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import os
from collections import deque

SRC = 'reference/farhaan-photo.jpg'
OUT_CUTOUT = 'public/assets/name-cutout.webp'
OUT_AVATAR = 'public/assets/avatar.webp'

src = Image.open(SRC).convert('RGB')
W, H = src.size
print(f"Loaded source image {SRC} with size {W}x{H}")

# 1. Avatar generation (head crop centered on face)
head_size = int(min(W, H) * 0.55)
center_x = int(W * 0.505)
center_y = int(H * 0.40)
left = max(0, center_x - head_size // 2)
top = max(0, center_y - head_size // 2)
right = min(W, left + head_size)
bottom = min(H, top + head_size)

avatar_crop = src.crop((left, top, right, bottom)).resize((256, 256), Image.LANCZOS)
avatar_crop.save(OUT_AVATAR, quality=92, method=6)
print(f"Saved {OUT_AVATAR} 256x256")

# 2. Cutout extraction
C = np.array(src).astype(np.float32)
SENT = (255, 0, 255)

f = src.copy()
px = f.load()

# Flood fill from outer boundaries
for x in range(2, W - 2, 16):
    for y in (2, H - 3):
        c = px[x, y]
        if c != SENT and c[0] > 180 and c[1] > 180 and c[2] > 180:
            ImageDraw.floodfill(f, (x, y), SENT, thresh=22)

for y in range(2, H - 2, 16):
    for x in (2, W - 3):
        c = px[x, y]
        if c != SENT and c[0] > 180 and c[1] > 180 and c[2] > 180:
            ImageDraw.floodfill(f, (x, y), SENT, thresh=22)

bg = np.all(np.array(f) == np.array(SENT), axis=2)

# Also catch near-white backdrop regions not reached by flood
neutral = (C.max(2) - C.min(2)) < 25
pale = (C.mean(2) > 205) & neutral

def dil(m, r):
    for _ in range(r):
        o = m.copy()
        o[1:, :] |= m[:-1, :]; o[:-1, :] |= m[1:, :]
        o[:, 1:] |= m[:, :-1]; o[:, :-1] |= m[:, 1:]
        m = o
    return m

def ero(m, r): return ~dil(~m, r)

# Guard against eating shirt: shirt is deep inside, backdrop is connected to edges
bg = bg | (pale & ~ero(~bg, 25))

# Matte creation
inner, outer = ero(~bg, 3), dil(~bg, 2)
band = outer & ~inner
brightness = C.mean(2)

alpha = np.where(inner, 1.0, 0.0)
alpha[band] = np.clip((245.0 - brightness[band]) / 80.0, 0.0, 1.0)
alpha[~outer] = 0.0

alpha = np.array(
    Image.fromarray((alpha * 255).astype(np.uint8), 'L').filter(ImageFilter.GaussianBlur(0.6))
).astype(np.float32) / 255.0

# Keep main body component and fill enclosed holes
solid = alpha > 0.1
keep = np.zeros_like(solid)
for y in range(H):
    row = solid[y]
    if not row.any(): continue
    edges = np.flatnonzero(np.diff(np.concatenate(([0], row.view(np.int8), [0]))))
    starts, ends = edges[0::2], edges[1::2]
    lengths = ends - starts
    longest = lengths.max()
    for st, en, ln in zip(starts, ends, lengths):
        if ln >= max(0.02 * longest, 4):
            keep[y, st:en] = True

alpha = np.where(keep, alpha, 0.0)

# Fill holes inside body
holes = alpha < 0.35
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

# Despill against white/pale backdrop
BACKDROP = np.array([242.0, 242.0, 242.0])
a3 = np.dstack([alpha] * 3)
F = np.clip(np.where(a3 > 0.02, (C - (1.0 - a3) * BACKDROP) / np.maximum(a3, 0.02), C), 0, 255)

img = Image.fromarray(np.dstack([F, alpha * 255]).astype(np.uint8), 'RGBA')
bbox = img.split()[3].getbbox()
if bbox:
    img = img.crop(bbox)

img.save(OUT_CUTOUT, quality=92, method=6)
print(f"Saved {OUT_CUTOUT} {img.size} aspect {img.width/img.height:.3f} {os.path.getsize(OUT_CUTOUT)//1024} KB")
