from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys

# 텍스트 편집기는 글자를 편집할 수 있는 위젯 
# 일반적 편집 기능 뿐만 아니라 ZoomIn, ZoomOut 등 다양한 확장 기능을 제공
# 공식문서 : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTextEdit.html

class 글편집기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.label1 = QLabel('텍스트 편집기')
        self.text_edit = QTextEdit()
        
        self.text_edit.setAcceptRichText(False)
        self.label2 = QLabel('글자수를 세어볼까요?')
        btn_clear = QPushButton('내용 지우기') 
        btn_color = QPushButton('빨간색으로 변경')

        btn_clear.clicked.connect(self.clear_text)  
        btn_color.clicked.connect(self.change_color)  
        self.text_edit.textChanged.connect(self.check_text_lengh)  

        '''
        - setAcceptRichText(True/False) : 리치텍스트를 허용하는 여부, False이면 플레인 텍스트
        - 다음 강의 예제에서 리치 텍스트와 플레인 텍스트의 차이를 알 수 있음
        - textChanged : 텍스트 입력기에서 텍스트가 수정되면 시그널 발생
        '''

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.label2)
        vbox.addWidget(btn_clear)
        vbox.addWidget(btn_color)

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def check_text_lengh(self):
        text = self.text_edit.toPlainText() # toPlainText() : 현재 입력된 텍스트를 플레인텍스트로 먼저 변경
        self.label2.setText(f'글자수는 : {len(text)} 입니다.') # len()을 활용해 글자수를 라벨에 업데이트

    def clear_text(self):
        self.text_edit.clear() # clear() : 텍스트 편집기에 입력된 내용을 지움

    def change_color(self):
        self.text_edit.setTextColor(QColor(252, 32, 12)) # setTextColor(): 텍스트를 지정된 색으로 변경 기본은 검정색 ,누르면 그때부터 지정된 색으로 작성


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 글편집기()
프로그램무한반복.exec_()