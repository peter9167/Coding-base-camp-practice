from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel
from PyQt5.QtCore import Qt
import sys


class 시그널슬롯동작(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()
        

    def UI초기화(self):
        self.count = 0 
        btn = QPushButton('클릭')
        btn.clicked.connect(self.changeLabel) 

        self.label = QLabel(f"{self.count} 번 눌렸습니다.")
        # - count 변수는 버튼 클릭시 값이 증가하기 위해 self.count로 선언
        # - clicked 클릭시  시그널을 보내고 정의된 self.changeLabel(슬롯)에 보내어 이벤트를 처리

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn)
        self.setLayout(vbox)
      
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Signal and Slot')
        self.show()
  
    def changeLabel(self): 
        self.count += 1
        self.label.setText(f"{self.count} 번 눌렸습니다.")
        # - 슬롯 (slot)은 시그널에 어떻게 반응할지를 구현한 함수.
        # - 슬롯 = 이벤트 핸들러(이벤트를 처리할 때 사용되는 함수)
        # 해당 강좌와 함께 읽어보면 좋을 공식문서 : https://doc.qt.io/qtforpython/overviews/signalsandslots.html


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 시그널슬롯동작()
프로그램무한반복.exec_()