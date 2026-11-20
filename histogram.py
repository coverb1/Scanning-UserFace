import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt
import os

def grayHistogram():
    root=os.getcwd()
    imgPath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img,cmap='gray')

    hist=cv.calcHist([img],[0],None,[256],[0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel("# of pixel")

    plt.show()

grayHistogram()