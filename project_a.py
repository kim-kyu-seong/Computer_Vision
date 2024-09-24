import sys 
import cv2
import numpy as np

img = cv2.imread("./assets/cat.jpg")
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# I = round(0.299*R + 0.587*G + 0.114*B)
# TODO: 컬러 사진을 흑백사진으로 변환하기
# 행렬 연산하기

# 이미지 크기 가져오기 (높이, 너비, 채널)
height, width, channels = img.shape
print(height, width, channels) # 가로, 세로 픽셀크기, 3차원확인

# 흑백 사진을 넣을 빈 이미지배열 생성 (높이 x 너비, 단일 채널, dtype 0~255값으로 제약)
gray_img = np.zeros((height, width), dtype=np.uint8)

# 명암 변환 공식을 적용해 R, G, B 값을 그레이스케일로 변환
for i in range(height):
    for j in range(width):
        # img (i,j)에 위치한 픽셀의 BGR값을 순서대로 읽음
        B, G, R = img[i, j]

        # 명암 변환
        gray_value = round(0.299 * R + 0.587 * G + 0.114 * B)

        # 해당 픽셀에 변환값을 입력
        gray_img[i, j] = gray_value

# 변환된 흑백 이미치 출력
cv2.imshow("Gray_image", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
