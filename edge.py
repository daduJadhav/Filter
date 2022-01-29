import cv2
import matplotlib.pyplot as plt
ho = cv2.imread('flower.jpeg')
dst = cv2.Canny(ho,100,300)
plt.imshow(dst)
plt.show()