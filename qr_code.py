import qrcode

def code_version():
    ver = input("\nEnter the version of QR code (1-40)(default is 1):\n")
    if ver.isdigit() and 1 <= int(ver) <= 40:
        ver = int(ver)
    else:
        print("Invalid version. Using default version 1.")
        ver = 1
    return ver

def box_size():
    b_size = input("\nEnter the box size (default is 5):\n")
    if b_size.isdigit():
        b_size = int(b_size)
    else:
        print("Invalid box size. Using default box size 5.")
        b_size = 5
    return b_size

def border_size():
    border = input("\nEnter the border size (default is 5):\n") 
    if border.isdigit():
        border = int(border)
    else:   
        print("Invalid border size. Using default border size 5.")
        border = 5
    return border

def main():
    while True:
        # add any link you want to generate a QR code for 
        website_link = input("Enter any website link:\n")

        # customize the QR code
        # choose own version, box size, and border size
        ver = code_version()
        b_size = box_size()
        border = border_size()

        qr = qrcode.QRCode(version = ver, box_size = b_size, border = border)
        qr.add_data(website_link)
        qr.make(fit=True)

        img = qr.make_image(fill_color = "black", back_color = "white")

        qr_name = input("\nEnter the name of the QR code image file (without extension):\n")
        if not qr_name:
            qr_name = "qr_code"

        img.save(f"{qr_name}.png")
        print(f"\nQR code generated and saved as '{qr_name}.png'.")

        # creating multiple QR codes
        cont = input("\nDo you want to generate another QR code? (yes/no):\n").strip().lower()
        if cont != 'yes':
            print("Exiting the QR code generator.")
            break
        print("\n" + "="*50 + "\n")
        print("Generating a new QR code...\n")

main()
