import cv2
import numpy

import warnings
warnings.simplefilter('ignore')

image1_gray = cv2.imread("Resources/image/demo-image.jpg",cv2.IMREAD_GRAYSCALE)
image1_color = cv2.imread("Resources/image/demo-image.jpg",cv2.IMREAD_COLOR)

cv2.imshow("gray image",image1_gray)
cv2.imshow("color image",image1_color)

cv2.waitKey(0)