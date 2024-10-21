import cv2 as cv  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations

# Path to the image file
link = r'PATH'  # Replace 'PATH' with the actual path to your image

# Read the image from the specified path
image = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation
resized_image = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Original Image', resized_image)

# 1. Translation (Shifting the image in different directions)
def translate(img, x, y):
    """
    Translate the image by shifting it along the x and y axes.

    Args:
        img: The input image.
        x: Shift along the x-axis (positive values shift right, negative shift left).
        y: Shift along the y-axis (positive values shift down, negative shift up).
    
    Returns:
        Translated image.
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # Transformation matrix for translation
    dimensions = (img.shape[1], img.shape[0])  # Dimensions of the translated image
    return cv.warpAffine(img, transMat, dimensions)

# Translation: Shift image to the left by 100 pixels
translated_image = translate(resized_image, -100, 0)
# Uncomment to display the translated image
# cv.imshow('Translated Image', translated_image)

"""
Translation directions:
-x --> Left
-y --> Up
x  --> Right
y  --> Down
"""

# 2. Rotation of Image
def rotate(img, angle, rot_point=None):
    """
    Rotate the image around a given point.

    Args:
        img: The input image.
        angle: Angle of rotation (in degrees).
        rot_point: The point around which the image will be rotated. If None, rotates around the center.
    
    Returns:
        Rotated image.
    """
    (height, width) = img.shape[:2]  # Get image dimensions
    if rot_point is None:
        rot_point = (width // 2, height // 2)  # Default rotation point is the center

    rot_matrix = cv.getRotationMatrix2D(rot_point, angle, 1.0)  # Get the rotation matrix
    dimensions = (width, height)  # Dimensions of the rotated image
    return cv.warpAffine(img, rot_matrix, dimensions)

# Rotate the image by 45 degrees around its center
rotated_image = rotate(resized_image, 45)
# Uncomment to display the rotated image
# cv.imshow('Rotated Image', rotated_image)

# 3. Resizing the Image
resized_image_2 = cv.resize(resized_image, (250, 250), interpolation=cv.INTER_AREA)
# Uncomment to display the resized image
# cv.imshow('Resized Image (250x250)', resized_image_2)

# 4. Flipping the Image
# Flip horizontally (axis=1)
flipped_horizontal = cv.flip(resized_image, 1)
# Uncomment to display the horizontally flipped image
# cv.imshow('Flipped Horizontally', flipped_horizontal)

# Flip vertically (axis=0)
flipped_vertical = cv.flip(resized_image, 0)
# Uncomment to display the vertically flipped image
# cv.imshow('Flipped Vertically', flipped_vertical)

# Flip both horizontally and vertically (axis=-1)
flipped_both = cv.flip(resized_image, -1)
# Uncomment to display the flipped image (both horizontally and vertically)
# cv.imshow('Flipped Both', flipped_both)

# 5. Cropping the Image
# Crop the image by selecting a region of interest (200:400 in y-axis and 0:100 in x-axis)
cropped_image = resized_image[200:400, 0:100]
# Display the cropped image
cv.imshow('Cropped Image', cropped_image)

# Wait for a key press to close the OpenCV windows
cv.waitKey(0)
cv.destroyAllWindows()
