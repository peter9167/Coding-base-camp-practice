from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QProgressBar,QLabel
from PyQt5.QtCore import QBasicTimer,Qt
import sys

# QProgressBar : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QProgressBar.html

class 진행바(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self): 
        self.bar1 = QProgressBar(self) # QProgressBar 생성
        self.bar1.setOrientation(Qt.Vertical) 
        self.bar1.setGeometry(50, 20, 50, 300) # (x, y, width, height)

        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(150,100,250,30)
        self.bar2.setRange(0,50) 

        self.label1 = QLabel('이 바의 범위는 ' + str(self.bar2.minimum())+" 부터 " +
                             str(self.bar2.maximum())+" 입니다.", self)
        self.label1.move(150,180)

        # - setOrientation(Qt.Vertical) : 세로 진행바를 생성, 반대는 Horizontal(가로)
        # - setRange(시작 숫자,끝 숫자) : 진행바의 범위를 설정
        # - minimum() : 시작 숫자를 가져옵니다.
        # - maximum() : 끝 숫자를 가져옵니다.
        
        self.label2 = QLabel('이곳에 첫 번째 바의 값이 나옵니다.',self)
        self.label2.move(130,300)
        

        self.btn = QPushButton('시작', self) 
        self.btn.move(40, 330)
        self.btn.clicked.connect(self.runTimer)  

        self.value = 0 
        self.timer = QBasicTimer() 
        self.bar1.valueChanged.connect(self.changeValue)

        # - 버튼이 클릭되면 runTimer 슬롯(이벤트) 호출
        # - value 변수: 진행 상황 숫자
        # - valueChanged : 값이 변할 때 changeValue() 호출

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QProgressBar')
        self.show()

    def runTimer(self): 
        
        if self.timer.isActive():  
            self.timer.stop() 
            self.btn.setText('시작')
        else:
            self.timer.start(self.bar1.maximum(), self)  
            
            self.btn.setText('중지')

        # - timer가 활성화(isActive)되어 있으면 즉, 실행중이면 버튼을 클릭했을 때 stop()으로 중지
        # - 그렇지 않다면 (실행중이 아니면) start(종료시간,이벤트가 수행되는 객체)을 시작

    def timerEvent(self, event): 

        if self.value >= self.bar1.maximum():  
            self.timer.stop()  
            self.btn.setText('완료')  
            return  

        self.value +=1   
        self.bar1.setValue(self.value)  

        # - timerEvent는 이미 정의되어 있는 함수(슬롯)으로 파라미터에 추가로 e(event)를 사용
        # - value 값이 설정된 최대값 이상이라면 타이머는 종료
        # - 그렇지 않다면 value값을 1씩 더해 setValue를 통해 업데이트

    def changeValue(self): # 진행바가 수행되는 도중 value 값을 라벨에 업데이트
        self.label2.setText(str(self.bar1.value()))


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 진행바()
프로그램무한반복.exec_()