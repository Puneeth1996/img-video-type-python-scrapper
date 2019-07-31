import pytesseract
from PIL import Image

img = Image.open("new.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
text = pytesseract.image_to_string(img)
print(text)