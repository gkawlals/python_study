import cv2
import numpy as np
from util.CmmUtils import *
import pandas as pd

def preprocessing():

    # 분석하기 위한 이미지 불러오기
    image = cv2.imread("Image/study_face.jpeg", cv2.IMREAD_COLOR)

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
image, gray = preprocessing()

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
        face_center = ( x + w // 2, y + h // 2)
        # 양쪽 눈 가운데 위치 값 가져오기
        eye_centers = [[x+ex+ew//2, y+ey+eh//2] for ex, ey, ew, eh in eyes]

        # 사진의 기울기 보정
        correction_image, correction_center = doCorrectionImage(image, face_center, eye_centers)

        rois = doDetectObject(faces[0], face_center)

        base_mask = np.full(correction_image.shape[:2], 255, np.uint8)

        # 얼굴 전체 마스크 만들기 ( 사람의 얼굴은 평균 약 45% 타원으로 구성 )
        # 얼굴 영역을 연산하지 않기 위해 색상을 검정색 ( 값 : 0) 으로 설정
        face_mask = draw_eclipse(base_mask, rois[3], 0, -1)

        # 얼굴 전체 마스크 만들기 ( 사람의 얼굴은 평균 약 45% 타원으로 구성 )
        # 얼굴 영역 연산하기 않기 위해 색상을 검정색( 값 : 255)으로 설정
        lip_mask = draw_eclipse(np.copy(base_mask), rois[2], 255)

        # 윗머리용, 얼굴전체 마스크, 귓밑머리용 얼굴전체 마스크, 입술 마스크, 입술 제외용 마스크를 masks 저장
        masks = [face_mask, face_mask, lip_mask, ~lip_mask]

        masks = [mask[y:y + h, x:x + w] for mask, ( x, y, w, h) in zip(masks, rois)]

        for i, mask in enumerate(masks):
            cv2.imshow("mask", str(i), mask)

    else :
        print("눈이 없어")

else :
    print("얼굴 없어")

# 입력받는 것 대기하기, 작성안하면, 결과창이 바로 닫힘
cv2.waitKey(0)
