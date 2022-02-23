from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from googletrans import Translator  # google API를 사용하기 위해 pip 명령어를 사용해 모듈을 설치하고, import
                                    # 구글 번역 API 공식문서 : https://py-googletrans.readthedocs.io/en/latest/
import sys

class 번역프로그램(QWidget):

    def __init__(self):
        super().__init__() # super().__init__ : 상속받고 있는 QWidget에 __init__()
        self.translator = Translator() # translator(인스턴스)를 통해 Translator를 가져옴
        self.UI초기화() # 인스턴스 함수 호출

    def UI초기화(self):
        self.label1 = QLabel('한국어', self) # 리벨(label1) 생성
        self.lable2 = QLabel('영어', self) # 라벨(label2) 생성

        self.edit1 = QTextEdit(self)
        self.edit2 = QTextEdit(self)

        self.transBtn = QPushButton('번역하기', self)
        self.changeBtn = QPushButton('언어 바꾸기', self)

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1.addWidget(self.label1,alignment=Qt.AlignCenter)
        vbox1.addWidget(self.edit1)
        vbox2.addWidget(self.lable2,alignment=Qt.AlignCenter)
        vbox2.addWidget(self.edit2)

        hbox  = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        layout = QVBoxLayout() 

        layout.addLayout(hbox) 
        layout.addWidget(self.transBtn)  # 버튼(transBtn)이 클릭되면 
        layout.addWidget(self.changeBtn) # 버튼(changeBtn)이 클릭되면 
        self.setLayout(layout)
        

        self.transBtn.clicked.connect(self.translate) # 번역을 실행하거나 언어를 서로 변경해주는 함수(translate)와 연결
        
        self.changeBtn.clicked.connect(self.changeLanguage) # 번역을 실행하거나 언어를 서로 변경해주는 함수(changeLanguage)와 연결

        self.setWindowTitle('(주)캣네생선 번역기') # 창 제목
        self.setGeometry(200, 200, 400, 400) # 창 크기
        self.show() # 창을 보여줌

    def translate(self):
        # 사용자가 입력하는 입력창의 라벨이 한국어라면, 입력창을 플레인 텍스트를 가져옴. 번역한 것을 가지고 translator.translate(번역할 글자, src=번역할 언어,  dest=번역된 언어).text 매서드를 사용하면 번역된 text를 얻음. 뒤에 꼭 .text를 붙여야 번역된 글자를 받을 수 있으니 주의
        if self.label1.text() == '한국어': 
            text_kor = self.edit1.toPlainText() 
            text_en = self.translator.translate(text_kor,src='ko',dest='en').text
            self.edit2.setText(text_en)
        elif self.label1.text() == '영어': 
            text_kor = self.edit1.toPlainText() 
            text_en = self.translator.translate(text_kor,src='en',dest='ko').text 
            self.edit2.setText(text_en)

    def changeLanguage(self): 
        # 번역될 언어, 글자 번역될 언어, 글자를 서로 바꿔주는 함수를 구현하면 번역기 프로그램이 완성
        if self.label1.text() == '한국어':
            t1, t2 = self.edit1.toPlainText(), self.edit2.toPlainText() 
            self.lable2.setText('한국어')
            self.label1.setText('영어')
            self.edit1.setText(t2)
            self.edit2.setText(t1)

        else:
            t1, t2 = self.edit1.toPlainText(), self.edit2.toPlainText()
            self.lable2.setText('영어')
            self.label1.setText('한국어')
            self.edit1.setText(t2)
            self.edit2.setText(t1)


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 번역프로그램()
프로그램무한반복.exec_()