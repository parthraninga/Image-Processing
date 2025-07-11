import cv2
import numpy as np

import warnings
warnings.simplefilter('ignore')

image1_gray = cv2.imread("Resources/image/demo-image.jpg",cv2.IMREAD_GRAYSCALE)
image1_color = cv2.imread("Resources/image/demo-image.jpg",cv2.IMREAD_COLOR)

print(image1_gray.shape)

cv2.imshow("gray image",image1_gray)
cv2.imshow("color image",image1_color)

blank=np.zeros([500,375],dtype='uint8')

cv2.imshow("blank image",blank)
cv2.waitKey(0)
