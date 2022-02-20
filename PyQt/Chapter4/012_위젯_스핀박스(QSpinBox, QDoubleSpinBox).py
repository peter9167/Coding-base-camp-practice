from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QDoubleSpinBox, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import sys

# SpinBox는 숫자를 올리거나 내릴 때 사용할 수 있는 input 창
# 정수는 QSpinBox를 통하여, 실수는 QDoubleSpinBox를 통해 구현할 수 있음

class 스핀박스(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        ###--------------QSpinBox-----------------###

        self.label1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(100000000)
        self.spinbox.setSingleStep(1000) 
        self.label2 = QLabel('0')
        
        self.spinbox.valueChanged.connect(self.valueChange)

        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSpinBox.html
        '''
        - QSpinBox는 정수만 표시 가능한 박스
        - setMinimum(값): 스핀박스의 최소값 지정
        - setMaximum(값): 스핀박스의 최대값 지정
        - self.spinbox.setRange(최저값,최대값) 으로도 설정가능 Default = 0 ~ 99
        - setSingleStep(값) : 스핀박스가 움직일 때 얼마 만큼 건너 뛸 수 있는지
        - 스핀 위젯이 변경될 때 발생하는 시그널을 valueChange 함수에 연결
        '''

        # ==============QDoubleSpinBox===========### 

        self.label3 = QLabel('QDoubleSpinBox')
        self.dSpinbox = QDoubleSpinBox()  
        self.dSpinbox.setSingleStep(0.5)
        
        self.dSpinbox.setSuffix("달러")
        self.dSpinbox.setDecimals(1)
        self.label4 = QLabel('0')

        self.dSpinbox.valueChanged.connect(self.valueChange2)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.dSpinbox)
        vbox.addWidget(self.label4)

        self.setLayout(vbox)
        self.setWindowTitle('QSpinBox, QDoubleSpinBox')
        self.setGeometry(300, 300, 400, 300)
        self.show()

        '''
        - 더블 스핀박스는 소수 점도 표현 할 수 있는 박스
        - self.spinbox.setRange(최저값,최대값) 으로도 설정가능 Default = 0 ~ 99
        - setPrefix(문자열) = 숫자 앞에 올 문자를 설정 할 수 있음
        - setDecimals(값): 소수점 아래 표시될 자리 수 설정
        - 더블 스핀 위젯이 변경될 때 발생하는 시그널을 valueChange2 함수에 연결
        '''

    def valueChange(self): # 현재 스핀박스의 값을 가져와 원화를 달러로 변경해 라벨에 업데이트
        self.label2.setText(f'{self.spinbox.value()}원 ->' + 
                            f'{round(self.spinbox.value()/1191, 2)}달러')

    def valueChange2(self): # 환율에 따른 결과를 round함수를 통해 소수점 이하 3번째자리에서 반올림하여 라벨에 업데이트 
        self.label4.setText(f'{self.dSpinbox.value()}달러 -> '+ 
                            f'{round(self.dSpinbox.value()*1191, 2)}원')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 스핀박스()
프로그램무한반복.exec_()