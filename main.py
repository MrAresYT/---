import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


def get_random_size():
    size = randint(50, 300)
    return randint(0, 500), randint(0, 500), size, size


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Cлучайные окружности')
        self.setFixedSize(600, 600)
        self.btn = QPushButton('Рисовать', self)
        self.btn.setFixedSize(100, 50)
        self.btn.move(0, 0)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(*get_random_color()))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(*get_random_size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = Example()
    ex.show()
    sys.exit(app.exec())
