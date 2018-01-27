
import numpy as np
import cv2 as cv

# 画像を読み込む
img = cv.imread('Lenna.png', cv.IMREAD_GRAYSCALE)

cv.imwrite('test.png', img)

# ウィンドウ名を指定して、画像を表示する
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()