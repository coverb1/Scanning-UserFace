import cv2 as cv
import os 
import matplotlib.pyplot as plt
import numpy as np

def readingImage():
    # It gets the location of the folder where your Python program is currently running.
    root=os.getcwd()
    # It joins two folder or file locations together.
    imgpath = os.path.join(root, 'demoImage', 'cutepic1.jpeg')
    # This displays your image on the computer screen.
    img=cv.imread(imgpath)
    debug=1
    cv.imshow('img',img)
    # This tells OpenCV to wait for you to press a keyboard key before closing the image window.
    cv.waitKey(0)

def writeImage():
    root = os.getcwd()

    # Read original image
    imgpath = os.path.join(root, 'demoImage', 'cutepic1.jpeg')
    img = cv.imread(imgpath)

    # Check if image was read
    if img is None:
        print("Image not found!")
        return

    # Save as a new image
    outpath = os.path.join(root, 'demoImage', 'newImage1.jpeg')

    success = cv.imwrite(outpath, img)

    if success:
        print("Image saved successfully!")
    else:
        print("Image could not be saved!")

writeImage()
