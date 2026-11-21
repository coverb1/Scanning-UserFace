import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def convulution():
    root=os.getcwd()
    imgPath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgPath)
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

# we create a variable called
# We will use this value to create our kernel.
    n=100
    kernel=np.ones((n,n),np.float32)/(n*n)
    imgFilter=cv.filter2D(imgRGB,-1,kernel)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)

    plt.subplot(121)
    plt.imshow(imgFilter)

    plt.show()

convulution()