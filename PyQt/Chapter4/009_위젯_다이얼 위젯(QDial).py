import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDial

# QDial 공식 문서 : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QDial.html

class 다이얼위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        self.dial = QDial(self)
        self.dial.move(30, 20)

        self.dial2 = QDial(self)
        self.dial2.move(200, 20)
        self.dial2.setRange(0, 50)
        self.dial2.setNotchesVisible(True)

        # - 범위 지정은 setRange(Start, Stop)으로 함.
        # - 노치(결과 창 참고, 주위로 범위를 표시할 수 있는 눈금) 를 표시하기 위해서는 setNotchesVisible() 사용함
        #  기본적으로는 False로 보여주지 않음.

        self.label1 = QLabel('다이얼 1값', self)
        self.label1.move(40, 130)
        self.label2 = QLabel('다이얼 2값', self)
        self.label2.move(210, 130)

        btn = QPushButton('기본값으로 되돌리기', self)
        btn.move(115, 200)

        self.dial.valueChanged.connect(self.chageValue)
        self.dial2.valueChanged.connect(self.chageValue)

        btn.clicked.connect(self.btn_clicked)

        # valueChanged은 다이얼값이 변경될 때 시그널

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('QLineEdit')  
        self.show()

    def btn_clicked(self): # 버튼 클릭시 초기화합니다.
        self.dial.setValue(0)
        self.dial2.setValue(0)

    def chageValue(self):
        self.label1.setText(str(self.dial.value()))
        self.label2.setText(str(self.dial2.value()))


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 다이얼위젯()
프로그램무한반복.exec_()