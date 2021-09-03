import cv2
from matplotlib import pyplot as plt
#이미지 경로
image_file = "Image/study_image.jpg"
# 수정 ㅇ벗는 원본 이미지
original = cv2.imread(image_file, cv2.IMREAD_COLOR)
# 흑백 사진 이미지
gray = cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)
# 이미지 파일의 알파 채널
unchange = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
# rbg는 저작권이 붙어 bgr로 입력
color = ('b','g','r')


for i,col in enumerate(color):
    # calcHist 파라미터 설명
    # 1. images : 분석할 이미지 파일
    # 2. Channel : 컬러 이미지(BGR)이면, 배열 값 3개로 정의
    # 3. mask : 분석할 영역의 형태인 mask
    # 4. images : 히스토그램의 hist 크기,
    # 5. 범위 : 컬러 이미지(bgr)아묜 0 - 256까지 배열
    hist = cv2.calcHist([original],[i], None, [256],[0,256])
    plt.figure(1)
    plt.plot(hist, color = col)


# 원본 이미지 히스토그램 출력
plt.show()




