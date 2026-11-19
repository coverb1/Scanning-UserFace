
import cv2 as cv
import os
import matplotlib.pyplot as plt

def imageResizing():
    root = os.getcwd()
    path = os.path.join(root, "demoImage", "cutepic1.jpeg")

    img = cv.imread(path)

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Crop the image
    img = img[286:345, 322:389, :]

    # Get image height and width
    height, width = img.shape[:2]

    # Resize to half the original size
    scale = 1 / 2

    interpMethods = [
        cv.INTER_AREA,
        cv.INTER_LINEAR,
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]

    interpTitle = [
        'area',
        'linear',
        'nearest',
        'cubic',
        'lanczos'
    ]

    plt.figure(figsize=(12, 8))

    # Display original image
    plt.subplot(2, 3, 1)
    plt.imshow(img)
    plt.title("Original")

    # Try all interpolation methods
    for i in range(len(interpMethods)):
        plt.subplot(2, 3, i + 2)

        imageResize = cv.resize(
            img,
            (int(width * scale), int(height * scale)),
            interpolation=interpMethods[i]
        )

        plt.imshow(imageResize)
        plt.title(interpTitle[i])

    plt.tight_layout()
    plt.show()


imageResizing()

# : keeps all the color channels.