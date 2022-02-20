from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import sys

# QLineEdit 에 자세한 내용은 아래 링크!
# https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLineEdit.html

class 한줄입력기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.label =QLabel(self) 
        self.label.move(30,20)

        self.ledit = QLineEdit(self)
        self.ledit.move(30, 50) 
        self.ledit.textChanged[str].connect(self.changed1)  # 여기서 시그널 중 textChanged[str]를 사용하여 입력창의 텍스트가 수정되고 있는 상태면 changed1 함수를 연결.
                                                            # 함수에서는 라벨 텍스트 수정과 사이즈 조절을 하고 있습니다.

        self.ledit.returnPressed.connect(self.changeText)   # returnPressed 시그널을 활용하여 엔터키를 입력하면 chageText 이벤트가 발생하도록 함.
                                                            # 여기서는 텍스트 에디터에 입력된 문자로 라벨 텍스트를 업데이트.
     
        self.label2 = QLabel(self)
        self.label2.move(30,100)

        ledit2 = QLineEdit(self)
        ledit2.move(30,130)
        ledit2.setEchoMode(2) # 미리 정의된 매서드 중 setEchoMode를 사용하여 입력된 문자를 라벨에 업데이트 함
        # setEchoMode()  함수 
        # QLineEdit.Normal : 입력된 문자 표시 (기본값) / 숫자 = 0
        # QLineEdit.NoEcho : 문자열 표시 x / 숫자 = 1
        # QLineEdit.Password : 입력된 문자 대신 비밀번호용 문자(*) 로 표시 / 숫자 = 2
        # QLineEdit.PasswordEchoOnEdit : 입력시에 문자 표시, 수정중에는 다른 문자 표시 / 숫자 =3
        
        ledit2.textChanged[str].connect(self.changed2)
 
        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def changed1(self): # ledit.textChanged[str]를 사용하여 이벤트 발생
        self.label.setText('편집중입니다. 마치실려면 Enter를 눌러주세요') 
        self.label.adjustSize() 

    def changeText(self): # returnPressed 시그널을 통해 이벤트 발생
        self.label.setText(self.ledit.text())

    def changed2(self,text): # ledit2.textChanged[str]를 사용하여 이벤트 발생
        self.label2.setText(text)
        self.label2.adjustSize()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 한줄입력기()
프로그램무한반복.exec_()