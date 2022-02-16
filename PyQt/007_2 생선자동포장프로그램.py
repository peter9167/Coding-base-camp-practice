# 마우스를 움직이는 이벤트, 키보드를 클릭하는 이벤트를 구현
# 자세한 내용 : https://pyautogui.readthedocs.io/en/latest/
import pyautogui #pip3 install pyautogui

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, QTimer


class 생선자동포장프로그램(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()


    # 전체 UI를 구성합니다. 생선포장수()는 라벨로 몇마리가 포장되었는지 표시할 것이고 대표이미지()는 이미지를 띄우는 것을, 포장버튼()은 포장 버튼을 누르면 self.포장카운트가 올라가게 할 것입니다. 그것을 대표 라벨에 출력하고요.
    def UI초기화(self):
        self.포장카운트 = 0
        self.클릭횟수카운트 = 0
        # self.포장카운트 : 얼마나 포장하였는지 저장한 변수, 클릭하면 +1 됩니다.
        # self.클릭횟수카운트 : 클릭이 얼마나 되었는지 확인하고 입력된 횟수랑 비교하여 프로그램을 Stop하는 역활로 사용됩니다.

        self.생선포장수()
        self.대표이미지()
        self.포장버튼()

        self.setWindowTitle('생선 자동 포장 프로그램')
        self.setGeometry(400, 300, 580, 500)
        self.show()

    def 대표이미지(self):
        self.대표이미지라벨 = QLabel(self)
        self.대표이미지라벨.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44))
        self.대표이미지라벨.move(10, 10)

    def 생선포장수(self):
        self.생선포장수라벨 = QLabel('00 마리가 포장되었습니다.', self)
        self.생선포장수라벨.setFont(QFont("Helvetica", pointSize=22, weight=2))
        self.생선포장수라벨.move(30, 70)
    
    def 포장버튼(self):
        self.생선준비버튼 = QPushButton('생선준비', self)
        self.생선준비버튼.move(30, 150)
        self.생선준비버튼.setFixedSize(250, 40)

        self.생선다듬기버튼 = QPushButton('생선다듬기', self)
        self.생선다듬기버튼.move(300, 150)
        self.생선다듬기버튼.setFixedSize(250, 40)

        self.생선포장버튼 = QPushButton('생선포장', self)
        self.생선포장버튼.move(30, 200)
        self.생선포장버튼.setFixedSize(520, 40)
        self.생선포장버튼.clicked.connect(self.countClick)

        self.포장시작버튼 = QPushButton('포장시작', self)
        self.포장시작버튼.move(300, 300)
        self.포장시작버튼.setFixedSize(250, 40)
        self.포장시작버튼.clicked.connect(self.startClick)

        self.간격입력창 = QLineEdit(self)
        self.간격입력창.setPlaceholderText('클릭 간격/ (초)') # setPlaceholderText : 워터마크를 활용한 표시 입력시, 힌트를 줄 때 유용
        self.간격입력창.move(30, 300)
        self.간격입력창설명라벨 = QLabel('몇 초 간격으로 포장할지 입력하세요.', self)
        self.간격입력창설명라벨.setFont(QFont("Helvetica", pointSize=7))
        self.간격입력창설명라벨.move(30, 340)

        self.횟수입력창 = QLineEdit(self)
        self.횟수입력창.setPlaceholderText('클릭 횟수')
        self.횟수입력창.move(30, 400)
        self.횟수입력창설명라벨 = QLabel('몇 회 포장할지 입력하세요.', self)
        self.횟수입력창설명라벨.setFont(QFont("Helvetica", pointSize=7))
        self.횟수입력창설명라벨.move(30, 440)

    # 스타트 버튼이 클릭되면 startClick 함수와 연결되게 됩니다. QTimer객체를 생성하고 x, y변수에 좌표값을 입력합니다. 여기서 좌표는 윈도우 상단에서부터 x, y값입니다. int값이기 때문에 정수로 더할 수 있습니다. 단위는 px입니다.

    # 지연시간 변수에 입력된 지연시간 값을 넣습니다. 시간 단위는 밀리세컨드입니다. 클릭된 횟수를 알아보기 위한 변수를 0으로 초기화 하고 타이머를 시작합니다. 단위가 밀리세컨드이기 때문에 1000을 곱하여 초 단위로 실행하도록 합니다.
    def startClick(self): 
        self.timer = QTimer()
        self.x = 550 #전체 윈도우에서 좌표값을 가져옴
        self.y = 510
        self.delay = int(self.간격입력창.text())

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouseClick) # 타이머가 종료되면 마우스로 버튼을 클릭하게 되고 아래 코드가 실행되면서 포장 마리수가 올라가게 됩니다.

    def mouseClick(self):
        # - pyautogui를 통해 파라미터로 넘겨받은 좌표를 클릭합니다.
        # - 클릭된 횟수를 1씩 증가합니다(여기서는 1초 단위로 1씩 증가)
        # - 목표인 클릭횟수에 도달하면 타이머를 종료합니다.
        pyautogui.click(self.x, self.y)
        self.클릭횟수카운트 += 1

        if self.클릭횟수카운트 == int(self.횟수입력창.text()):
            self.timer.stop()
     
    def countClick(self):
        self.포장카운트 += 1
        self.생선포장수라벨.setText(f'{str(self.포장카운트)} 마리가 포장되었습니다.')
        

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 생선자동포장프로그램()
프로그램무한반복.exec_()