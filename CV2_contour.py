import cv2 as cv  # OpenCV for image processing tasks
import numpy as np  # NumPy for numerical operations

# Define the path to the image file
image_path = r'PATH'  # Replace 'PATH' with the actual path to your image file

# Read the image from the specified path
image = cv.imread(image_path)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (recommended for shrinking)
resized_image = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)

# Create a blank image (black) with the same dimensions as the resized image
blank_image = np.zeros(resized_image.shape, dtype='uint8')

# 1. Convert the image to grayscale
# Grayscale conversion is a preprocessing step to simplify the image for contour detection
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

# 2. Apply Gaussian blur to the grayscale image to reduce noise and improve edge detection
blurred_image = cv.GaussianBlur(gray_image, (5, 5), cv.BORDER_DEFAULT)

# 3. Perform edge detection using the Canny edge detector
# The Canny edge detector is often used as a preprocessing step for contour detection
canny_edges = cv.Canny(blurred_image, 130, 255)
cv.imshow('Canny Edge Detection', canny_edges)

# 4. Apply binary thresholding
# Thresholding converts the grayscale image into a binary image, which is necessary for contour detection
_, binary_threshold = cv.threshold(gray_image, 125, 255, cv.THRESH_BINARY)
cv.imshow('Binary Thresholded Image', binary_threshold)

# 5. Find contours in the thresholded image
# Contours are useful for shape detection and recognition
# cv.findContours() returns the contours found and their hierarchy information
contours_simple, hierarchy_simple = cv.findContours(binary_threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours_simple)} contours were found using CHAIN_APPROX_SIMPLE.")

# Using a different contour approximation method (CHAIN_APPROX_NONE)
contours_none, hierarchy_none = cv.findContours(binary_threshold, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours_none)} contours were found using CHAIN_APPROX_NONE.")

# 6. Draw the detected contours on the blank image
# Draw the contours in red (color = (0, 0, 255)) with a thickness of 1 pixel
cv.drawContours(blank_image, contours_simple, -1, (0, 0, 255), 1)

# Display the image with drawn contours
cv.imshow('Contours Drawn on Blank Image', blank_image)

# Wait indefinitely for a key press before closing all OpenCV windows
cv.waitKey(0)
