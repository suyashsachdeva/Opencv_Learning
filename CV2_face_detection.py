import cv2  # OpenCV for image and video processing
import os  # OS module for working with file paths
import numpy as np  # NumPy for numerical operations

# Path to the Haar Cascade XML file for face detection
loc = r'../haarcascade_frontalface_default.xml'  # Replace with the actual path if needed

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(loc)

# Start video capture from the default camera (0 refers to the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    _, frame = cap.read()

    # Convert the captured frame to grayscale for the face detection algorithm
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using the detectMultiScale method
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

    # Loop through all the detected faces and draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)  # Draw rectangle in blue color (BGR)

    # Display the frame with detected faces
    cv2.imshow("Face Detection", frame)

    # Break the loop when 'Esc' key (ASCII 27) is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
