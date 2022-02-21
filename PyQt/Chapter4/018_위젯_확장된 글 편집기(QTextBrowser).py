from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QTextBrowser, QLineEdit
from PyQt5.QtCore import Qt
import sys

### QTextBrowser

# QTextBrowser는 앞서 배웠던 QTextEdit의 확장형입니다. 여기서는 하이퍼링크, 마크업 언어가 사용 가능
# 공식문서 : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTextBrowser.html

class 확장된글편집기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.line_edit = QLineEdit() # LineEdit : 한 줄 입력기
        self.line_edit.returnPressed.connect(self.addText) # 입력기에서 Enter를 치거나 (returnPressed) 버튼을 누르면 시그널 발생

        self.btn_add = QPushButton('입력')
        self.btn_add.clicked.connect(self.addText)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True) # setAcceptRichText(True) : 리치 텍스트 사용 여부 : 서식있는 텍스트를 사용가능
        self.tb.setOpenExternalLinks(True) # setOpenExternalLinks(True)  : 외부링크를 허용하는지에 대한 여부
        self.tb.append('일반 플래인 텍스트입니다.')
        self.tb.append('''
        <p style="text-align: center; font-weight:bold;">Bold</p>
        <i>Italic</i>
        <p style="color: red; text-align: center;">Red</p>
        <p style="color: blue; text-align: center;"><b>Blue</b></p>
        <p style="font-size: 20px; text-align: center;"><i>20px<i></p>
        <p style="font-size: 40px; text-align: center;">40px</p>
        <a href="https://www.naver.com">네이버</a>
        <a href="https://www.inflearn.com/instructors/19857/courses">제주 코딩베이스 캠프 강의 목록</a>
        <a href="https://www.youtube.com/channel/UC4GnvNKtuJ4cqWsYjxNxAEQ">저희의 유튜브 입니다.</a>
        <img src= "img/weniv-licat.png" width ="100" height = "100">''')

        self.tb.setAlignment(Qt.AlignCenter)
        self.btn_clear = QPushButton('지우기')
        self.btn_clear.clicked.connect(self.clearText)

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.btn_add)
        vbox.addWidget(self.btn_clear)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 400)
        self.show()

    def addText(self): # 입력기에서 입력된 텍스트를 가져와 TextBrowser에 추가하고(append) 입력된 텍스트를 지움
        text = self.line_edit.text()
        self.tb.append(text)
        self.line_edit.clear()

    def clearText(self):
        self.tb.clear() # clear()를 통해 TextBrowser에 있는 텍스트를 전부 지움


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 확장된글편집기()
프로그램무한반복.exec_()