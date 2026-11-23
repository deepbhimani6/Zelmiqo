#!/usr/bin/env python3
"""
generate_dock_annotated_assets.py
Takes the user's 9 uploaded base images (with user-drawn red boxes)
and stamps crisp red badge tabs with matching workstation numbers onto each box.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_UPLOADED = '/Users/shunyavkashminim2/.gemini/antigravity/brain/15b07e7f-69f3-4dc8-984e-f7fdb152baee/.user_uploaded/'
OUTPUT_DIR = '/Users/shunyavkashminim2/Downloads/Test/new-content-html-pages/assets/'

FONT_PATH = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
RED_BG = (230, 25, 25)      # #e61919 exact standard
WHITE_TEXT = (255, 255, 255) # Pure white text
BORDER_COLOR = (180, 20, 20)

def draw_badge(draw, text, x, y, font, align='left', place='above'):
    """
    Draws a crisp callout badge tab at (x, y).
    place: 'above' (tab sits on top of y), 'inside' (tab sits below y), or 'top_left'
    """
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pad_h = 7
    pad_v = 4
    bw = tw + pad_h * 2
    bh = th + pad_v * 2
    
    if align == 'center':
        bx = int(x - bw / 2)
    elif align == 'right':
        bx = int(x - bw)
    else:
        bx = int(x)
        
    if place == 'above':
        by = int(y - bh)
    elif place == 'inside':
        by = int(y)
    else:
        by = int(y - bh / 2)
        
    # Draw solid red rectangle tab with slight rounding or clean corners
    draw.rectangle([bx, by, bx + bw, by + bh], fill=RED_BG)
    # White text centered in badge
    tx = bx + pad_h
    ty = by + pad_v - bbox[1]
    draw.text((tx, ty), text, font=font, fill=WHITE_TEXT)
    return (bx, by, bx + bw, by + bh)


def process_hero():
    src = os.path.join(BASE_UPLOADED, 'media_1795411945974_89f8a25d.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Box 1: Title x=[505, 956], y=[11, 90]
    draw_badge(draw, "[1] Title", 505, 11, font, align='left', place='inside')
    
    # Box 2: Callout on watch image x=[236, 441], y=[106, 169]
    draw_badge(draw, "[Callout] Image Tag", 236, 106, font, align='left', place='above')
    
    # Box 3: Subtitle x=[509, 938], y=[96, 168]
    draw_badge(draw, "[1] Subtitle", 509, 96, font, align='left', place='inside')
    
    # Box 4: 4 Bullet points x=[505, 701], y=[170, 305]
    draw_badge(draw, "[4] Highlights", 505, 170, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_hero.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_faqs():
    src = os.path.join(BASE_UPLOADED, 'media_1795412083015_281d8c54.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Header: y=[15, 128], x=[532, 1005]
    draw_badge(draw, "[1] Header", 532, 15, font, align='left', place='inside')
    
    # Accordion 1: y=[140, 211], x=[526, 1005]
    draw_badge(draw, "[FAQ 1] Multi-Device Charging", 526, 140, font, align='left', place='inside')
    
    # Accordion 2: y=[226, 299], x=[526, 1012]
    draw_badge(draw, "[FAQ 2] iPhone & Samsung Compatibility", 526, 226, font, align='left', place='inside')
    
    # Accordion 3: y=[312, 386], x=[516, 1005]
    draw_badge(draw, "[FAQ 3] Screen Visibility & Cases", 516, 312, font, align='left', place='inside')
    
    # Accordion 4: y=[397, 471], x=[513, 1005]
    draw_badge(draw, "[FAQ 4] Built-In Watch Stand", 513, 397, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_faqs.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_two_col():
    src = os.path.join(BASE_UPLOADED, 'media_1795412104022_41859d61.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Top box: y=[108, 232], x=[28, 463]
    draw_badge(draw, "[1] Heading & Value Story", 28, 108, font, align='left', place='inside')
    
    # Bottom box: y=[242, 356], x=[33, 474]
    draw_badge(draw, "[2] Trust Guarantee Cards", 33, 242, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_two_col.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_center_4blocks():
    src = os.path.join(BASE_UPLOADED, 'media_1795412132011_f1445191.png')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Top header: y=[7, 119], x=[245, 787]
    draw_badge(draw, "[1] Header", 245, 7, font, align='left', place='inside')
    
    # Block 1 (Left top): y=[177, 256], x=[117, 369]
    draw_badge(draw, "[2] Block 1", 117, 177, font, align='left', place='inside')
    
    # Block 2 (Left bottom): y=[261, 334], x=[123, 367]
    draw_badge(draw, "[3] Block 2", 123, 261, font, align='left', place='inside')
    
    # Block 3 (Right top): y=[175, 256], x=[645, 896]
    draw_badge(draw, "[4] Block 3", 645, 175, font, align='left', place='inside')
    
    # Block 4 (Right bottom): y=[261, 336], x=[645, 896]
    draw_badge(draw, "[5] Block 4", 645, 261, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_center_4blocks.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_benefits_grid():
    src = os.path.join(BASE_UPLOADED, 'media_1795412160735_e89e0e3b.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Header: y=[9, 77], x=[291, 721]
    draw_badge(draw, "[1] Header", 291, 9, font, align='left', place='inside')
    
    # Card 1 (Top Left): y=[113, 255], x=[487, 690]
    draw_badge(draw, "[2] Less Cable Clutter", 487, 113, font, align='left', place='inside')
    
    # Card 2 (Top Right): y=[116, 255], x=[692, 891]
    draw_badge(draw, "[3] Phone Stays Visible", 692, 116, font, align='left', place='inside')
    
    # Card 3 (Bottom Left): y=[259, 400], x=[491, 689]
    draw_badge(draw, "[4] Everything in One Place", 491, 259, font, align='left', place='inside')
    
    # Card 4 (Bottom Right): y=[260, 398], x=[692, 891]
    draw_badge(draw, "[5] Cleaner Bedside Setup", 692, 260, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_benefits_grid.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_table():
    src = os.path.join(BASE_UPLOADED, 'media_1795412179545_27de365f.png')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Left Header: y=[57, 163], x=[59, 482]
    draw_badge(draw, "[1] Header & Value Pitch", 59, 57, font, align='left', place='inside')
    
    # Right Table Matrix: y=[17, 276], x=[523, 929]
    draw_badge(draw, "[2] Comparison Table Matrix", 523, 17, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_table.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_marquee():
    src = os.path.join(BASE_UPLOADED, 'media_1795412202659_8e1e73ba.png')
    raw = Image.open(src).convert('RGBA')
    rw, rh = raw.size # (1024, 51)
    
    # Create canvas of height 180 with website dark navy background (11, 19, 41)
    # This provides clean space for the 4 callout badges above the ribbon without obscuring text
    ch = 180
    canvas = Image.new('RGB', (1024, ch), (11, 19, 41))
    
    # Paste marquee ribbon vertically centered at y=70
    paste_y = 70
    canvas.paste(raw, (0, paste_y), raw if raw.mode == 'RGBA' else None)
    
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(FONT_PATH, 11)
    
    # The 4 pillars in the user's image are at:
    # Pillar 1: x=[121, 266], y=[paste_y + 10, paste_y + 40]
    # Pillar 2: x=[296, 432], y=[paste_y + 12, paste_y + 40]
    # Pillar 3: x=[461, 586], y=[paste_y + 11, paste_y + 40]
    # Pillar 4: x=[616, 734], y=[paste_y + 13, paste_y + 40]
    draw_badge(draw, "[1] Quality Guarantee", 121, paste_y + 10, font, align='left', place='above')
    draw_badge(draw, "[2] Worldwide Shipping", 296, paste_y + 12, font, align='left', place='above')
    draw_badge(draw, "[3] Global Delivery", 461, paste_y + 11, font, align='left', place='above')
    draw_badge(draw, "[4] Privacy Protected", 616, paste_y + 13, font, align='left', place='above')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_marquee.jpg')
    canvas.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_customers():
    src = os.path.join(BASE_UPLOADED, 'media_1795412214461_59d69430.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Header: y=[6, 125], x=[320, 735]
    draw_badge(draw, "[1] Section Header", 320, 6, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_customers.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


def process_related():
    src = os.path.join(BASE_UPLOADED, 'media_1795412224841_08e96bed.jpg')
    im = Image.open(src).convert('RGB')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, 13)
    
    # Header: y=[17, 96], x=[344, 635]
    draw_badge(draw, "[1] Header", 344, 17, font, align='left', place='inside')
    
    out_path = os.path.join(OUTPUT_DIR, 'product_dock_related.jpg')
    im.save(out_path, 'JPEG', quality=95)
    print("Saved:", out_path)


if __name__ == '__main__':
    process_hero()
    process_faqs()
    process_two_col()
    process_center_4blocks()
    process_benefits_grid()
    process_table()
    process_marquee()
    process_customers()
    process_related()
    print("\nAll 9 dock images annotated successfully with matching numbers!")
