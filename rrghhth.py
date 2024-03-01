import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import random

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)

        self.s = QtWidgets.QGraphicsScene()
        self.vi = QtWidgets.QGraphicsView(self)
        self.vi.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.vi.setScene(self.s)

        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(0, 300)
        ci = QtWidgets.QGraphicsEllipseItem(-diameter / 2, -diameter / 2, diameter, diameter)
        ci.setBrush(QtGui.QColor(255, 255, 0))
        self.s.clear()
        self.s.addItem(ci)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
