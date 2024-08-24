import qrcode

def generate_qr_code(data, filename="Result.png"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="yellow")
    
    # Save the image to a file
    img.save(filename)
    print(f"qr code saved as {filename}")

# Example usage:
data = ""
generate_qr_code(data)
