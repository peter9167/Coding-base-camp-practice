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

        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        temp = pg.plot(x, y, pen=None, symbol='o')
        
        self.setCentralWidget(temp) # 창을 덮어씀으로써 창 하나로 병합
        
        self.setWindowIcon(QIcon('img/캣네생선.png'))
        self.setGeometry(300, 300, 400, 300)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그래프()
프로그램무한반복.exec_()