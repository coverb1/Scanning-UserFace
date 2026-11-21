
import cv2 as cv
import os

def callback(value):
    pass

# Creates a function called averageFiltering.
def averageFiltering():

    root = os.getcwd()
    imgpath = os.path.join(root, "demoImage\\cutepic1.jpeg")

    img = cv.imread(imgpath)

    if img is None:
        print("Image not found!")
        return

    # Stores the window name.
    winName = "avg filter"

    # Creates a window.
    cv.namedWindow(winName)

    # Creates a slider.
    cv.createTrackbar('n', winName, 1, 100, callback)

    # Get image size.
    height, width, _ = img.shape

    # Resize image.
    scale = 1/4
    width = int(width * scale)
    height = int(height * scale)

    img = cv.resize(img, (width, height))

    while True:

        if cv.waitKey(1) == ord('q'):
            break

        # Get slider value.
        n = cv.getTrackbarPos('n', winName)

        # Prevent zero filter size.
        if n < 1:
            n = 1

        # Apply average filtering.
        imgFilter = cv.blur(img, (n, n))

        # Display image.
        cv.imshow(winName, imgFilter)

    cv.destroyAllWindows()

averageFiltering()
