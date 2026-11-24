import qrcode


qr = qrcode.QRCode(
    version=1,  # Controls size (1 is 21x21, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (30%)
    box_size=10,  # Pixels per box
    border=4,  # Thickness of the white border
)

qr.add_data("https://goggle.com")
qr.make(fit=True)

img = qr.make_image(fill_color="navy", back_color="white")
img.save("custom_qrcode.png")
