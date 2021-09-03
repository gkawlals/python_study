import cv2
import numpy as np
from util.CmmUtils import *
import roi as roi
def preprocessing():

    # 분석하기 위한 이미지 불러오기
    image = cv2.imread("Image/study_image.jpg", cv2.IMREAD_COLOR)

    # 이미지가 존재하지 않으면 에러 발생
    if image is None : return None, None

    # 이미지 크기 사이즈 변경하기
    image = cv2.resize(image,(700, 700))

    # 흑백사진으로 변경
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 변환한 흑백사진으로부터 히스토그램 평활화 ( 흑백의 강도를 쌔게해서 인식률을 높인다 )
    gray = cv2.equalizeHist(gray)

    return image, gray

# 학습된 얼굴 정면검출기 사용하기
face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")

# 학습된 눈 검출기 사용하기
eye_cascade = cv2.CascadeClassifier("data/haarcascade_eye_tree_eyeglasses.xml")

# 인식률을 높이기 위한 전처리 함수 호출
image, gray = preprocessing() # 전처리 : 데이터를 가공하는 구문

if image is None: raise Exception("영상 파일 읽기 에러")

# 얼굴 검출수행 ( 정확도 높이는 방법의 아래 파라미터를 조절 )
# 얼굴 검출은 히스토그램 평황화한 이미지 사용
# scaleFactor : 1.1
# minNeighbors : 인근 유사 픽셀 발견 비율이 2번 이상
# flags : 0 => 더이상 사용하지 않는 인자값
# 분석할 이미지의 최소 크기 : 가로 100, 세로 100
faces = face_cascade.detectMultiScale(gray, 1.1, 2, 0, (100, 100))


# 얼굴이 검출되면
if faces.any():

    # 얼굴 위치 값 들고오기
    x, y, w, h = faces[0]

    # 원본이미지로부터 얼굴영역 가져오기
    face_image = image[y:y + h, x:x + w]

    # 눈 검출 수행하기 ( 정확도 높이는 방법의 아래 파라미터를 조절 )
    # 눈 거물은 얼굴 이미지 영역만 불러와 분석 수행
    # scaleFactor : 1.15
    # minNeighbors : 인근 유사 픽셀 발견 비율이 7번 이상
    # flags : 0 => 더이상 사용하지 않는 인자값
    # 분석할 이미지의 최소 크기 : 가로 25, 세로 20
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))

    # 눈을 찾을 수 있다면,
    if len(eyes) == 2:

        # 얼굴 가운데
        face_center  = ( x + w // 2, y + h // 2)
        # 양쪽 눈 가운데 위치 값 가져오기
        eye_centers = [[x+ex+ew//2, y+ey+eh//2] for ex, ey, ew, eh in eyes]

        # 사진의 기울기 보정
        correction_image, correction_center = doCorrectionImage( image, face_center, eye_centers )

        # 보정된 눈 좌표 그리기
        rois = doDetectObject(faces[0], face_center)

        # 얼굴 검출 사각형 그리기
        cv2.rectangle(correction_image, rois[0], (255, 0, 255), 2) # 윗머리 영역
        cv2.rectangle(correction_image, rois[1], (255, 0, 255), 2) # 귀밑머리 영역

        # 입술 검출 사각형 그리기
        cv2.rectangle(correction_image, rois[2], (255, 0, 0), 2)

        # 보정된 눈 좌표 그리기
        cv2.circle(correction_image, tuple(correction_center[0]), 5, (0, 255, 0), 2)
        # 보정 눈 좌표
        cv2.circle(correction_image, tuple(correction_center[1]), 5, (0, 255, 0), 2)
        # 보정된 얼굴 중심 그리기
        cv2.circle(correction_image, face_center, 3, ( 0, 0, 255 ), 2) # 얼굴 중심 좌표

        # resize_img = cv2.resize(correction_image,(700,700))

        cv2.imshow("MyFace_Edit", correction_image)

    else :
        print("눈이 없어")

    # # 얼굴 검출 사각형 그리기
    # cv2.rectangle(image, faces[0], ( 255, 0, 0), 4)
    #
    # # 사이즈 변경된 이미지로 출력하기
    # cv2.imshow("Myface", image)
else : print("얼굴 없어")

# 입력받는 것 대기하기, 작성안하면, 결과창이 바로 닫힘
cv2.waitKey(0)