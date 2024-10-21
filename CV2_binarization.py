import cv2 as cv  # Importing OpenCV for image processing tasks

# Define the path to the image file
link = r'PATH'  # Replace 'PATH' with the actual path to your image file

# Read the image from the specified path
im = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation (ideal for shrinking)
img = cv.resize(im, (500, 500), interpolation=cv.INTER_AREA)

# Display the resized image in a window titled 'image'
cv.imshow('image', img)

# Convert the resized image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the grayscale version of the image
cv.imshow('gray', gray)

# 1. Simple Thresholding
# Perform binary thresholding: pixels above 100 are set to 255 (white), others are set to 0 (black)
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

# Display the result of simple thresholding
cv.imshow('Simple Thresholded', thresh)

# Print the threshold value (100 in this case)
print(f"Threshold value used: {threshold}")

# 2. Inverse Thresholding
# Perform binary inverse thresholding: pixels below 50 are set to 255 (white), others are set to 0 (black)
threshold, threshinv = cv.threshold(gray, 50, 255, cv.THRESH_BINARY_INV)

# Display the result of inverse thresholding
cv.imshow('Simple Thresholded Inverse', threshinv)

# 3. Adaptive Thresholding (Mean Method)
# Adaptive thresholding using the mean of the neighborhood pixel values
# Block size is 17, C is the constant subtracted from the mean
adap = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 15)

# Display the result of adaptive mean thresholding
cv.imshow('Adaptive Thresholding (Mean)', adap)

# 4. Adaptive Thresholding (Gaussian Method)
# Adaptive thresholding using the weighted sum of the neighborhood pixel values (Gaussian)
adap_gau = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 15)

# Display the result of adaptive Gaussian thresholding
cv.imshow('Adaptive Thresholding (Gaussian)', adap_gau)

# Wait indefinitely for a key press before closing the windows
cv.waitKey(0)
