import cv2 as cv  # Importing OpenCV for image processing
import numpy as np  # Importing NumPy for handling array-based operations

# Path to the image file
link = r'image_path'

# Read the image from the specified path
im = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (recommended for shrinking images)
img = cv.resize(im, (500, 500), interpolation=cv.INTER_AREA)

# Display the resized image in a window named 'image'
cv.imshow('image', img)

# Create a blank image with the same height and width as the resized image
blank = np.zeros(img.shape[:2], dtype='uint8')  # Shape[:2] gives the height and width (without channels)

# Split the image into its blue, green, and red channels
b, g, r = cv.split(img)

# Print the shapes of the original image and its individual color channels
print(f"Original image shape: {img.shape}")
print(f"Blue channel shape: {b.shape}")
print(f"Green channel shape: {g.shape}")
print(f"Red channel shape: {r.shape}")

# Merge the blue channel with two blank channels (zeros) to isolate the blue channel visually
blue = cv.merge([b, blank, blank])
cv.imshow('Blue Channel', blue)

# Merge the green channel with two blank channels to isolate the green channel visually
green = cv.merge([blank, g, blank])
cv.imshow('Green Channel', green)

# Merge the red channel with two blank channels to isolate the red channel visually
red = cv.merge([blank, blank, r])
cv.imshow('Red Channel', red)

# Merge the channels in a different order: red, blue, green (instead of the usual blue, green, red)
# This changes the color mapping, producing a visually altered image
merged = cv.merge([r, b, g])
cv.imshow('Merged Image (RBG)', merged)

# Wait indefinitely for a key press before closing the windows
cv.waitKey(0)
