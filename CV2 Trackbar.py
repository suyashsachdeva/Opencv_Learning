import cv2  # OpenCV for image and video processing
import numpy as np  # NumPy for numerical operations

# Define a dummy callback function for the trackbar
def nothing():
    pass

# Start video capture from the default webcam
cap = cv2.VideoCapture(0)

# Create a window where the trackbar will be placed
cv2.namedWindow("frame")

# Create a trackbar named "test" in the window "frame" with an initial value of 50 and a range of 0 to 500
cv2.createTrackbar("test", "frame", 50, 500, nothing)

# Create a trackbar named "color" in the window "frame" to switch between color and grayscale mode (0 for color, 1 for grayscale)
cv2.createTrackbar("color", "frame", 0, 1, nothing)

# Start an infinite loop to process the video frames in real-time
while True:
    # Read the frame from the webcam
    _, frame = cap.read()

    # Get the current position of the "test" trackbar
    test_value = cv2.getTrackbarPos("test", "frame")

    # Get the current position of the "color" trackbar (0 for color, 1 for grayscale)
    color_switch = cv2.getTrackbarPos("color", "frame")

    # Display the value of the "test" trackbar as text on the video frame
    cv2.putText(frame, str(test_value), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), 2)

    # If the "color" trackbar is set to 1, convert the frame to grayscale
    if color_switch == 0:
        pass  # Keep the frame in color
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale

    # Display the frame in the "frame" window
    cv2.imshow("frame", frame)

    # Check if the 'Esc' key (ASCII 27) is pressed, if so, break the loop and exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
