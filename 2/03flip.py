
import numpy as np
import cv2 as cv

# 画像を読み込む
img = cv.imread('Lenna.png')

# 画像を反転する
img = cv.flip(img, 1)

# ウィンドウ名を指定して、画像を表示する
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()