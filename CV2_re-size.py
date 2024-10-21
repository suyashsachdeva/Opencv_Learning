import cv2 as cv  # Importing OpenCV library for image processing tasks

# Function to rescale the frame by a specified scale factor
def rescale(frame, scale=0.75):
    """
    Resizes the given frame by a specified scale factor.

    Args:
        frame: The image or video frame to be resized.
        scale: Scaling factor. Default is 0.75 (i.e., 75% of the original size).

    Returns:
        Resized frame using the specified scale.
    """
    width = int(frame.shape[1] * scale)  # Calculate the new width
    height = int(frame.shape[0] * scale)  # Calculate the new height
    dimension = (width, height)  # Combine width and height into a dimension tuple

    # Resize the frame with INTER_AREA interpolation (best for shrinking)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# Capture video from the default camera (0 refers to the default webcam)
cap = cv.VideoCapture(0)

# Infinite loop to continuously capture video frames from the webcam
while True:
    # Read the frame from the video capture object
    isTrue, frame = cap.read()

    if not isTrue:
        print("Failed to capture frame from camera. Exiting...")
        break

    # Rescale the captured frame using the rescale function
    frame_resized = rescale(frame)

    # Display the resized frame in a window titled 'resize'
    cv.imshow('Resized Frame', frame_resized)

    # Wait for a key press and exit loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):  # Corrected condition for key press check
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
