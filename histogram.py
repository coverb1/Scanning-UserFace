import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt
import os

def grayHistogram():
    root=os.getcwd()
    imgPath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    # cv.imread() means read an image. // cv.IMREAD_GRAYSCALE tells OpenCV to read the image in grayscale.
    # Grayscale means the image contains shades of gray, from black to white.
    img=cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure()

    # plt.imshow() means display an image.
    # cmap='gray' tells Matplotlib to use a grayscale color map.
    plt.imshow(img,cmap='gray')

# We are asking OpenCV to calculate how many pixels have each brightness value.
# Since your image is grayscale, it has only one channel, and its index is 0
    hist=cv.calcHist([img],[0],None,[256],[0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel('bins')
    plt.ylabel("# of pixel")

    plt.show()

grayHistogram()