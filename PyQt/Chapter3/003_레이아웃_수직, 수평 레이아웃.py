import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

class 레이아웃(QWidget):
    
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        label1_img = QLabel() 
        label1_img.setPixmap(QPixmap('img/weniv-licat.png'))
        label1 = QLabel('내 이름은 라이캣!')

        label2_img = QLabel()
        label2_img.setPixmap(QPixmap('img/weniv-mura.png'))
        label2 = QLabel('내 이름은 무라!')

        # 여기서 주의하셔야 할 것은 `addWidget`과 `addLayout`을 구분하는 것입니다. 수평, 수직 또는 격자로 레이아웃 구성을 하신 다음, 또다른 수평, 수직 또는 격자로 구성한 레이아웃에 삽입하려 하신다면 `addWidget`이 아니라 `addLayout`을 통해 레이아웃을 추가하셔야 합니다.

        #- QHBoxLayout : 수평(Horizontal)으로 쌓는 레이아웃

        # [QHBoxLayout - Qt for Python](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QHBoxLayout.html)

        #- QVBoxLayout : 수직(Vertical)으로 쌓는 레이아웃

        vbox1 = QVBoxLayout() 
        vbox2 = QVBoxLayout()
        
        vbox1.addWidget(label1_img) 
        vbox1.addWidget(label1) 

        vbox2.addWidget(label2_img) 
        vbox2.addWidget(label2) 

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)  
        hbox.addLayout(vbox2) 
       
        self.setLayout(hbox) 

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 400, 300)
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 레이아웃()
프로그램무한반복.exec_()
