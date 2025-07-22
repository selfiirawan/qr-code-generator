import qrcode

while True:
    # add any link you want to generate a QR code for 
    website_link = input("Enter any website link:\n")

    # customize the QR code
    # choose own version, box size, and border size
    ver = input("\nEnter the version of QR code (1-40):\n")
    if ver.isdigit() and 1 <= int(ver) <= 40:
        ver = int(ver)
    else:
        print("Invalid version. Using default version 1.")
        ver = 1

    b_size = input("\nEnter the box size (default is 5):\n")
    if b_size.isdigit():
        b_size = int(b_size)
    else:
        print("Invalid box size. Using default box size 5.")
        b_size = 5

    border = input("\nEnter the border size (default is 5):\n") 
    if border.isdigit():
        border = int(border)
    else:   
        print("Invalid border size. Using default border size 5.")
        border = 5

    qr = qrcode.QRCode(version = ver, box_size = b_size, border = border)
    qr.add_data(website_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qr_result.png")
    break
