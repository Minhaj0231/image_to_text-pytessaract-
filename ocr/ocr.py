from PIL import Image

import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'  # Add path where tesseract is installed in computer


print("ok")

fileDict = {}

def imgToString(filename):
    """
    This function will handle the core OCR processing of images.
    """
    path = "images/{}".format(filename)
    text = pytesseract.image_to_string(Image.open(path))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# print(imgToString('images/ss2.png'))
