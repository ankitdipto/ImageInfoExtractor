import cv2
import PIL
from PIL import Image
from PIL import ImageFilter


img = cv2.imread("1.jpg")
image2 = cv2.resize(img, None, fx=0.75, fy=0.75)
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)
x = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 11)


cv2.imshow('x', x)

cv2.waitKey(0)