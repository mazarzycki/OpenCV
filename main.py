import cv2
import random

img = cv2.imread('assets/logo.jpg', 1)
img = cv2.resize(img, (0,0), fx=2, fy=2)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#Copy part of image
tag = img[500:700, 300:500]

#Paste part of image
img[100:300, 200:400] = tag

cv2.imshow('Corinthians', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
