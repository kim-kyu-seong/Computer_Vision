import sys 
import cv2

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# I = round(0.299*R + 0.587*G + 0.114*B)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # <--
resized_img = cv2.resize(gray_img, dsize=(0,0), fx=0.5, fy=0.5)

cv2.imshow("Color Image", img)
cv2.imshow("Grayscale Image", gray_img) # <--
cv2.imshow("Resized Image", resized_img) # <--
cv2.waitKey()
cv2.destroyAllWindows()




