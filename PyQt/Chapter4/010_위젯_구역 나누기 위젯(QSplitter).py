import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QSplitter, QHBoxLayout

# QSplitter를 사용하면 가장 좋은 점은 Split Handle을 사용할 수 있다는 것
# 예를 들어 아래와 같은 구성이라면 Handler를 마우스로 클릭하여 상하 좌우로 움직일 수 있음

# 자세한 내용은 링크! : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSplitter.html

class 구역나누기위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        hbox = QHBoxLayout(self)

        top = QWidget(self)
        top.setStyleSheet('background-color : red;')

        middle = QWidget(self)
        middle.setStyleSheet('background-color : green;'
                             'border-radius : 10px;')

        bottom_left = QWidget(self)
        bottom_left.setStyleSheet('background-color : blue;'
                                  'border-style : solid;'
                                  'border-width : 3px;'
                                  'border-color : black;')

        bottom_right = QWidget(self)
        bottom_right.setStyleSheet('background-color : gray;'
                                   'border-style : outset;'
                                   'border-width : 4px;'
                                   'border-color : red;')

        # - 각 위젯의 경계선을 선택해 위젯의 크기를 줄이거나 늘릴 수 있음
        # - 각 위젯마다 setStyleSheet로 옵션을 주어 다르게 표시

        split1 = QSplitter(Qt.Horizontal)
        split1.addWidget(bottom_left)
        split1.addWidget(bottom_right)

        split2 = QSplitter(Qt.Vertical)
        split2.addWidget(top)
        split2.addWidget(middle)
        split2.addWidget(split1)

        hbox.addWidget(split2)

        self.setLayout(hbox)

        # - QWidget, QSplitter, QHBoxLayout 이용해 레이아웃 설정
        # - 즉, 최하단 위젯에서 최상위 레이아웃으로 가는것을 표시한다면
        # - `split1(bottom_left, bottom_right) → split2 (top, middle,split1) → hbox → 화면` 구성으로 되어있음

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('QLineEdit')  
        self.show()