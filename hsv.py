import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvcolorsegmentation():
    root=os.getcwd()
    imgpath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgpath)
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow('mask',mask)
    cv.waitKey(0)
    cv.destroyAllWindows()
    hsvcolorsegmentation()

    # What does cv.inRange()
    # If the pixel is inside your selected range, it becomes white (255).
    # If the pixel is outside your selected range, it becomes black (0).