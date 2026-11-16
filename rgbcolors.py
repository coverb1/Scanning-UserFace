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

# pureColors()
# OpenCV	BGR
# Matplotlib	RGB

def bgrchannelGrayScale():
    root=os.getcwd()
    imgPath=os.path.join(root,'demoImage\\cutepic1.jpeg')
    img=cv.imread(imgPath)
    b,g,r=cv.split(img)

# Creates a new space where we can display our image.
    plt.figure()
    # This creates a layout for displaying images.
    # 1 row.
    # 3 columns.
    # 1 = first position.
    plt.subplot(131)
    plt.imshow(b)
    plt.title('b')

    plt.show()
# bgrchannelGrayScale()
def bgrchannelColor():
    root=os.getcwd()
    imgPath=os.path.join(root,'demoImage\\cutepic')
    img=cv.imread(imgPath)
    zeros=np.zeros_like(b)
    bimage=cv.merge((b,zeros,zeros))
    gimage=cv.merge((zeros,g,zeros))
    
