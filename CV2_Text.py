import cv2  # OpenCV for image processing tasks
import numpy as np  # NumPy for numerical operations

# Create a blank black image of size 700x700 pixels with 3 channels (RGB)
blank = np.zeros((700, 700, 3), dtype='uint8')

# Draw the text "AAAA" on the blank image at position (150, 150)
# Use the FONT_HERSHEY_COMPLEX font, size 1, white color (255, 255, 255), and thickness of 1
cv2.putText(blank, "AAAA", (150, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

# Draw a white rectangle around the text, from the top-left corner (150, 104) to the bottom-right corner (323, 154)
cv2.rectangle(blank, (150, 104), (323, 154), (255, 255, 255), 1)

# Display the resulting image with text and rectangle
cv2.imshow("Image with Text and Rectangle", blank)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all the windows created by OpenCV
cv2.destroyAllWindows()
