import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
filename = 'Image.png'
last_time = time.time()
while (True):
    screen = np.array(ImageGrab.grab(bbox=(581, 708, 992, 771)))
    last_time = time.time()
    cv2.imwrite(filename, screen)
    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img, lang='eng+rus')
    if text.find('♀') >= 0:
        continue
    if len(text.strip()) > 0:
        print(text)

cv2.destroyAllWindows()