import cv2 as cv  # OpenCV for image processing

# Path to the image file
link = r'PATH'  # Replace 'PATH' with the actual path to your image

# Read the image from the specified path
image = cv.imread(link)

# Resize the image to 500x500 pixels using INTER_AREA interpolation
resized_image = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Original Image', resized_image)

# Convert the image to grayscale for face detection
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_image)

# Load the Haar Cascade Classifier for face detection (make sure the XML file is in the correct path)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Detect faces in the grayscale image
# `scaleFactor` specifies how much the image size is reduced at each scale. 
# `minNeighbors` specifies how many neighbors each rectangle should have to retain it.
face_rectangles = haar_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3)

# Print the number of faces detected
print(f"Number of faces detected: {len(face_rectangles)}")

# Loop through the detected faces and draw a rectangle around each face
for (x, y, w, h) in face_rectangles:
    cv.rectangle(resized_image, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)  # Draw a green rectangle with thickness 2

# Display the image with the detected faces highlighted
cv.imshow('Detected Faces', resized_image)

# Wait for a key press to close the OpenCV windows
cv.waitKey(0)
cv.destroyAllWindows()
