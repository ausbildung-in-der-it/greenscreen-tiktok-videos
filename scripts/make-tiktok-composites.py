#!/usr/bin/env python3
"""
Composite Schaubilder onto a 1080x1920 white canvas with padding.

Usage:
    python3 make-tiktok-composites.py [VIDEO_DIR]

VIDEO_DIR defaults to current directory. Looks for ./schaubilder/*.jpeg and
*.png, generates ./tiktok-1080x1920/tiktok-<NAME>.jpg for each.
"""

from PIL import Image
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

# Padding um das Schaubild herum
PAD_TOP = 180
PAD_SIDE = 130

TARGET_W = CANVAS_W - 2 * PAD_SIDE

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
    out_path = os.path.join(out_dir, f"tiktok-{stem}.jpg")
    canvas.save(out_path, "JPEG", quality=92)
    bottom_space = CANVAS_H - PAD_TOP - new_h
    print(f"OK {out_path}  ({TARGET_W}x{new_h} an {PAD_SIDE},{PAD_TOP}, {bottom_space}px unten frei)")

print(f"\n{len(inputs)} Schaubilder verarbeitet.")
