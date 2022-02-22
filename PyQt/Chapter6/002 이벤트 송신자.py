from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,QLabel
from PyQt5.QtCore import Qt
import sys

class 이벤트송신자(QWidget): 

    def __init__(self):
        super().__init__()

        self.UI초기화()

    def UI초기화(self):
        self.btn1 = QPushButton("버튼 1" )
        self.btn2 = QPushButton("버튼 2" )
 
        self.btn1.clicked.connect(self.buttonClicked) # 시그널(buttonClicked)과 슬롯을 연결
        self.btn2.clicked.connect(self.buttonClicked) # 시그널(buttonClicked)과 슬롯을 연결

        self.label = QLabel('누가 시그널을 보냈을까?')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label,alignment=Qt.AlignCenter)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Event Sender')
        self.show()

    def buttonClicked(self): # sender() 함수는 누구로 부터 호출 받았는지 알려줌.
        sender = self.sender()
        self.label.setText(sender.text() + '이 보냈습니다.') # 시그널을 보낸 객체 이름text()로 값을 가져와 라벨에 표시


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 이벤트송신자()
프로그램무한반복.exec_()