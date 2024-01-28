import pyqrcode
import os
import shutil

title = input("Give your QR code a title ! >> ")
text = input("What would you like the QR code to say >> ")

file_name_svg = title + ".svg"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)

os.mkdir(fr"c:\Users\Cyril_\Desktop\{title}")


shutil.move(file_name_svg, fr"c:\Users\Cyril_\Desktop\{title}")
