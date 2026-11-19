import cv2 as cv
import os

def grayscale():
    root=os.getcwd()
    imgpath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgpath)
    imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",imgGray)
    cv.waitKey(0)

def readGray():
    root=os.getcwd()
    imgPath=os.path.join(root,"demoImage\\cutepic1.jpeg")
    img=cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    cv.imshow("gray",img)
    cv.waitKey(0)

readGray()

# //Use cvIMREAD_GRAYSCALE when you only need a grayscale image.
# Use cv.cvtColor() when you first need to read the image in color and then convert it later.1