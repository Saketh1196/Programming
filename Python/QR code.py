import pyqrcode
from pyqrcode import QRCode
s= str(input("Enter the url for the website to create QR Code: "))
## Generates QR code for the link provided
url= pyqrcode.create(s)
## Creates and save the QR code as svg file
url.svg("QRCode.svg",scale=6)
