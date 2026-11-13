
import os
import cv2 as cv


# 1. Capture video from webcam
def videofromWebcam():

    # Connect to webcam
    cap = cv.VideoCapture(0)

    # Check webcam connection
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    # Keep capturing frames
    while True:

        # Capture one frame
        ret, frame = cap.read()

        # Check if frame was captured
        if not ret:
            print("Cannot receive frame")
            break

        # Display the frame
        cv.imshow("webcam", frame)

        # Press q to stop
        if cv.waitKey(1) == ord('q'):
            break

    # Release webcam
    cap.release()

    # Close windows
    cv.destroyAllWindows()


# 2. Read and play video from a file
def videoFromFIle():

    # Get current working folder
    root = os.getcwd()

    # Create video path
    videopath = os.path.join(root, 'videoImage', 'cuteVideo.mov')

    # Open video file
    cap = cv.VideoCapture(videopath)

    # Check if video opened
    if not cap.isOpened():
        print("Cannot open video")
        return

    # Keep reading frames
    while True:

        # Read one frame
        ret, frame = cap.read()

        # Check if frame was read
        if not ret:
            print("Video ended or frame could not be read")
            break

        # Display frame
        cv.imshow('video', frame)

        # Set delay
        delay = int(1000 / 60)

        # Press q to stop
        if cv.waitKey(delay) == ord('q'):
            break

    # Release video
    cap.release()

    # Close windows
    cv.destroyAllWindows()


# 3. Record webcam video and save it to a file
def writeVideToFile():

    # Connect to webcam
    cap = cv.VideoCapture(0)

    # Check webcam connection
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    # Select video codec
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    # Get current working folder
    root = os.getcwd()

    # Create output path
    outputPath = os.path.join(root, 'demoImage', 'webcams.avi')

    # Create video writer
    out = cv.VideoWriter(outputPath, fourcc, 20, (640, 480))

    # Check if video writer opened
    if not out.isOpened():
        print("Cannot create video file")
        cap.release()
        return

    # Keep recording
    while True:

        # Capture one frame
        ret, frame = cap.read()

        # Check if frame was captured
        if not ret:
            print("Cannot receive frame")
            break

        # Save frame into video
        out.write(frame)

        # Display webcam
        cv.imshow('webcam', frame)

        # Press q to stop recording
        if cv.waitKey(1) == ord('q'):
            break

    # Release webcam
    cap.release()

    # Finish saving video
    out.release()

    # Close windows
    cv.destroyAllWindows()


# Call the function you want to run

# videofromWebcam()
# videoFromFIle()
writeVideToFile()

# ret – tells you whether OpenCV successfully captured a frame.
# frame – contains the actual picture captured by the webcam.