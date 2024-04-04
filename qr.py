import pyqrcode
import os
import shutil


def clear():
    os.system("cls")


clear()
title = input("Give your QR code a title ! >> ")
print()
text = input("What would you like the QR code to say >> ")
print()
input("Your qr code has been created on your deesktop")

file_name_svg = title + ".svg"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)

os.mkdir(fr"#YOUR PATH WHERE YOU WANT THE FILE\{title}")


shutil.move(file_name_svg, fr"#YOUR PATH WHERE YOU WANT THE FILE\{title}")
