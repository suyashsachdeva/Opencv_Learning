import cv2 as cv

# Path to the image file
link = r'PATH'

# Load the image from the specified path
im = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation, which is recommended for shrinking images
img = cv.resize(im, (500, 500), interpolation=cv.INTER_AREA)

# Display the original resized image in a window named 'image'
cv.imshow('image', img)

# 1. Averaging Blur Effect
# Averaging blur works by averaging the pixel values in the kernel area and replacing the central pixel with this averaged value.
# The kernel size (5x5) determines the size of the window that slides across the image.
avg = cv.blur(img, (5, 5))  # The larger the kernel size, the stronger the blur effect.
cv.imshow('Average', avg)    # Display the averaged blur effect in a window named 'Average'

# 2. Gaussian Blur Effect
# Gaussian blur gives more weight to the central pixels by applying a Gaussian function (bell curve) to the pixel values.
# The kernel size (5x5) and sigma (10) control the strength and shape of the blur.
gsb = cv.GaussianBlur(img, (5, 5), 10)  # A higher sigma results in a stronger blur.
cv.imshow('Gaussian', gsb)              # Display the Gaussian blur effect

# Gaussian blur with sigma = 0 (automatically determined based on the kernel size)
gsb1 = cv.GaussianBlur(img, (5, 5), 0)  # A sigma of 0 means the function will calculate the value automatically.
cv.imshow('Gaussian1', gsb1)            # Display the Gaussian blur with automatic sigma

# 3. Median Blur Effect
# Median blur is a non-linear filter. It replaces the central pixel with the median value in the kernel area, which reduces noise.
# This is particularly effective for salt-and-pepper noise.
median = cv.medianBlur(img, 5)  # Kernel size of 5; it must be an odd number.
cv.imshow('Median', median)     # Display the median blur effect

# 4. Bilateral Filter
# Bilateral filter reduces noise while keeping edges sharp. It applies Gaussian blur in both space and color intensity.
# Parameters: diameter of the pixel neighborhood (50), sigmaColor (150), sigmaSpace (150).
# Larger sigmaColor means that more colors in the neighborhood will be mixed together.
bil = cv.bilateralFilter(img, 50, 150, 150)  # Bilateral filter with a high spatial and color distance
cv.imshow('Bilateral', bil)                  # Display the bilateral filter effect

# Wait indefinitely for a key press, then close all windows
cv.waitKey(0)
cv.destroyAllWindows()
