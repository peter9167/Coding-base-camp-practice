from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
import sys

# QLabel은 이미지, 글자, 영상 등을 담을 수 있는 Object. 사용자와 상호작용하는 라이브러리는 아님
# [QLabel - Qt for Python](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html)
# QLabel에서 담을 수 있는 타입은 아래와 같다. 여기서 Rich Text는 마크업 언어 -> https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html

class 라벨(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        
        # - font() : 해당 라벨의 폰트 값을 가져옴
        # - setPointSize(15) : 폰트 크기를 15로 설정
        # - setItalic(True) : 이탤릭체 설정
        # - setFamily('Helvetica') : 글꼴 설정
        # - setBold(True) : 진한 글씨체 설정

        label_1 = QLabel(self)
        label_1.setText('라벨 1') 
        label_1.setAlignment(Qt.AlignLeft) 

        label_2 = QLabel('라벨 2',self) 
        label_2.setAlignment(Qt.AlignRight) 

        label_3 = QLabel('라벨 3',self)
        
        font_1 = label_1.font() # font() : 해당 라벨의 폰트 값을 가져옴
        font_1.setPointSize(15) # setPointSize(15) : 폰트 크기를 15로 설정
        font_1.setItalic(True)  # setItalic(True) : 이탤릭체 설정

        font_2 = label_2.font()
        font_2.setPointSize(20)  
        font_2.setFamily('Helvetica') # setFamily('Helvetica') : 글꼴 설정

        font_3 = label_3.font()
        font_3.setPointSize(30)
        font_3.setBold(True) # setBold(True) : 진한 글씨체 설정

        label_1.setFont(font_1) 
        label_2.setFont(font_2)
        label_3.setFont(font_3)

        vbox = QVBoxLayout() 
        vbox.addWidget(label_1) 
        vbox.addWidget(label_2)
        vbox.addWidget(label_3, alignment=Qt.AlignCenter) # alignment=Qt.AlignCenter : 가운데 정렬

        self.setLayout(vbox)
        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 400, 200)
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 라벨()
프로그램무한반복.exec_()