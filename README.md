# QR Code Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Repo Size](https://img.shields.io/github/repo-size/selfiirawan/qr-code-generator)
![Stars](https://img.shields.io/github/stars/selfiirawan/qr-code-generator?style=social)

A beginner-friendly Python project to generate **customizable QR codes** from any URL.  
Users can create unlimited QR codes in one session and just type `no` to exit the program.  
Each QR code is saved as a `.png` file in the project folder.

> **Inspired by [Codédex](https://www.codedex.io)**
> 

The original project was simple and straightforward so I make some improvements, as suggested by the original developer.

---

## Features

- Generate QR codes from any links (Instagram, YouTube, websites, etc.)
- **Customize QR code properties**:
  - Version (1–40)
  - Box size
  - Border size
- Save QR codes as `.png` files with custom file names.
- Loop functionality: create multiple QR codes in one session without restarting the program.
- Structured and cleaner code using functions for each customization step.

---

## Demo

Here’s an example of how the program works and the QR codes it generates:

### Terminal Session

```text
Enter any website link:
https://www.youtube.com/

Enter the version of QR code (1-40)(default is 1):
2

Enter the box size (default is 5):
8

Enter the border size (default is 5):
3

Enter the name of the QR code image file (without extension):
youtube_qr

QR code generated and saved as 'youtube_qr.png'.

Do you want to generate another QR code? (yes/no):
no

Exiting the QR code generator...
Thank you!
```

### Generated QR Codes

![Example Generated QR Code](youtube_qr.png)

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/selfiirawan/qr-code-generator.git
cd qr-code-generator
```
2. **Install dependencies**
```bash
pip install qrcode[pil]
```
3. **Run the program**
```bash
python main.py
```
---
## Tech Stack
- Python 3
- qrcode library
- Pillow (PIL)
  
---

## License
```text
This project is licensed under the MIT License.
