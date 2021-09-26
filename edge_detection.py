import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    cv2.imshow('Camera', frame)

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    laplacian = np.uint8(laplacian)
    cv2.imshow("Laplacian", laplacian)

    edges = cv2.Canny(frame,80,80)
    cv2.imshow("Canny", edges)

    if cv2.waitKey(5) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
