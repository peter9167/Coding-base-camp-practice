import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
# pip install pyqtgraph
import numpy as np

class 그래프(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        pg.setConfigOption('background', 'w') # 배경화면(background)을 w(white)로 지정
        self.setCentralWidget(pg.plot([1,4,2,3,5]))
        
        self.setWindowIcon(QIcon('img/캣네생선.png'))
        self.setGeometry(300, 300, 400, 300)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그래프()
프로그램무한반복.exec_()