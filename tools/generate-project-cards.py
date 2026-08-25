"""
Generate three project/polaroid artworks in public/assets/projects/
representing Farhaan's key cybersecurity projects and security research:
1. Smart QR Inspector (Android QR Security & Threat Detection)
2. AutoBB (Automated Bug Bounty CLI Pipeline in Go)
3. Security Lab & Ethical Hacking Research
"""
import os
from PIL import Image, ImageDraw, ImageFont

PROJECTS_DIR = 'public/assets/projects'
os.makedirs(PROJECTS_DIR, exist_ok=True)

W, H = 1000, 806  # ~1.24 landscape ratio

def draw_smart_qr_inspector():
    img = Image.new('RGB', (W, H), (18, 20, 24))
    draw = ImageDraw.Draw(img)
    
    # Grid lines
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(28, 32, 40), width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(28, 32, 40), width=1)
        
    # App Frame / Holographic Scanner
    draw.rounded_rectangle([180, 80, W-180, H-80], radius=24, fill=(12, 14, 18), outline=(56, 189, 248), width=3)
    
    # Scanner HUD Corner brackets
    # Top Left
    draw.line([(220, 140), (300, 140)], fill=(56, 189, 248), width=6)
    draw.line([(220, 140), (220, 220)], fill=(56, 189, 248), width=6)
    # Top Right
    draw.line([(W-220, 140), (W-300, 140)], fill=(56, 189, 248), width=6)
    draw.line([(W-220, 140), (W-220, 220)], fill=(56, 189, 248), width=6)
    # Bottom Left
    draw.line([(220, H-140), (300, H-140)], fill=(56, 189, 248), width=6)
    draw.line([(220, H-140), (220, H-220)], fill=(56, 189, 248), width=6)
    # Bottom Right
    draw.line([(W-220, H-140), (W-300, H-140)], fill=(56, 189, 248), width=6)
    draw.line([(W-220, H-140), (W-220, H-220)], fill=(56, 189, 248), width=6)
    
    # QR stylized modules in center
    draw.rounded_rectangle([W//2 - 130, H//2 - 130, W//2 + 130, H//2 + 130], radius=16, fill=(24, 28, 36))
    draw.rectangle([W//2 - 100, H//2 - 100, W//2 - 40, H//2 - 40], outline=(235, 25, 38), width=6)
    draw.rectangle([W//2 + 40, H//2 - 100, W//2 + 100, H//2 - 40], outline=(235, 25, 38), width=6)
    draw.rectangle([W//2 - 100, H//2 + 40, W//2 - 40, H//2 + 100], outline=(235, 25, 38), width=6)
    draw.rectangle([W//2 - 10, H//2 - 10, W//2 + 10, H//2 + 10], fill=(56, 189, 248))
    
    # Laser Scan line
    draw.line([(200, H//2), (W-200, H//2)], fill=(235, 25, 38), width=4)
    
    # Security tags
    draw.text((W//2, 115), "[ SMART QR INSPECTOR // REAL-TIME THREAT RADAR ]", fill=(56, 189, 248), anchor="mm")
    draw.text((W//2, H-110), "VIRUSTOTAL  *  GOOGLE SAFE BROWSING  *  URLHAUS  *  UPI DEFENSE", fill=(200, 210, 220), anchor="mm")
    
    img.save(os.path.join(PROJECTS_DIR, 'studio-01.webp'), quality=92)
    print("Saved studio-01.webp")

def draw_autobb_cli():
    img = Image.new('RGB', (W, H), (14, 16, 20))
    draw = ImageDraw.Draw(img)
    
    # Terminal Window Header
    draw.rounded_rectangle([80, 70, W-80, H-70], radius=18, fill=(8, 10, 14), outline=(40, 45, 55), width=2)
    draw.rectangle([80, 70, W-80, 130], fill=(22, 26, 34))
    
    # Window controls
    draw.ellipse([110, 95, 126, 111], fill=(239, 68, 68))
    draw.ellipse([140, 95, 156, 111], fill=(245, 158, 11))
    draw.ellipse([170, 95, 186, 111], fill=(34, 197, 94))
    draw.text((W//2, 103), "bash - autobb --target enterprise-scope.com", fill=(148, 163, 184), anchor="mm")
    
    # Terminal Lines
    lines = [
        ("> AutoBB v2.4 // Automated Bug Bounty Pipeline [Golang]", (56, 189, 248)),
        ("[+] Initializing multi-source OSINT recon: crt.sh, Shodan, SecurityTrails", (148, 163, 184)),
        ("[*] Discovered 148 alive subdomains across target infrastructure", (34, 197, 94)),
        ("[*] Running vulnerability engines: XSS, SQLi, SSRF, IDOR, CORS, Headers", (148, 163, 184)),
        ("[!] High Vulnerability Detected: SSRF endpoint verified at /api/v1/fetch", (239, 68, 68)),
        ("[+] Nuclei template scan completed. Deduplicating findings...", (245, 158, 11)),
        ("[+] Report exported: output_audit.html | audit.json | summary.md", (56, 189, 248)),
        ("root@farhaan-sec:~$ _", (248, 250, 252))
    ]
    
    y_pos = 170
    for text, color in lines:
        draw.text((120, y_pos), text, fill=color)
        y_pos += 60
        
    img.save(os.path.join(PROJECTS_DIR, 'studio-02.webp'), quality=92)
    print("Saved studio-02.webp")

def draw_security_research():
    img = Image.new('RGB', (W, H), (16, 20, 26))
    draw = ImageDraw.Draw(img)
    
    # Network Security / Traffic Packet Visualization
    for i in range(12):
        y = 120 + i * 48
        draw.line([(100, y), (W-100, y)], fill=(28, 36, 48), width=1)
        draw.text((120, y - 10), f"PACKET #0{1420 + i*3}  SRC: 192.168.1.{10+i}  DST: GATEWAY  TCP/TLS", fill=(100, 116, 139))
    
    # Center Cyber Shield / Certification Badge
    draw.rounded_rectangle([W//2 - 180, H//2 - 170, W//2 + 180, H//2 + 170], radius=24, fill=(15, 23, 42), outline=(56, 189, 248), width=3)
    
    # Shield Polygon
    shield = [
        (W//2, H//2 - 110), (W//2 + 110, H//2 - 60), (W//2 + 90, H//2 + 50),
        (W//2, H//2 + 110), (W//2 - 90, H//2 + 50), (W//2 - 110, H//2 - 60),
        (W//2, H//2 - 110)
    ]
    draw.polygon(shield, fill=(30, 58, 138, 200), outline=(56, 189, 248))
    
    # Keyhole or Bug icon in center
    draw.ellipse([W//2 - 20, H//2 - 30, W//2 + 20, H//2 + 10], fill=(235, 25, 38))
    draw.polygon([(W//2 - 15, H//2 - 5), (W//2 + 15, H//2 - 5), (W//2 + 24, H//2 + 40), (W//2 - 24, H//2 + 40)], fill=(235, 25, 38))
    
    draw.text((W//2, H//2 + 130), "ETHICAL HACKING & TRAFFIC AUDIT", fill=(240, 246, 252), anchor="mm")
    draw.text((W//2, H - 70), "PROMPT INFOTECH  *  TRYHACKME 2025  *  CAPPRICIOSEC BOOTCAMP", fill=(56, 189, 248), anchor="mm")
    
    img.save(os.path.join(PROJECTS_DIR, 'studio-03.webp'), quality=92)
    print("Saved studio-03.webp")

if __name__ == '__main__':
    draw_smart_qr_inspector()
    draw_autobb_cli()
    draw_security_research()
    print("All project artworks generated successfully!")
