from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QProgressBar,QLabel
from PyQt5.QtCore import QBasicTimer,Qt
import sys

# QProgressBar : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QProgressBar.html

class 진행바(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.bar1 = QProgressBar(self) 
        self.bar1.setOrientation(Qt.Vertical) 
        self.bar1.setGeometry(50, 20, 50, 300)

        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(150,100,250,30)
        self.bar2.setRange(0,50) 

        self.label1 = QLabel('이 바의 범위는 ' + str(self.bar2.minimum())+" 부터 " +
                             str(self.bar2.maximum())+" 입니다.", self)
        self.label1.move(150,180)
        
        self.label2 = QLabel('이곳에 첫 번째 바의 값이 나옵니다.',self)
        self.label2.move(130,300)
        

        self.btn = QPushButton('시작', self) 
        self.btn.move(40, 330)
        self.btn.clicked.connect(self.runTimer)  

        self.value = 0 
        self.timer = QBasicTimer() 
        self.bar1.valueChanged.connect(self.changeValue)

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('QProgressBar')
        self.show()

    def runTimer(self): 
        
        if self.timer.isActive():  
            self.timer.stop() 
            self.btn.setText('시작')
        else:
            self.timer.start(self.bar1.maximum(), self)  
            
            self.btn.setText('중지')

    def timerEvent(self, event): 

        if self.value >= self.bar1.maximum():  
            self.timer.stop()  
            self.btn.setText('완료')  
            return  

        self.value +=1   
        self.bar1.setValue(self.value)  

    def changeValue(self):
        self.label2.setText(str(self.bar1.value()))


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 진행바()
프로그램무한반복.exec_()