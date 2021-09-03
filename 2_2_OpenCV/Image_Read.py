import cv2

image_file = "Image/study_image.jpg"

original = cv2.imread(image_file, cv2.IMREAD_COLOR)

gray = cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)

unchange = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)


cv2.imshow("imread_color", original)
cv2.imshow("image_gratscale", gray)
cv2.imshow("imread_unchange",unchange)

cv2.waitKey(0)