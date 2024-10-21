import cv2 as cv  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations on arrays
import matplotlib.pyplot as plt  # Matplotlib for plotting histograms

# Path to the image file
link = r'PATH'  # Replace 'PATH' with the actual path to your image

# Read the image from the specified path
im = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (best for shrinking)
img = cv.resize(im, (500, 500), interpolation=cv.INTER_AREA)

# Create a blank mask with the same height and width as the image (single channel)
blank = np.zeros(img.shape[:2], dtype='uint8')

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the grayscale image
cv.imshow('Grayscale Image', gray)

# Create a circular mask with a radius of 100 pixels at the center of the image
circle = cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100, 255, thickness=-1)

# Apply the circular mask to the grayscale image using bitwise AND
masked = cv.bitwise_and(gray, gray, mask=circle)

# Display the masked grayscale image
cv.imshow('Masked Grayscale Image', masked)

# 1. Grayscale Histogram
# Calculate the histogram for the masked grayscale image (single channel)
gray_hist = cv.calcHist([masked], [0], None, [256], [0, 256])

# Plot the grayscale histogram using Matplotlib
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')  # X-axis label
plt.ylabel('Number of Pixels')  # Y-axis label
plt.plot(gray_hist)
plt.xlim([0, 256])  # Set x-axis limits to cover all pixel values from 0 to 255

# 2. Color Histogram
# Calculate and plot the histogram for each color channel (blue, green, red)
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    # Calculate the histogram for each color channel with the circular mask applied
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    # Plot the histogram for the respective color
    plt.plot(hist, color=col)

# Display the color histograms
plt.title('Color Histogram')
plt.xlabel('Bins')  # X-axis label
plt.ylabel('Number of Pixels')  # Y-axis label
plt.xlim([0, 256])  # Set x-axis limits to cover all pixel values from 0 to 255

# Show all the plots
plt.show()

# Wait for a key press to close all OpenCV windows
cv.waitKey(0)
