import sys
import random

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QMainWindow
from circles_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.qp = QPainter()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event: QPaintEvent):
        if self.flag:
            self.qp.begin(self)
            self.qp.setBrush(QColor(random.randint(0, 0xffffff)))
            self.qp.setPen(QColor(random.randint(0, 0xffffff)))
            a = random.randint(0, 150)
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            self.qp.drawEllipse(x - a // 2, y - a // 2, a, a)
            self.qp.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
