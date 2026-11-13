import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def pureColors():
    zeros=np.zeros((100,100))
    ones=np.ones((100,100))
    bImges=cv.merge((zeros,255*ones,zeros))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImges)
    plt.title("blue")

    plt.show()

pureColors()
# OpenCV	BGR
# Matplotlib	RGB

# def bgrchannelGrayScale():
#     root=os.getcwd()