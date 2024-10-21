import cv2 as cv  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations on arrays

# Create a blank black image of size 400x400 pixels
blank = np.zeros((400, 400), dtype='uint8')

# Draw a white rectangle on a copy of the blank image
# The rectangle is drawn from coordinates (30, 30) to (370, 370)
rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Draw a white circle on another copy of the blank image
# The circle is centered at (200, 200) with a radius of 200 pixels
cir = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# Display the rectangle and circle
cv.imshow('Rectangle', rect)
cv.imshow('Circle', cir)

# 1. Bitwise AND operation
# This operation keeps only the intersecting regions between the rectangle and the circle
bitand = cv.bitwise_and(rect, cir)
cv.imshow('AND', bitand)

# 2. Bitwise OR operation
# This operation keeps the union of the two shapes (both intersecting and non-intersecting areas)
bitor = cv.bitwise_or(rect, cir)
cv.imshow('OR', bitor)

# 3. Bitwise XOR operation
# XOR keeps only the non-intersecting regions of the two shapes
bitxor = cv.bitwise_xor(rect, cir)
cv.imshow('XOR', bitxor)

# 4. Bitwise NOT operation
# This inverts the rectangle image, turning black regions to white and white regions to black
bitnot = cv.bitwise_not(rect)
cv.imshow('NOT', bitnot)

# Wait indefinitely for a key press before closing the windows
cv.waitKey(0)
