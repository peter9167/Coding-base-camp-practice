from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
import sys

# 다이얼 로그는 user와 프로그램 간에 의사소통을 하는 중요한 도구
# 간단한 입력부터 file까지 다양한 입력을 할 수 있도록 도와줌

class 입력다이얼로그(QWidget):
    def __init__(self):
        super().__init__()
        self.day = ['월', '화', '수', '목', '금'] # 리스트 호출을 사용하기 위해 요일을 리스트로 표현 = getItem()을 위한 리스트 생성
        self.UI초기화()

    def UI초기화(self):
        self.btn1 = QPushButton('이름 입력', self)
        self.btn1.move(30, 30)
        self.btn1.clicked.connect(self.showDialog1)

        self.btn2 = QPushButton('요일 선택', self)
        self.btn2.move(30, 80)
        self.btn2.clicked.connect(self.showDialog2)

        self.btn3 = QPushButton('일자 선택', self)
        self.btn3.move(30, 130)
        self.btn3.clicked.connect(self.showDialog3)

        # 테스트를 위한 여러 버튼을 만들고 시그널과 슬롯을 연결합니다.

        self.label1 = QLabel('이곳에 이름이 표시됩니다.', self)
        self.label1.move(180, 35)
        self.label1.setFixedSize(220, 20)

        self.label2 = QLabel('이곳에 요일이 표시됩니다.', self)
        self.label2.move(180, 85)
        self.label2.setFixedSize(220, 20)

        self.label3 = QLabel('이곳에 날짜가 표시됩니다.', self)
        self.label3.move(180, 135)
        self.label3.setFixedSize(220, 20)

        self.setWindowTitle('QInputDialog')
        self.setGeometry(300, 300, 450, 200)
        self.show()

    def showDialog1(self):
        text, flag = QInputDialog.getText(self, '입력창', '이름을 입력하세요.')
        if flag:
            self.label1.setText(str(text))

        # - getText(부모위젯,창이름,표시할 메세지) → text와 flag로 반환
        # - flag : 만약 다이얼로그에서 OK버튼을 누르면 flag는 True가 되어 라벨에 입력된 텍스트로 업데이트

    def showDialog2(self):
        text, flag = QInputDialog.getItem(self, '리스트 호출 입력창',\
                                                '요일을 선택하세요', self.day)
        if flag:
            self.label2.setText(str(text))

        # - getItem(부모위젯,창이름,표시할메세지,선택할 리스트) → text와 flag로 반환
        # - 값을 선택하고 OK버튼을 누르면 해당 값으로 라벨에 업데이트

    def showDialog3(self):
        number, flag = QInputDialog.getInt(self, "요일 선택 창",\
                                                 "요일을 선택하세요", min=1, max=31)
        if flag:
            self.label3.setText(str(number)+"일")

        # - getInt(부모위젯,창이름,표시할메세지) → number와 flag로 반환
        # - 파라미터 옵션으로 1부터 31까지만 선택하도록 만듦

        
프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 입력다이얼로그()
프로그램무한반복.exec_()