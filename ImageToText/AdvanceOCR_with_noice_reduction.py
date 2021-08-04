import cv2
import pytesseract

img2 = cv2.imread("images/006.jpg") #read an image
# text = pytesseract.image_to_string(img2)
# print(text)

# resizing the image
# it's recommended if you’re working with images that have a DPI of less than 300 dpi (dots per inch)
img2= cv2.resize(img2,None, fx=.5, fy=0.5)

#convert to gray scale
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# text2= pytesseract.image_to_string(gray)
# print(text2)

#still some wroeds are wiered.lets try adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,85, 11 )

text2= pytesseract.image_to_string(adaptive_threshold)
print(text2)
