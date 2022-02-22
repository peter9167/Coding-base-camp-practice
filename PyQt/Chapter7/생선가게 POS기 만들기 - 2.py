from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import *

class 생선가게POS기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.s = ''

        ## number ##
        self.one = QPushButton('1')
        self.one.clicked.connect(lambda:self.clickedNum('1'))

        self.two = QPushButton('2')
        self.two.clicked.connect(lambda:self.clickedNum('2'))

        self.three = QPushButton('3')
        self.three.clicked.connect(lambda:self.clickedNum('3'))

        self.four = QPushButton('4')
        self.four.clicked.connect(lambda:self.clickedNum('4'))

        self.five = QPushButton('5')
        self.five.clicked.connect(lambda:self.clickedNum('5'))

        self.six = QPushButton('6')
        self.six.clicked.connect(lambda:self.clickedNum('6'))

        self.seven = QPushButton('7')
        self.seven.clicked.connect(lambda:self.clickedNum('7'))

        self.eight = QPushButton('8')
        self.eight.clicked.connect(lambda:self.clickedNum('8'))

        self.nine = QPushButton('9')
        self.nine.clicked.connect(lambda:self.clickedNum('9'))

        self.zero = QPushButton('0')
        self.zero.clicked.connect(lambda:self.clickedNum('0'))

        ## calculator ##
        self.plus = QPushButton('+')
        self.plus.clicked.connect(lambda:self.clickedNum('+'))

        self.minus = QPushButton('-')
        self.minus.clicked.connect(lambda:self.clickedNum('-'))

        self.division = QPushButton('/')
        self.division.clicked.connect(lambda:self.clickedNum('/'))

        self.multiply = QPushButton('*')
        self.multiply.clicked.connect(lambda:self.clickedNum('*'))

        self.dot = QPushButton('.')
        self.dot.clicked.connect(lambda:self.clickedNum('.'))

        self.squared = QPushButton('x^2')
        self.squared.clicked.connect(lambda:self.clickedNum('**2'))

        self.remainder = QPushButton('%')
        self.remainder.clicked.connect(lambda:self.clickedNum('%'))

        self.clear = QPushButton('Clear')
        self.clear.clicked.connect(self.clearText)
        self.back = QPushButton('Back')
        self.back.clicked.connect(self.backText)
        self.enter = QPushButton("=")
        self.enter.clicked.connect(self.calculateResult)

        self.lcd = QLineEdit('')
        self.lcd.setReadOnly(True)
        self.lcd.setAlignment(Qt.AlignRight)
        self.lcd.setStyleSheet('font-size:15px;font-weight:bold;padding:10px;')

        self.label = QLabel('계산기')

        grid = QGridLayout()
        grid.setSizeConstraint(QLayout.SetFixedSize)

        grid.addWidget(self.label, 0, 0, 1, 4, alignment=Qt.AlignCenter)
        grid.addWidget(self.lcd, 1, 0, 1, 4)

        grid.addWidget(self.plus, 2, 0)
        grid.addWidget(self.minus, 2, 1)
        grid.addWidget(self.multiply, 2, 2)
        grid.addWidget(self.division, 2, 3)

        grid.addWidget(self.seven, 3, 0)
        grid.addWidget(self.eight, 3, 1)
        grid.addWidget(self.nine, 3, 2)
        grid.addWidget(self.clear, 3, 3)

        grid.addWidget(self.four, 4, 0)
        grid.addWidget(self.five, 4, 1)
        grid.addWidget(self.six, 4, 2)
        grid.addWidget(self.back, 4, 3)

        grid.addWidget(self.one, 5, 0)
        grid.addWidget(self.two, 5, 1)
        grid.addWidget(self.three, 5, 2)
        grid.addWidget(self.squared, 5, 3)

        grid.addWidget(self.remainder, 6, 0)
        grid.addWidget(self.zero, 6, 1)
        grid.addWidget(self.dot, 6, 2)
        grid.addWidget(self.enter, 6, 3)

        self.setLayout(grid)
        
        self.setWindowTitle("계산기")
        self.show()
        
    def clickedNum(self, text):
        self.s += text
        self.lcd.setText(self.s)

    def calculateResult(self):
        self.lcd.setText(str(eval(self.s)))
        self.s = ''

    def clearText(self):
        self.lcd.setText('')
        self.s = ''

    def backText(self):
        self.s = self.s[:-1]
        self.lcd.setText(self.s)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.calculateResult()
        elif event.key() == Qt.Key_Backspace:
            self.backText()
        elif event.key() == Qt.Key_Escape:
            self.close()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 생선가게POS기()
프로그램무한반복.exec_()