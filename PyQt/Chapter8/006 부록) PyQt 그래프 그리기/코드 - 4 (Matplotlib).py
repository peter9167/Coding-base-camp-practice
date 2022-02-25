import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fc

class 그래프(QWidget): 
    def __init__(self): 
        super().__init__() 
        버튼 = QPushButton('hello') 
        라벨 = QLabel('world', self)

        self.fig = plt.Figure()
        ax = self.fig.add_subplot(1, 1, 1)
        ax.grid() # 격자 무늬
        ax.plot([1, 2, 3], [10, 20, 30])

        self.canvas = fc(self.fig)

        가로정렬 = QHBoxLayout() 
        가로정렬.addWidget(버튼) 
        가로정렬.addWidget(라벨)
        가로정렬.addWidget(self.canvas) # 레이아웃이 아니지만 웨젯처럼 사용

        self.setLayout(가로정렬) 
        self.setGeometry(300, 300, 800, 400)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그래프()
프로그램무한반복.exec_()