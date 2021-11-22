import sys
from random import choice

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.qwa)
        self.pushButton.setStyleSheet("background-color: #FFFF00")
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def qwa(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        self.coords_ = [choice(range(800)), choice(range(800))]
        khe = choice(range(400))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.coords_[0], self.coords_[1], khe, khe)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
