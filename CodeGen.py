import code
from PIL import Image

def generate_qr_code(data, filename="qrcode.png", box_size=10, border=4):
    try:
        # Create a QRCode object with error correction
        qr = code.QRCode(
            version=1,
            error_correction=code.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        
        # Add data to the QRCode object
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QRCode instance
        img = qr.make_image(fill='black', back_color='white')
        
        # Save the generated image
        img.save(filename)
        print(f"QR code generated and saved as {filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
data = "https://www.example.com"
generate_qr_code(data, "example_qrcode.png")
