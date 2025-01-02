import cv2

# 카메라 연결 (기본 카메라: 0번)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: 카메라를 열 수 없습니다.")
    exit()

# 프레임 크기 설정 (옵션)
cap.set(3, 300)  # 너비
cap.set(4, 200)  # 높이

while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        print("Error: 프레임을 읽을 수 없습니다.")
        break

    cv2.imshow("VideoFrame", frame)  # 프레임 출력

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
