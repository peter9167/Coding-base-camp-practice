import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
# pip install pyqtgraph
import numpy as np

class 그래프(QWidget): 
    def __init__(self): 
        super().__init__() 
        버튼 = QPushButton('hello') 
        라벨 = QLabel('world', self)

        pg.setConfigOption('background', 'w')
        그래프 = pg.plot([1,4,2,3,5])

        가로정렬 = QHBoxLayout() 
        가로정렬.addWidget(버튼) 
        가로정렬.addWidget(라벨)
        가로정렬.addWidget(그래프)

        self.setLayout(가로정렬) 
        self.setGeometry(300, 300, 400, 400)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그래프()
프로그램무한반복.exec_()