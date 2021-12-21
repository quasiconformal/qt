import numpy as np
import cv2 as cv

from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QImage, QPixmap

##https://note.com/fz5050/n/n3b6015667654

class MainWindow(QWidget):

   def __init__(self):
       super().__init__()

       self.setup()

   
   # 各種セットアップ
   def setup(self):


       # OpenCVで画像をロードしてBGR⇒RGBにチャネル順を修正
       img = cv.imread('test1.png',cv.IMREAD_COLOR)
       img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

       height, width, _ = img.shape
       bytePerLine = img.strides[0] # ⇒ 3*width相当

       # QImageオブジェクト作成 PyQt6.0.0時点ではQImageの引数の型が変わっているので注意
       # qimg = QImage(img.tobytes(), width, height, bytePerLine, QImage.Format.Format_RGB888)
       qimg = QImage(img.data, width, height, bytePerLine, QImage.Format.Format_RGB888)       
       # QPixmapの作成
       pixmap = QPixmap(QPixmap.fromImage(qimg))
       imgLabel = QLabel(self)
       imgLabel.setPixmap(pixmap)
       

       # 表示するwindowの調整
       self.resize(imgLabel.pixmap().size())
       self.setWindowTitle("load from OpenCV")
       #self.setGeometry(0, 0, pixmap.width(), pixmap.height()) # ディスプレイ上の表示位置と描画範囲
       self.show()


if __name__ == '__main__':
   app = QApplication([])
   windows = MainWindow()
   app.exec()