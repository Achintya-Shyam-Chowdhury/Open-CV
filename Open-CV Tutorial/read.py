import cv2 as cv #importing open-cv as cv
import resize as rescale
def mediaResize(frame, scale=.80):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

    

capture = cv.VideoCapture('DD/hp.mp4')#capturing the video

while True:
    isTrue, frame = capture.read()
    rescaled_frame = mediaResize(frame, scale=.5)
    cv.imshow("ReFrame", rescaled_frame)
    cv.imshow("Frame", frame)
    print(type(frame))
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()