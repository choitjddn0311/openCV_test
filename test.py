import cv2 as c
import numpy as numpy

# opencv 라이브러리를 사용해서 python에서 이미지 불러오기
# 변수 선언 후 imread("경로" , image type) image type에서 0,1도 넣을 수 있음 0 = grayscale, 1 = color
gray = 0
color = 1
image = c.imread("C:/Users/user/Desktop/slexn/openCV_test/1.jpg" , color)
#numpy저장배열덕에 숫자도 사용할수 있다 - = 어둡게 , + = 밝게
image2 = image+50
image3 = image-1
# imshow 함수를 사용해 창을 통해 창 title과 뭘 보여줄지 설정 imshow("name" , 보여줄 파일) 
c.imshow("testcv", image3)
# 키 입력 대기함수 waitKey(0) <== 무한대기 ex) waitKey(1000) <== 1초 단위가 ms 이다
c.waitKey(0)
# 모든 창을 닫는 함수 (왜 있는지는 모름) 없어도 코드 실행은 됨
c.destroyAllWindows()