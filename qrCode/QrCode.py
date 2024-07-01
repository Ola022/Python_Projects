import pyqrcode

import qrCode


""" [ pip install PyQRCode, pip install pypng ] 
"""

url =  input("Enter a URL to generate QR Code:\n")

QR = pyqrcode.create(url)

QR.png("webqr.png", scale=8)