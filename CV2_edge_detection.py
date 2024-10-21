import cv2 as cv  # OpenCV for image processing tasks
import numpy as np  # NumPy for numerical operations

# Define the path to the image file
link = r'address'  # Replace 'address' with the actual path to your image file

# Read the image from the specified path
image = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (recommended for shrinking)
resized_image = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)

# Display the resized image
cv.imshow('Original Image', resized_image)

# Convert the resized image to grayscale for edge detection
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_image)

# 1. Laplacian Edge Detection
# The Laplacian operator is used to detect edges by calculating the second derivative of the image
laplacian = cv.Laplacian(gray_image, cv.CV_64F)  # Use a 64-bit float data type to capture negative values
laplacian = np.uint8(np.absolute(laplacian))  # Convert the absolute values to unsigned 8-bit integers
cv.imshow('Laplacian', laplacian)

# 2. Sobel Edge Detection (X and Y gradients)
# Sobel operator calculates the gradient of the image intensity in both horizontal (X) and vertical (Y) directions
sobel_x = cv.Sobel(gray_image, cv.CV_64F, 1, 0)  # Sobel filter for X direction (horizontal edges)
sobel_y = cv.Sobel(gray_image, cv.CV_64F, 0, 1)  # Sobel filter for Y direction (vertical edges)

# Combine the results of Sobel X and Sobel Y using bitwise OR
sobel_combined = cv.bitwise_or(sobel_x, sobel_y)

# Display the Sobel edge detections
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel X and Y', sobel_combined)

# 3. Canny Edge Detection for Comparison
# Canny edge detector is used for edge detection by finding gradients and applying thresholds
canny_edges = cv.Canny(resized_image, 175, 150)
cv.imshow('Canny Edge Detection', canny_edges)

# Wait indefinitely for a key press before closing all OpenCV windows
cv.waitKey(0)
