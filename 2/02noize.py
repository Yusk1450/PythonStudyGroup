
import numpy as np
import cv2 as cv
import random

# 画像を読み込む
img = cv.imread('Lenna.png')

w = img.shape[0]
h = img.shape[1]
for x in range(w):
	for y in range(h):
		if random.randint(0, 10) == 0:
			img[y, x] = 0

# 移動平均フィルタ
dstimg = cv.blur(img, (10, 10))
# メディアンフィルタ
# dstimg = cv.medianBlur(img, 5)
# ガウシアンフィルタ
# dstimg = cv.GaussianBlur(img, (3, 3), 3)

# ウィンドウ名を指定して、画像を表示する
cv.imshow('image', img)
cv.imshow('result', dstimg)

cv.waitKey(0)
cv.destroyAllWindows()