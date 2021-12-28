from PyQt6 import QtCore, QtGui, QtQuick


class CVItem(QtQuick.QQuickPaintedItem):
    imageChanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CVItem, self).__init__(parent)
        # self.setRenderTarget(QtQuick.QQuickPaintedItem.FramebufferObject)
        self.m_image = QtGui.QImage()

    def paint(self, painter):
        if self.m_image.isNull():
            print("image null")
            return
        image = self.m_image.scaled(self.size().toSize())
        painter.drawImage(QtCore.QPoint(), image)

    def image(self):
        return self.m_image

    def setImage(self, image):
        #print("set image", image, self.m_image)
        if self.m_image == image:
            print("image unchanged")
            return
        if self.m_image.isNull():
            print("setImage image null")
        self.m_image = image
        #print("emit image")
        self.imageChanged.emit()
        self.update()

    image = QtCore.pyqtProperty(QtGui.QImage, fget=image, fset=setImage, notify=imageChanged)