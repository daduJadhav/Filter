import cv2
import matplotlib.pyplot as plt
ho = cv2.imread('house.jpeg')
dst = cv2.GaussianBlur(ho,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(dst)
plt.show()