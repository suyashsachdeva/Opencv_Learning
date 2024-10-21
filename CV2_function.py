import cv2 as cv  # OpenCV for image processing tasks

# Function to rescale an image by a given scale factor
def rescale(frame, scale=0.17):
    """
    Rescale the input frame to a specified scale factor.
    
    Args:
        frame: The input image or video frame.
        scale: The scaling factor (default is 0.17, which reduces the image size to 17% of the original).
    
    Returns:
        Resized image based on the scale factor.
    """
    width = int(frame.shape[1] * scale)  # Calculate the new width
    height = int(frame.shape[0] * scale)  # Calculate the new height
    dimension = (width, height)  # New dimensions tuple

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)  # Resize using INTER_AREA interpolation (best for shrinking)

# Path to the image file
path = r'PATH'  # Replace 'PATH' with the actual path to your image

# Read the image from the specified path
img = cv.imread(path)

# Rescale the image using the defined function
frame = rescale(img)
cv.imshow('Rescaled Image', frame)

# 1. Convert the image to grayscale
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# Uncomment below to display the grayscale image
# cv.imshow('Grayscale Image', gray)

# 2. Apply Gaussian blur to the image
blur = cv.GaussianBlur(frame, (3, 3), cv.BORDER_DEFAULT)
# Uncomment below to display the blurred image
# cv.imshow('Blurred Image', blur)

# 3. Detect edges using the Canny edge detector
canny = cv.Canny(frame, 200, 500)  # Apply Canny edge detection on the original image
cv.imshow('Canny Edges', canny)

# 3.1. Apply Canny edge detection on the blurred image to reduce noise
canny_blur = cv.Canny(blur, 125, 175)  # Use a blurred image to reduce the number of edges
# Uncomment below to display the edges of the blurred image
# cv.imshow('Canny Edges (Blurred)', canny_blur)

# 4. Dilate the edges
dilated_edges = cv.dilate(canny_blur, (3, 3), iterations=3)  # Dilate the edges from the blurred image
cv.imshow('Dilated Edges', dilated_edges)

# Dilate the original image to make it thicker with 10 iterations (exaggerates dilation effect)
dilated_image = cv.dilate(frame, (3, 3), iterations=10)
cv.imshow('Dilated Image', dilated_image)

# 5. Erode the image (reverse of dilation)
eroded_edges = cv.erode(dilated_edges, (3, 3), iterations=3)  # Erode the dilated edges to reduce thickness
# Uncomment below to display the eroded image
# cv.imshow('Eroded Image', eroded_edges)

# Another erosion example with only 1 iteration
eroded_image = cv.erode(frame, (3, 3), iterations=1)
# Uncomment below to display the eroded original image
# cv.imshow('Eroded Image (Original)', eroded_image)

# 6. Resizing the image to different sizes
# Resize the image to 600x500 pixels using INTER_AREA interpolation
resized_1 = cv.resize(img, (600, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized to 600x500', resized_1)

# Resize the image to 500x500 pixels using INTER_AREA interpolation
resized_2 = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized to 500x500', resized_2)

# Resize the image using INTER_LINEAR interpolation (faster, good quality for enlarging)
resized_linear = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized with INTER_LINEAR', resized_linear)

# Resize the image using INTER_CUBIC interpolation (slower, best quality for enlarging)
resized_cubic = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized with INTER_CUBIC', resized_cubic)

# 7. Cropping the image
# Crop a section of the image from top-left corner (0,0) to (700,500)
cropped_image = img[0:700, 0:500]
cv.imshow('Cropped Image', cropped_image)

# Wait for a key press to close all OpenCV windows
cv.waitKey(0)
cv.destroyAllWindows()
