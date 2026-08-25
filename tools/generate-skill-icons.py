"""
Generate crisp, high-resolution skill icons for Farhaan's cybersecurity & programming stack:
- Kali Linux
- Burp Suite
- Wireshark
- Python
- Go (Golang)
- MySQL
"""
import os
from PIL import Image, ImageDraw, ImageFont

SKILLS_DIR = 'public/assets/skills'
os.makedirs(SKILLS_DIR, exist_ok=True)

SIZE = 512

def create_kali_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Rounded dark tile with Kali cyan accent
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(15, 23, 42, 255), outline=(56, 189, 248, 200), width=6)
    
    # Dragon stylized curve / Kali emblem shape
    # Background subtle glow
    draw.ellipse([SIZE//2 - 140, SIZE//2 - 140, SIZE//2 + 140, SIZE//2 + 140], fill=(30, 58, 138, 180))
    
    # Stylized Dragon fin & tail
    points = [
        (256, 80), (310, 150), (380, 160), (330, 210), (360, 280),
        (300, 270), (256, 350), (220, 280), (160, 310), (180, 230),
        (130, 180), (200, 170), (256, 80)
    ]
    draw.polygon(points, fill=(56, 189, 248, 255))
    draw.text((256, 400), "KALI", fill=(240, 246, 252, 255), anchor="mm")
    
    img.save(os.path.join(SKILLS_DIR, 'kali.png'), 'PNG')
    print("Saved kali.png")

def create_burp_suite_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # PortSwigger orange rounded tile
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(234, 88, 12, 255))
    
    # White B / Burp Suite badge
    draw.rounded_rectangle([100, 100, SIZE-100, SIZE-100], radius=50, fill=(255, 255, 255, 255))
    draw.rounded_rectangle([140, 140, SIZE-140, SIZE-140], radius=35, fill=(234, 88, 12, 255))
    
    # Inner stylized 'BS' monogram
    draw.rectangle([190, 180, 230, 332], fill=(255, 255, 255, 255))
    draw.ellipse([210, 180, 320, 260], fill=(255, 255, 255, 255))
    draw.ellipse([240, 205, 290, 235], fill=(234, 88, 12, 255))
    draw.ellipse([210, 252, 330, 332], fill=(255, 255, 255, 255))
    draw.ellipse([240, 277, 300, 307], fill=(234, 88, 12, 255))
    
    img.save(os.path.join(SKILLS_DIR, 'burp-suite.png'), 'PNG')
    print("Saved burp-suite.png")

def create_wireshark_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Wireshark Blue rounded tile
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(24, 88, 168, 255))
    
    # Wireshark white Shark Fin
    # Wave under fin
    draw.arc([80, 280, 432, 420], start=180, end=0, fill=(255, 255, 255, 180), width=18)
    
    # Shark fin polygon
    fin = [
        (130, 320), (220, 310), (320, 140), (270, 170), (230, 220), (130, 320)
    ]
    draw.polygon(fin, fill=(255, 255, 255, 255))
    
    img.save(os.path.join(SKILLS_DIR, 'wireshark.png'), 'PNG')
    print("Saved wireshark.png")

def create_python_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Dark modern tile
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(30, 41, 59, 255))
    
    # Blue top snake
    draw.rounded_rectangle([140, 120, 320, 240], radius=40, fill=(56, 130, 194, 255))
    draw.rounded_rectangle([140, 120, 240, 340], radius=40, fill=(56, 130, 194, 255))
    draw.ellipse([180, 155, 205, 180], fill=(255, 255, 255, 255))
    
    # Yellow bottom snake
    draw.rounded_rectangle([192, 272, 372, 392], radius=40, fill=(255, 212, 59, 255))
    draw.rounded_rectangle([272, 172, 372, 392], radius=40, fill=(255, 212, 59, 255))
    draw.ellipse([307, 332, 332, 357], fill=(30, 41, 59, 255))
    
    img.save(os.path.join(SKILLS_DIR, 'python.png'), 'PNG')
    print("Saved python.png")

def create_go_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Go Cyan tile
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(0, 173, 216, 255))
    
    # White "GO" bold text / shapes
    # G shape
    draw.rounded_rectangle([90, 150, 240, 362], radius=60, fill=(255, 255, 255, 255))
    draw.rounded_rectangle([140, 200, 200, 312], radius=30, fill=(0, 173, 216, 255))
    draw.rectangle([180, 245, 240, 290], fill=(255, 255, 255, 255))
    
    # O shape
    draw.rounded_rectangle([260, 150, 422, 362], radius=60, fill=(255, 255, 255, 255))
    draw.rounded_rectangle([310, 200, 372, 312], radius=30, fill=(0, 173, 216, 255))
    
    # Speed lines
    draw.line([(60, 180), (100, 180)], fill=(255, 255, 255, 255), width=8)
    draw.line([(40, 230), (90, 230)], fill=(255, 255, 255, 255), width=8)
    draw.line([(55, 280), (95, 280)], fill=(255, 255, 255, 255), width=8)
    
    img.save(os.path.join(SKILLS_DIR, 'go.png'), 'PNG')
    print("Saved go.png")

def create_mysql_icon():
    img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # MySQL deep slate / navy tile with orange accent
    draw.rounded_rectangle([16, 16, SIZE-16, SIZE-16], radius=90, fill=(0, 97, 138, 255))
    
    # Orange dolphin wave accent
    draw.arc([100, 80, 412, 392], start=210, end=30, fill=(234, 140, 0, 255), width=24)
    draw.ellipse([340, 140, 370, 170], fill=(234, 140, 0, 255))
    
    # "SQL" badge in white
    draw.rounded_rectangle([120, 250, 392, 360], radius=24, fill=(255, 255, 255, 255))
    draw.rectangle([130, 260, 382, 350], fill=(0, 97, 138, 255))
    
    # Draw simple SQL monogram lines
    # S
    draw.arc([160, 275, 210, 315], start=90, end=270, fill=(255, 255, 255, 255), width=6)
    draw.arc([160, 295, 210, 335], start=270, end=90, fill=(255, 255, 255, 255), width=6)
    # Q
    draw.ellipse([230, 275, 280, 335], outline=(255, 255, 255, 255), width=6)
    draw.line([(265, 315), (285, 338)], fill=(255, 255, 255, 255), width=6)
    # L
    draw.line([(310, 275), (310, 335)], fill=(255, 255, 255, 255), width=6)
    draw.line([(310, 335), (345, 335)], fill=(255, 255, 255, 255), width=6)
    
    img.save(os.path.join(SKILLS_DIR, 'mysql.png'), 'PNG')
    print("Saved mysql.png")

if __name__ == '__main__':
    create_kali_icon()
    create_burp_suite_icon()
    create_wireshark_icon()
    create_python_icon()
    create_go_icon()
    create_mysql_icon()
    print("All skill icons generated successfully!")
