import cv2 as cv
import os
import matplotlib.pyplot as plt

def  readAndWriteSinglePixels():
     root=os.getcwd()
     imgpath=os.path.join(root,'demoImage\\cutepic1.jpeg')
     img=cv.imread(imgpath)
    #  we are here converting image from bgr2rgb
     imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

     eyepixel=imgRGB[214,272]
     imgRGB[214,272]=(255,0,0)

def readAndWritePixelRegion():
     root=os.getcwd()
     imgpath=os.path.join(root,"demoImage\\cutepic1.jpeg")
     img=cv.imread(imgpath)
     imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)

     plt.figure()
     plt.imshow(imgRGB)
     plt.show()
readAndWriteSinglePixels()