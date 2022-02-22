from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication,\
                            QPushButton, QLabel
from PyQt5.QtCore import Qt, QCoreApplication
import sys


class 전광판만들기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        lcd = QLCDNumber(self) # QLCDNumber() : 숫자lcd 위젯
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)

        self.slider.valueChanged.connect(lcd.display) # valueChanged : 값이 변하면 시그널을 보냄 / lcd.display : 내장 함수로서 슬라이더값과 연동해 숫자를 보여주는 기능
        self.slider.valueChanged.connect(self.setValue) # valueChanged : 값이 변하면 시그널을 보냄

        btn1 = QPushButton('초기화')
        btn2 = QPushButton('종료')

        btn1.clicked.connect(self.changeValue)  
        btn2.clicked.connect(self.exitProgram)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(self.slider, alignment=Qt.AlignCenter)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Signal and Slot')
        self.show()
    
    def changeValue(self): # 값을 초기화 함
        self.slider.setValue(0)
        self.label.setText(str(self.slider.value()))

    def setValue(self): # 슬라이더 값이 변경되면 라벨 값 변경되도록
        self.label.setText(str(self.slider.value()))

    def exitProgram(self): # 종료 버튼을 누르면 종료 되도록
        QCoreApplication.instance().quit()
        # super().close() 이것도 사용가능


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 전광판만들기()
프로그램무한반복.exec_()