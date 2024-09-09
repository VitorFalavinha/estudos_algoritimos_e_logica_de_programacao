import pytesseract
import cv2
import os
import re

def readImage(imgPath):
    if not os.path.exists(imgPath):
        print("Arquivo não encontrado!")
        return

    img = cv2.imread(imgPath)
    pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img)
    valid_text = re.sub(r'[^\w\-_\. ]', '', text)  # Limpa caracteres especiais
    print(valid_text.replace('\n',''))
    
    oldnameCompletePath = os.path.abspath(imgPath)

    path = r'C:\Users\vitor\OneDrive\Documentos\Algorítimos e lógica de programação Udemy\estudos_algoritimos_e_logica_de_programacao\computer-vision-tests\assets'
    newName = os.path.join(path, valid_text)

    os.rename(oldnameCompletePath, newName + '.jpg')
    

imgPath = input("Digite o caminho da imagem: ")
readImage(imgPath)




