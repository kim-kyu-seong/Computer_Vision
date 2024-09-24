import sys
import cv2

cap = cv2.VideoCapture("./assets/Video.mp4")
if not cap.isOpened(): # --> boolean
    sys.exit("파일 없음")

captures = []
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("비디오", frame)
        key = cv2.waitKey(1)
        if key == ord("c"):
            captures.append(frame)
            print(captures)
        elif key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

# 캡쳐된 프레임 저장하기
if len(captures) > 0:
    for i, capture in enumerate(captures): # 인덱스를 같이 뽑아주는 내장함수 0, 1, 2, 3, ---
        cv2.imwrite(f"./outputs/frame-{i}.jpg", capture) # 파일명
