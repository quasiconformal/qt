import numpy as np
import cv2 as cv

#画像データのロード
#ロード失敗時のNone処理は省略
img = cv.imread('../len_std.png',cv.IMREAD_COLOR)

#ウィンドウに表示
cv.imshow('title',img)

cv.waitKey(0)
#cv.destroyWindow('title')
cv.destroyAllWindows()