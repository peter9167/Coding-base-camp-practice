import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout  
from PyQt5.QtCore import Qt


class 격자레이아웃(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        insert = QPushButton('Insert') 
        home = QPushButton('Home')
        pageUp = QPushButton('Page Up')
        delete = QPushButton('Delete')
        end = QPushButton('End')
        pageDown = QPushButton('Page Down')
        keyboard = QLabel('KeyBoard')

        grid = QGridLayout()
        grid.setSpacing(15) 

        grid.addWidget(insert, 0, 0) 
        grid.addWidget(home, 0, 1) 
        grid.addWidget(pageUp, 0, 2)

        grid.addWidget(delete, 1, 0)
        grid.addWidget(end, 1, 1)
        grid.addWidget(pageDown,1,2)

        grid.addWidget(keyboard, 2, 0, 2, 3, alignment=Qt.AlignHCenter)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Review')
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 격자레이아웃()
프로그램무한반복.exec_()