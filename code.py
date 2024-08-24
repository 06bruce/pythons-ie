import code

def generate_qr_code(data):
    """Generates a QR code image from the given data.

    Args:
        data: The data to be encoded in the QR code.

    Returns:
        The generated QR code image.
    """

    qr = code.QRCode(
        version=1,
        error_correction=code.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    qr_code_image = generate_qr_code(data)
    qr_code_image.save("qr_code.png")
    print("QR code generated and saved as qr_code.png")