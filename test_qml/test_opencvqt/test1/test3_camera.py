import cv2 as cv

# VideoCaptureオブジェクトの作成
cameraCapture = cv.VideoCapture(0)

# 表示用ウィンドウの準備
cv.namedWindow('myWindow') 

print('now running.../ press any key to stop')

# キャプチャしているの映像フレームを取得して表示
success, frame = cameraCapture.read()
while success and cv.waitKey(1) == -1:
   cv.imshow('myWindow', frame)
   success, frame = cameraCapture.read()

# 終了処理
cv.destroyWindow("myWindow")
cameraCapture.release()
