from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys

# QMessageBox는 질문창 또는 사용자에게 정보를 주거나 받을 수 있는 창을 만들 수 있다.
# 공식문서 : https://doc.qt.io/qt-5/qmessagebox.html

class 메세지다이얼로그(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        btn = QPushButton('프로그램 종료',self)
        btn.clicked.connect(self.close) # close() 함수(슬롯)은 이미 정의 되어있기 때문에 재정의
        btn.move(20, 50)

        btn2 = QPushButton("에러 발생",self)
        btn2.move(180,50)
        btn2.clicked.connect(self.critical)

        btn3 = QPushButton("경고 발생",self)
        btn3.move(320,50)
        btn3.clicked.connect(self.warning)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 450, 200)
        self.show()

    def close(self): 

        question = QMessageBox.question(self, '질문 메세지 창',\
                               '정말 종료하시겠습니까?',\
                               QMessageBox.Yes | QMessageBox.No , QMessageBox.No) # QMessageBox.question(부모위젯,창 이름,나타날 메세지,[추가할 버튼] ,옵션:기본으로 선택된 버튼)
        
        if question == QMessageBox.Yes: # 만약 Yes 버튼이 눌렀다면 프로그램을 종료
            super().close()
          
    def critical(self):
        cri = QMessageBox.critical(self, '에러 창',\
                               '심각한 에러가 생겼습니다.',\
															 QMessageBox.Help| QMessageBox.Reset | QMessageBox.Apply)

    def warning(self):
        warn = QMessageBox.warning(self, "경고 창",\
                               '에러가 날 수 있는 문제가 생겼습니다.',
															 QMessageBox.Ok|QMessageBox.Retry|QMessageBox.Ignore)

    # 각 버튼에 대응하여 동작하는 메세지 박스를 생성


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 메세지다이얼로그()
프로그램무한반복.exec_()