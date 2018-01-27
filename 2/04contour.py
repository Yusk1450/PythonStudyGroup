
import numpy as np
import cv2 as cv

# 画像を読み込む
img = cv.imread('apple.jpg')

# グレースケールの画像を作成する
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2値化
ret, thresimg = cv.threshold(grayimg, 210, 255, cv.THRESH_BINARY)

# 輪郭抽出
image, cnts, hierarchy = cv.findContours(thresimg, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(len(cnts))

for i in range(len(cnts)):
	# area = cv.contourArea(cnts)

	if len(cnts[i]) > 0:
		rect = cnts[i]
		x, y, w, h = cv.boundingRect(rect)
		if w > 30 or h > 30:
			cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

# ウィンドウ名を指定して、画像を表示する
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()