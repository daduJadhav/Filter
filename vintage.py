import cv2
import numpy as nm
from matplotlib import pyplot as py

ho = cv2.imread('fruit.jpeg')
row, cols = ho.shape[:2]

kernal_X = cv2.getGaussianKernel(cols,200) 
kernal_Y = cv2.getGaussianKernel(row,200)
kernal = kernal_X.T * kernal_Y   #  .T = .Teanspose ( like in matrix ) 

filter = 255* kernal/ nm.linalg.norm(kernal)

vintage = nm.copy(ho)

for i in range(3):
    vintage[:,:,i] = vintage[:,:,i] * filter

py.imshow(vintage)
py.show()
