import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton

class Madoka(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('空っぽな窓') # ウィンドウのタイトル
        self.setGeometry(100,100,200,150) # ウィンドウの位置と大きさ
        button1 = QPushButton('とあるボタン',self)
        button1.setGeometry(25,25,150,100)

qAp = QApplication(sys.argv)
mado = Madoka()
mado.show()
qAp.exec()