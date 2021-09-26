import cv2

video = cv2.VideoCapture(0)
subtractor = cv2.createBackgroundSubtractorMOG2(10,100)

while True:

    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(5) == ord('q'):
            break

cv2.destroyAllWindows()
video.release()
