from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

from PyQt6.QtCore import pyqtSignal, pyqtSlot, QThread

import cv2 as cv
import numpy as np

class VideoThread(QThread):
   # シグナル設定
   change_pixmap_signal = pyqtSignal(np.ndarray)

   def __init__(self):
       super().__init__()
       self._run_flag = True

   # QThreadのrunメソッドを定義
   def run(self):
       cap = cv.VideoCapture(0)
       while self._run_flag:
           ret, cv_img = cap.read() # 1フレーム取得
           # 新たなフレームを取得できたら
           # シグナル発信(cv_imgオブジェクトを発信)            
           if ret:
               self.change_pixmap_signal.emit(cv_img)

       # videoCaptureのリリース処理
       cap.release()
   
   # スレッドが終了するまでwaitをかける
   def stop(self):
       self._run_flag = False
       self.wait()


class App(QWidget):

   def __init__(self):
       super().__init__()

       self.image_label = QLabel(self)
       
       # vboxにQLabelをセット
       vbox = QVBoxLayout()
       vbox.addWidget(self.image_label)

       # vboxをレイアウトとして配置
       self.setLayout(vbox)

       # ビデオキャプチャ用のスレッドオブジェクトを生成
       self.thread = VideoThread()
       # ビデオスレッド内のchange_pixmap_signalオブジェクトのシグナルに対するslot
       self.thread.change_pixmap_signal.connect(self.update_image)

       self.thread.start() # スレッドを起動


   # 終了時にスレッドがシングルになるようにする
   def closeEvent(self,event):
       self.thread.stop()
       event.accept()


   @pyqtSlot(np.ndarray)
   def update_image(self, cv_img):
       #img = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
       # QT側でチャネル順BGRを指定
       qimg = QtGui.QImage(cv_img.tobytes(),cv_img.shape[1],cv_img.shape[0],cv_img.strides[0],QtGui.QImage.Format.Format_BGR888)
       qpix = QPixmap.fromImage(qimg)
       self.image_label.setPixmap(qpix)

if __name__ == "__main__":
   app = QApplication([])
   window = App()
   window.show()
   app.exec()