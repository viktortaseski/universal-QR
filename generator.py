import qrcode

URL = "https://www.facebook.com"  # 🔗 Change URL here
OUTPUT_FILE = "qr.png"


qr_img = qrcode.make(URL)


qr_img.save(OUTPUT_FILE)
print(f"Saved as {OUTPUT_FILE}")
