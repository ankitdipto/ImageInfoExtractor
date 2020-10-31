from PIL import Image
from PIL import ImageFilter
import pytesseract
import requests
import cv2
import os
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"




def image_preprocess(image):
    ''' 1)resizing the image so that OCR can prepossess it in a better way
    2)converting image to grayscale one can also help us to get a better image input for OCR engine
    3)converting image to black & white will also help for better results
      we will set a threshold so that open CV will make that part of image while which is below that threshold
      and it will make the part of image black that have intensity greater than that threshold '''
    image2 = cv2.resize(image, None, fx=0.25, fy=0.25)
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    adaptive_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 75, 15)
    for i in range(0, adaptive_image.shape[0]):
        for j in range(0, adaptive_image.shape[1]):
            adaptive_image[i][j] = abs(adaptive_image[i][j] - 250)
    return adaptive_image


class OCR():

    def __init__(self, imagename):
        self.image = cv2.imread(imagename)
        #self.pre_image = image_preprocess(self.image)
        self.new_name = imagename[0:-4]+"_extracted.txt"


    def extraction(self):

        text = pytesseract.image_to_string(self.image)
        path = "C:\\Users\\DELL\\OneDrive\\Desktop\\New folder"
        fullpath = os.path.join(path, self.new_name)
        file = open(fullpath, "w")
        file.write(text)
        file.close()

