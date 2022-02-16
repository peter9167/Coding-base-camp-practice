import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication

class 월급받아집은언제(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.합산 = QLabel('* 5년 월급 합: -원,  \n\n* 5년 실수령액 합 : -원\n\n* 실수령액과 집값과의 차 : -원')
        버튼 = QPushButton('계산하기')
        버튼.clicked.connect(self.btnClick)

        가로정렬 = QHBoxLayout()
        가로정렬.addWidget(self.사용자입력그룹박스())
        가로정렬.addWidget(self.연봉그룹박스())
        가로정렬.addWidget(self.실수령액그룹박스())

        세로정렬 = QVBoxLayout()
        세로정렬.addLayout(가로정렬)
        세로정렬.addWidget(self.합산)
        세로정렬.addWidget(버튼)

        self.setLayout(세로정렬)

        self.setWindowTitle('월급받아 집은 언제 살 수 있을까?')
        self.setWindowIcon(QIcon('img/캣네생선.png'))
        self.setGeometry(800, 300, 1000, 540)
        self.show()

    def 사용자입력그룹박스(self):
        self.월급_라벨 = QLabel('월급(만원)')
        self.월급_라인입력 = QLineEdit(self)
        self.월급_라인입력.setFixedWidth(200)

        self.세금_라벨 = QLabel('세금(%)')
        self.세금_라인입력 = QLineEdit(self)
        self.세금_라인입력.setFixedWidth(200)

        self.연인상율_라벨 = QLabel('연인상율(%)')
        self.연인상율_라인입력 = QLineEdit(self)
        self.연인상율_라인입력.setFixedWidth(200)

        self.집값_라벨 = QLabel('집값(억원)')
        self.집값_라인입력 = QLineEdit(self)
        self.집값_라인입력.setFixedWidth(200)

        self.그룹박스_사용자입력 = QGroupBox('사용자 입력 그룹박스')
        self.세로정렬_사용자입력 = QVBoxLayout()
        self.세로정렬_사용자입력.addWidget(self.월급_라벨)
        self.세로정렬_사용자입력.addWidget(self.월급_라인입력)
        self.세로정렬_사용자입력.addWidget(self.세금_라벨)
        self.세로정렬_사용자입력.addWidget(self.세금_라인입력)
        self.세로정렬_사용자입력.addWidget(self.연인상율_라벨)
        self.세로정렬_사용자입력.addWidget(self.연인상율_라인입력)
        self.세로정렬_사용자입력.addWidget(self.집값_라벨)
        self.세로정렬_사용자입력.addWidget(self.집값_라인입력)
        self.그룹박스_사용자입력.setLayout(self.세로정렬_사용자입력)
        self.그룹박스_사용자입력.setFixedWidth(330)

        return self.그룹박스_사용자입력

    def 연봉그룹박스(self):
        self.연봉_라벨하나 = QLabel('1년 : -원')
        self.연봉_라벨둘 = QLabel('2년 : -원')
        self.연봉_라벨셋 = QLabel('3년 : -원')
        self.연봉_라벨넷 = QLabel('4년 : -원')
        self.연봉_라벨다섯 = QLabel('5년 : -원')

        self.그룹박스_연봉 = QGroupBox('연봉')
        self.세로정렬_연봉 = QVBoxLayout()
        self.세로정렬_연봉.addWidget(self.연봉_라벨하나)
        self.세로정렬_연봉.addWidget(self.연봉_라벨둘)
        self.세로정렬_연봉.addWidget(self.연봉_라벨셋)
        self.세로정렬_연봉.addWidget(self.연봉_라벨넷)
        self.세로정렬_연봉.addWidget(self.연봉_라벨다섯)
        self.그룹박스_연봉.setLayout(self.세로정렬_연봉)

        return self.그룹박스_연봉

    def 실수령액그룹박스(self):
        self.실수령_라벨하나 = QLabel('1년 : -원')
        self.실수령_라벨둘 = QLabel('2년 : -원')
        self.실수령_라벨셋 = QLabel('3년 : -원')
        self.실수령_라벨넷 = QLabel('4년 : -원')
        self.실수령_라벨다섯 = QLabel('5년 : -원')

        self.그룹박스_실수령액 = QGroupBox('실수령액')
        self.세로정렬_실수령액 = QVBoxLayout()
        self.세로정렬_실수령액.addWidget(self.실수령_라벨하나)
        self.세로정렬_실수령액.addWidget(self.실수령_라벨둘)
        self.세로정렬_실수령액.addWidget(self.실수령_라벨셋)
        self.세로정렬_실수령액.addWidget(self.실수령_라벨넷)
        self.세로정렬_실수령액.addWidget(self.실수령_라벨다섯)
        self.그룹박스_실수령액.setLayout(self.세로정렬_실수령액)

        return self.그룹박스_실수령액

    def btnClick(self):
        입력값 = []
        입력값.append(float(self.월급_라인입력.text()))
        입력값.append(float(self.세금_라인입력.text()))
        입력값.append(float(self.연인상율_라인입력.text()))
        입력값.append(float(self.집값_라인입력.text()))
        
        일년차_연봉 = 입력값[0]*12
        이년차_연봉 = 일년차_연봉*(입력값[2]+100)/100
        삼년차_연봉 = 이년차_연봉*(입력값[2]+100)/100
        사년차_연봉 = 삼년차_연봉*(입력값[2]+100)/100
        오년차_연봉 = 사년차_연봉*(입력값[2]+100)/100

        self.연봉_라벨하나.setText(f'1년 : {일년차_연봉}만원')
        self.연봉_라벨둘.setText(f'2년 : {이년차_연봉}만원')
        self.연봉_라벨셋.setText(f'3년 : {삼년차_연봉}만원')
        self.연봉_라벨넷.setText(f'4년 : {사년차_연봉}만원')
        self.연봉_라벨다섯.setText(f'5년 : {오년차_연봉}만원')

        self.실수령_라벨하나.setText(f'1년 : {format(일년차_연봉-일년차_연봉*입력값[1]/100,".2f")}만원')
        self.실수령_라벨둘.setText(f'2년 : {format(이년차_연봉-이년차_연봉*입력값[1]/100,".2f")}만원')
        self.실수령_라벨셋.setText(f'3년 : {format(삼년차_연봉-삼년차_연봉*입력값[1]/100,".2f")}만원')
        self.실수령_라벨넷.setText(f'4년 : {format(사년차_연봉-사년차_연봉*입력값[1]/100,".2f")}만원')
        self.실수령_라벨다섯.setText(f'5년 : {format(오년차_연봉-오년차_연봉*입력값[1]/100,".2f")}만원')

        월급합 = 일년차_연봉 + 이년차_연봉 + 삼년차_연봉 + 사년차_연봉 + 오년차_연봉
        실수령합 = 월급합 - 월급합*입력값[1]/100
        집값차 = float(format(입력값[3]*10000-실수령합, ".0f"))

        if 집값차 >= 10000:
            self.합산.setText(f'* 5년 월급 합: {format(월급합,".0f")}만원  \n\n* 5년 실수령액 합 : {format(실수령합,".0f")}만원\n\n* 실수령액과 집값과의 차 : {int(집값차//10000)}억{int(집값차%10000)}만원')

        else:
            self.합산.setText(f'* 5년 월급 합: {format(월급합,".0f")}만원  \n\n* 5년 실수령액 합 : {format(실수령합,".0f")}만원\n\n* 실수령액과 집값과의 차 : {format(입력값[3]*10000-실수령합,".0f")}만원')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 월급받아집은언제()
프로그램무한반복.exec_()