
import numpy as np
import cv2 as cv
import random

# 画像を読み込む
img = cv.imread('Lenna.png')

# グレースケールの画像を作成する
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 顔の分類器の作成
face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
# 目の分類器の作成
eye_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')

# 認識した顔配列
facerect = face_cascade.detectMultiScale(grayimg, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
# 認識した目配列
eyerect = eye_cascade.detectMultiScale(grayimg)

print(facerect)
print(eyerect)

if len(facerect) > 0:
	for rect in facerect:
		cv.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=1)

if len(eyerect) > 0:
	for rect in eyerect:
		cv.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 255, 0), thickness=1)

# ウィンドウ名を指定して、画像を表示する
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()