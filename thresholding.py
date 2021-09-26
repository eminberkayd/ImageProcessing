import cv2

img = cv2.imread("book.jpeg",0)


_, frame = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 8)

cv2.imshow("Normal Image", img)
cv2.imshow("Direct Threshold", frame)
cv2.imshow("Adaptive Threshold", adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()
