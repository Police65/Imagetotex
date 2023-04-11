from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img1 = Image.open("images/img (1).jpg")
img2 = Image.open("images/img (2).jpg")
img3 = Image.open("images/img (3).jpg")
img4 = Image.open("images/img (4).jpg")
img5 = Image.open("images/img (5).jpg")
img6 = Image.open("images/img (6).jpg")
img7 = Image.open("images/img (7).jpg")
img8 = Image.open("images/img (8).jpg")
img9 = Image.open("images/img (9).jpg")

resultado = pytesseract.image_to_string(img1, lang="eng")
resultado2 = pytesseract.image_to_string(img2, lang="eng")
resultado3 = pytesseract.image_to_string(img3, lang="eng")
resultado4 = pytesseract.image_to_string(img4, lang="eng")
resultado5 = pytesseract.image_to_string(img5, lang="eng")
resultado6 = pytesseract.image_to_string(img6, lang="eng")
resultado7 = pytesseract.image_to_string(img7, lang="eng")
resultado8 = pytesseract.image_to_string(img8, lang="eng")
resultado9 = pytesseract.image_to_string(img9, lang="eng")
texto = 'PalabrasExtraidas.txt'
with open(texto, 'w') as archivo:
    archivo.write('1 FOTO') 
    archivo.write(resultado)
    archivo.write('2 FOTO')
    archivo.write(resultado2)
    archivo.write('3 FOTO')
    archivo.write(resultado3)
    archivo.write('4 FOTO')
    archivo.write(resultado4)
    archivo.write('5 FOTO')
    archivo.write(resultado5)
    archivo.write('6 FOTO')
    archivo.write(resultado6)
    archivo.write('7 FOTO')
    archivo.write(resultado7)
    archivo.write('8 FOTO')
    archivo.write(resultado8)
    archivo.write('9 FOTO')
    archivo.write(resultado9)

print(resultado)
#print(pytesseract.get_languages(config=''))