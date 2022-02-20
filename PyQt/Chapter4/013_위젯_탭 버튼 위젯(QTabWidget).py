from PyQt5.QtWidgets import QWidget, QApplication,QTabWidget,QVBoxLayout
from PyQt5.QtCore import Qt
import sys

# 탭은 액셀 하단에 있는 Sheet와 같은 역할을 하는 창변환 기능

class 탭버튼위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.tab1 = QWidget() 
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        tabs = QTabWidget()
        
        tabs.addTab(self.tab1,'라이캣')
        tabs.addTab(self.tab2,'파이')
        tabs.addTab(self.tab3,'썬')
        tabs.setTabPosition(1) 
        tabs.setTabShape(1) 

        tabs.tabBarClicked.connect(self.clickedTab)
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        '''
        - addTab(탭에 넣을 위젯, 탭에 표시할 텍스트)
        - setTabPosition() : North(0), South(1), West(2), East(3) 로 가능 기본 = North
        - setTabShape() :  Rounded(0), Triangular(1) 기본 =0
        - tapBarClicked 시그널은 index 인수를 같이 넘겨줌
        '''

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 400)
        self.show()


    def clickedTab(self,index): # 인덱스를 받아 탭이 3개이므로 0~2 까지 있음 , 탭이 변경될 때마다 이미지가 바뀌는 함수(슬롯)
        if index == 0: 
            self.tab1.setStyleSheet('image : url(img/weniv-licat.png)')
        elif index == 1:
            self.tab2.setStyleSheet('image : url(img/weniv-pie.png)')
        else:
            self.tab3.setStyleSheet('image : url(img/weniv-sun.png)')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 탭버튼위젯()
프로그램무한반복.exec_()