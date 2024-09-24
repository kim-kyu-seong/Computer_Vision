import sys 
import cv2

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# I = round(0.299*R + 0.587*G + 0.114*B)
# TODO: 컬러 사진을 흑백사진으로 변환하기

cv2.imshow(cvt_img)