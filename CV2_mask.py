import cv2 as cv  # OpenCV for image processing tasks
import numpy as np  # NumPy for numerical operations

# Path to the image file
link = r'PATH'  # Replace 'PATH' with the actual path to your image file

# Read the image from the specified path
im = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (recommended for shrinking)
img = cv.resize(im, (500, 500), interpolation=cv.INTER_AREA)

# Display the resized image in a window titled 'image'
cv.imshow('Image', img)

# Create a blank mask (single-channel, black image) with the same dimensions as the image
blank = np.zeros(img.shape[:2], dtype='uint8')

# 1. Circular Mask
# Create a circular mask with a radius of 125 pixels at the center of the image
mask = cv.circle(blank.copy(), (img.shape[1] // 2, img.shape[0] // 2), 125, 255, thickness=-1)

# Display the circular mask
cv.imshow('Circular Mask', mask)

# 2. Rectangular Mask
# Create a rectangular mask from coordinates (200, 200) to (380, 380)
mask1 = cv.rectangle(blank.copy(), (200, 200), (380, 380), 255, thickness=-1)

# Display the rectangular mask
cv.imshow('Rectangular Mask', mask1)

# 3. Combined Mask
# Perform a bitwise AND operation between the circular and rectangular masks
maskCom = cv.bitwise_and(mask, mask1)

# Display the combined mask (intersection of circle and rectangle)
cv.imshow('Combined Mask', maskCom)

# Apply the combined mask to the original image using bitwise AND
maskedCom = cv.bitwise_and(img, img, mask=maskCom)

# Display the masked image (with the combined circular and rectangular mask)
cv.imshow('Masked Image with Combined Mask', maskedCom)

# Wait indefinitely for a key press before closing all OpenCV windows
cv.waitKey(0)
