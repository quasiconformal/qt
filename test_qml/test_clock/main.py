import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QTimer

from time import strftime, localtime

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

def update_time():
    # Pass the current time to QML.
    curr_time = strftime("%Y/%m/%d %H:%M:%S", localtime())
    engine.rootObjects()[0].setProperty('currTime', curr_time)

timer = QTimer()
timer.setInterval(100)  # msecs 100 = 1/10th sec
timer.timeout.connect(update_time)
timer.start()


sys.exit(app.exec())