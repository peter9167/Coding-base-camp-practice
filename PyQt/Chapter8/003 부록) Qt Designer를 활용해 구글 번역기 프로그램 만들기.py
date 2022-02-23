from PyQt5 import uic # uic 라이브러리는 Qt Designer로 작성된 파일을 다룰 수 있음
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from googletrans import Translator

ui = uic.loadUiType("chapter8/test.ui")[0] # uic.loadUiType("경로/파일이름.ui")[0] 를 통해 만든 UI파일을 가져옴

class 구글번역프로그램(QWidget,ui): # 파라미터에 ui를 추가

    def __init__(self):
        super().__init__()
        self.setupUi(self) # 기존에 사용했던 initUI가 없어지고 self.setupUi(self)가 생성
        self.translator = Translator() 
        self.transBtn.clicked.connect(self.translate)
        self.changeBtn.clicked.connect(self.changeLanguage)
        # 더불어 기존에 번역하는 함수들은 재활용 하고 슬롯과 시그널을 연결해주는 코드만 들어감

    def translate(self):
        if self.label1.text() == '한국어': 

            text_kor = self.edit1.toPlainText() 
            text_en = self.translator.translate(text_kor,src='ko',dest='en').text
            self.edit2.setText(text_en)  

        elif self.label1.text() == '영어': 
            text_kor = self.edit1.toPlainText() 
            text_en = self.translator.translate(text_kor,src='en',dest='ko').text 
            self.edit2.setText(text_en)
        


    def changeLanguage(self): 
        if self.label1.text() == '한국어':
            t1, t2 = self.edit1.toPlainText(), self.edit2.toPlainText() 
            self.label2.setText('한국어')
            self.label1.setText('영어')
            self.edit1.setText(t2)
            self.edit2.setText(t1)

        else:
            t1, t2 = self.edit1.toPlainText(), self.edit2.toPlainText()
            self.label2.setText('영어')
            self.label1.setText('한국어')
            self.edit1.setText(t2)
            self.edit2.setText(t1)

    
    app = QApplication(sys.argv)
    ex = 구글번역프로그램()
    ex.show() # show()를 통해 UI를 화면에 띄워줍니다.
    app.exec_()