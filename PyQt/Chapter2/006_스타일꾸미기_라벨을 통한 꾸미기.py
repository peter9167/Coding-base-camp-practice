import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

# QLabel : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html


class 라벨(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        licat = QLabel()    # 라벨(licat) 생성
        pie = QLabel()      # 라벨(pie) 생성
        sun = QLabel()      # 라벨(sun) 생성

        licat.setStyleSheet(    # 라벨(licat) 스타일 설정
            "border-style: solid;"  # 테두리 스타일 지정 <- 실선(solid)
            "border-width: 3px;"    # 테두리 넓이(두께) 지정 <- 3px
            "border-color: red;"    # 테두리 색상 지정 <- 빨강(red)
            "border-radius: 3px;"   # 테두리 둥근 모서리 크기 지정 <- 3px
            "image: url(img/weniv-licat.png)"   # 이미지 지정 <- weniv-licat.png
            # 이하 내용(초기화, 설정) 같음
        )
        pie.setStyleSheet(
            "border-style: double;"
            "border-width: 5px;"
            "border-color: blue;"
            "background-color: #87CEFA;"
            "image: url(img/weniv-pie.png)"
        )
        sun.setStyleSheet(
            "border-style: dot-dot-dash;"
            "border-width: 5px;"
            "border-color: green;"
            "border-radius: 3px;"
            "background-color: beige;"
            "image: url(img/weniv-sun.png)"
        )

        hbox = QHBoxLayout()    # QHBoxLayout : 수직박스 생성 <- 여기서 주목해야 되는 것은 QH에서 H가 Height를 나타냄. 그래서 수직박스로 지정됨.
        hbox.addWidget(licat)   # 레이아웃 추가
        hbox.addWidget(pie)     # 레이아웃 추가
        hbox.addWidget(sun)     # 레이아웃 추가

        self.setLayout(hbox)    # 창에 레이아웃 연결

        self.setGeometry(400, 400, 500, 400)
        self.setWindowTitle('라벨을 통한 꾸미기!')
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 라벨()
프로그램무한반복.exec_()