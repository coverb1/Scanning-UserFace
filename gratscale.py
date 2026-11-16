import cv2 as cv
import os

def grayscale():
    root=os.getcwd()
    imgpath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",imgGray)
    cv.waitKey(0)

grayscale()