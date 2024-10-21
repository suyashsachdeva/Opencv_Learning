import cv2 as cv
import numpy as np

blank=np.zeros((480,600,3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. Change the background color of teh image
blank[:]= 0,255,255
#cv.imshow('Green',blank)

# 2. Draw a rectange
cv.rectangle(blank,(80,100), (250,blank.shape[1]//2), (255,0,0), thickness=-1)
#cv.imshow('rectangle',blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[1]//2), 40, (0,0,255), thickness=-1)
#cv.imshow('circle', blank)

# 4.Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
#cv.imshow('line', blank)

# 5.Text on the image
cv.putText(blank, 'Suyash Sachdeva', (blank.shape[1]//8,blank.shape[0]//8), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)