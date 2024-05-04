import cv2 as cv
import numpy as np
img  = np.zeros((500,500,3), dtype='uint8')
img[:] = 80,255,136
cv.rectangle(img, (0,0), (255,255), (0,255,0), thickness=-1 )
cv.circle(img, (300,300), 20, (255,255,255), thickness=-1 )
cv.line(img, (0,0), (300,300), (0,0,255), thickness=int((3+1) / 2) )
cv.putText(img, "Hello World", (0, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
cv.imshow('image',img)
cv.waitKey(0)
