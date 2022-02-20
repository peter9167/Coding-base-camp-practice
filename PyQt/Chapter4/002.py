import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout
from PyQt5.QtGui import QColor, QIcon

# QPushButton : ("단축키설정" 혹은 문자열로 표시할 내용 생성) ALT + &뒤에 한글자와 합쳐져 단축키가 됨 여기서는 Alt + b
# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html

    # setCheckable(True) :** 단축키를 선택되거나 선택되지 않은 상태로 만들 수 있음
    # btn_2.toggle()** : 프로그램이 시작될 때 선택되어 있는 상태로 실행 하는 함수
    # setIcon(QIcon('img/weniv-licat.png')) :** QIcon 라이브러리로 icon설정 가능

class 버튼(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        btn_1 = QPushButton(self)
        btn_1.setText('버튼1')
        btn_1.setEnabled(True)

        btn_2 = QPushButton('&Button2', self)
        btn_2.setText('버튼2')
        btn_2.setEnabled(True)

        btn_3 = QPushButton('버튼3', self)
        btn_3.setIcon(QIcon('img/weniv-licat.png'))
        btn_3.move(50, 200)
        btn_3.setFixedSize(200, 50)

        btn_2.toggle()

        hbox = QHBoxLayout() 
        hbox.addWidget(btn_1) 
        hbox.addWidget(btn_2)
        hbox.addWidget(btn_3)
       
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QCheckBox')  
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 버튼()
프로그램무한반복.exec_()