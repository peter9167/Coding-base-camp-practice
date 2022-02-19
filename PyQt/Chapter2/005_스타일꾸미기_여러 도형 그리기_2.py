import sys

from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPolygon
from PyQt5.QtCore import Qt, QPoint


class 도형그리기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('도형 그리기!')
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.다각형(paint)
        paint.end()

    def 다각형(self, paint):
        점 = [              # 무작위로 다각형점 지정
            QPoint(10, 10),
            QPoint(20, 30),
            QPoint(130, 120),
            QPoint(260, 140),
            QPoint(360, 160),
            QPoint(320, 280),
            QPoint(220, 270),
            QPoint(200, 195),
        ]

        다각형 = QPolygon(점)   # 다각형 생성
        paint.setPen(QPen(Qt.red, 10))
        paint.drawPolygon(다각형)

        점 = [
            QPoint(320, 260),
            QPoint(300, 180),
            QPoint(120, 290),
            QPoint(200, 295),
        ]

        다각형_둘 = QPolygon(점)
        paint.setPen(QPen(Qt.blue, 10))
        paint.drawPolygon(다각형_둘)

        # 호, 현, 파이
        # (x, y, width, height, start-angle, span-angle)
        paint.setPen(QPen(Qt.black, 5))
        paint.drawArc(100, 300, 100, 100, 0*16, 180*16)
        paint.drawText(100, 450, '180도')

        paint.setPen(QPen(Qt.red, 5))
        paint.drawChord(250, 300, 100, 100, 270*16, 60*16)
        paint.drawText(250, 450, '60도')

        paint.setPen(QPen(Qt.blue, 5))
        paint.drawPie(400, 300, 100, 100, 90*16, 180*16)
        paint.drawText(400, 450, '180도')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 도형그리기()
프로그램무한반복.exec_()