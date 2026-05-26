#!/usr/bin/env python3
"""
Composite Schaubilder onto a 1080x1920 white canvas with padding.

Usage:
    python3 make-tiktok-composites.py [VIDEO_DIR]

VIDEO_DIR defaults to current directory. Looks for ./schaubilder/*.jpeg and
*.png, generates ./tiktok-1080x1920/tiktok-<NAME>.png for each.

Output ist PNG mit sRGB-ICC-Profil. Grund: TikTok-Upload vom iPhone erkennt
PNG zuverlaessig, JPGs ohne Profil werden teils farblich verschoben dargestellt
oder gar nicht akzeptiert. Bei Flat-Graphics mit viel Weissraum ist PNG zudem
meist kleiner als das frueher genutzte JPG (Q92).
"""

from PIL import Image
from PIL.ImageCms import createProfile, ImageCmsProfile
import sys
import os

VIDEO_DIR = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
src_dir = os.path.join(VIDEO_DIR, "schaubilder")
out_dir = os.path.join(VIDEO_DIR, "tiktok-1080x1920")

if not os.path.isdir(src_dir):
    print(f"Fehler: {src_dir} existiert nicht")
    sys.exit(1)

os.makedirs(out_dir, exist_ok=True)

CANVAS_W, CANVAS_H = 1080, 1920

# Padding um das Schaubild herum. Werte 2026-05-26 nach unten gezogen,
# damit das Schaubild groesser erscheint und mobil besser lesbar ist.
# Greenscreen-Raum unten bleibt mit >800px ausreichend fuer den Sprecher.
PAD_TOP = 100
PAD_SIDE = 60

TARGET_W = CANVAS_W - 2 * PAD_SIDE

# sRGB-Profil als Bytes, damit Farben auf iPhone und in TikTok eindeutig
# interpretiert werden. createProfile liefert ein PIL-internes Profil,
# ImageCmsProfile.tobytes() schreibt es ins PNG-Header.
srgb_icc_bytes = ImageCmsProfile(createProfile("sRGB")).tobytes()

inputs = sorted(
    f for f in os.listdir(src_dir)
    if f.lower().endswith((".jpeg", ".jpg", ".png"))
    and not f.startswith(".")
)

if not inputs:
    print(f"Keine Bilder in {src_dir} gefunden.")
    sys.exit(1)

for fname in inputs:
    src_path = os.path.join(src_dir, fname)
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    new_h = int(h * (TARGET_W / w))
    img_resized = img.resize((TARGET_W, new_h), Image.LANCZOS)

    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), (255, 255, 255))
    canvas.paste(img_resized, (PAD_SIDE, PAD_TOP))

    stem = os.path.splitext(fname)[0]
    out_path = os.path.join(out_dir, f"tiktok-{stem}.png")
    canvas.save(out_path, "PNG", optimize=True, icc_profile=srgb_icc_bytes)
    bottom_space = CANVAS_H - PAD_TOP - new_h
    print(f"OK {out_path}  ({TARGET_W}x{new_h} an {PAD_SIDE},{PAD_TOP}, {bottom_space}px unten frei)")

print(f"\n{len(inputs)} Schaubilder verarbeitet.")
