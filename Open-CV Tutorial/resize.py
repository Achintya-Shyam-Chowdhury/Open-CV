import cv2 as cv

def mediaResize(frame, scale=.80):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

    
    