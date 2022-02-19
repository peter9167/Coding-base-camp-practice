# QWidget의 기본 위치를 지정하는 메서드는 아래와 같음

    # - def update (x, y, w, h)
    # - def setGeometry (x, y, w, h)
    # - def setContentsMargins (left, top, right, bottom)
    # - def setFixedSize (w, h)
    # - def setFixedWidth (w)
    # - def setFixedHeight (h)
    # - def repaint (x, y, w, h)
    # - def setSizeIncrement (w, h)
    # - def resize (w, h)

# 대부분의 위젯은 QWidget을 상속받기 때문에 위 메서드를 사용할 수 있음
# 자세한 내용은 아래 공식문서를 참고

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

# QLabel : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html


class 기본위치(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        # 테스트버튼 = QPushButton('버튼입니다.', self)
        # 테스트버튼.setGeometry(50, 200, 100, 40)
        # 테스트버튼.move(50, 100)
        # 테스트버튼.resize(100, 50)    # width 와 height 를 지정 또는 나타냄
        # 테스트버튼.setFixedSize(w, h) # width 와 height 를 고정
        # 테스트버튼.setFixedWidth(w)   # width 만 고정
        # 테스트버튼.setFixedHeight(h)  # height 만 고정

        파이라벨 = QLabel('나는 파이', self)
        파이라벨.move(60, 20)
        썬라벨 = QLabel('나는 썬', self)
        썬라벨.move(230, 60)


        파이이미지 = QLabel(self)
        파이이미지.setPixmap(QPixmap('img/weniv-pie.png')) # 이미지 설정
        파이이미지.move(40,40)
        
        썬이미지 = QLabel(self)
        썬이미지.setPixmap(QPixmap('img/weniv-sun.png'))
        썬이미지.move(200,80)

        파이버튼 = QPushButton('파이', self)
        파이버튼.move(70, 230)
        썬버튼 = QPushButton('썬', self)
        썬버튼.move(230, 230)

        self.setWindowTitle('기본위치')
        self.setWindowIcon(QIcon('img/캣네생선.png'))
        self.setGeometry(300, 300, 400, 300)
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 기본위치()
프로그램무한반복.exec_()




