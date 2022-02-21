from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,\
                            QLabel, QFontDialog, QColorDialog, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys

# HTML로 매핑을 하자면, form에 input을 만드는 것
# 공식문서(QColorDialog) : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QColorDialog.html
# 공식문서 (QFontDialog) : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFontDialog.html
class 글꼴컬러설정다이얼로그(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.label = QLabel('안녕하세요! 제주코딩베이스 캠프 PyQt5 강좌 입니다!', self)
        self.label.setAlignment(Qt.AlignCenter) 

        btn1 = QPushButton('폰트 선택', self)
        btn1.clicked.connect(self.showFont) 

        color = QColor(Qt.black) 

        self.colorFrame = QFrame(self)
        self.colorFrame.setStyleSheet(
            f'background-color: {color.name()};')  
        

        btn2 = QPushButton('색상 선택', self)
        btn2.clicked.connect(self.showColor) 
        # QColor(Qt.색상) 또는 QColor(r,g,b)으로도 사용가능

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn1)
        vbox.addWidget(self.colorFrame)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        self.setWindowTitle('QFont, QColor Dialog')
        self.setGeometry(300, 300, 450, 300)
        self.show()

    def showFont(self):
        font, flag = QFontDialog.getFont() # getFont()로 폰트값과 bool값을 가져옴

        if flag: 
            self.label.setFont(font)
        else:
            self.label.setText("선택 되지 않았어요! 다시 한번 선택해주세요!")
        # 만약 글꼴을 선택하고 ok버튼을 클릭하면 해당 값으로 글꼴을 변경하고 아니라면 라벨에 선택되지 않았다는 문구를 업데이트

    def showColor(self):
        color = QColorDialog.getColor() # getColor() 로 현재 선택된 값을 가져옵니다. 단,bool값은 가져오지 못함

        if color.isValid(): 
            self.colorFrame.setStyleSheet(f'background-color: {color.name()}')
           
        else: 
            self.colorFrame.setStyleSheet("image : url(img/weniv-licat.png)")
        # 대신 isValid로 유효한지 즉, 컬러가 잘 선택되었는지 확인해 컬러값으로 Frame을 변경, 아니라면 라이캣이미지로 변경


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 글꼴컬러설정다이얼로그()
프로그램무한반복.exec_()