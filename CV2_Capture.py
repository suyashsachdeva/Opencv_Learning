import cv2  # OpenCV library for computer vision tasks
import numpy as np  # NumPy library for numerical operations (not used directly here but often useful in image processing)

# Open the default camera (device index 0) for video capture
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Infinite loop to continuously capture frames from the camera
while True:
    # ret: Boolean indicating if the frame was captured successfully
    # frame: The current frame from the video capture (the image)
    ret, frame = cap.read()

    if not ret:
        print("Error: Frame could not be captured.")
        break

    # Display the frame in a window titled 'frame'
    cv2.imshow('frame', frame)

    # Wait for 1 millisecond and check if 'q' is pressed to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object to free the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
