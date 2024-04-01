import pytesseract
import cv2
import os

def readImage(imgPath):
    img = cv2.imread(f"{imgPath}")
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img)
    print(text.replace('\n',''))
    #rename(imgPath,text)

    oldname = r'C:\Users\vitor\Documents\Algorítimos e lógica de programação Udemy\estudos_algoritimos_e_logica_de_programacao\computer-vision-tests'
    oldnameCompletePath = os.path.join(oldname,imgPath)

    path = r'C:\Users\vitor\Documents\Algorítimos e lógica de programação Udemy\estudos_algoritimos_e_logica_de_programacao\computer-vision-tests\assets'
    newName = os.path.join(path,(text.replace('\n','')))

    os.rename(oldnameCompletePath, newName + '.jpg')
    

imgPath = input('Insert image path: ')
readImage(imgPath)




