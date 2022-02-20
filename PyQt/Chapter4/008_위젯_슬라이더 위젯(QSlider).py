from PyQt5.QtWidgets import QWidget, QApplication,QLabel,QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 
import sys

# QSlider 공식문서 링크 : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSlider.html

class 슬라이더위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()
    
    def UI초기화(self):

        sli = QSlider(Qt.Vertical,self) # 슬라이더 생성
        sli.setGeometry(200,50,100,200) 
        sli.setTickPosition(QSlider.TicksLeft) 
        sli.valueChanged[int].connect(self.changeValue)

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('chapter4/mute.png'))
        self.img.adjustSize() 
        self.img.move(30,70)
        
        self.label = QLabel(f'범위:{sli.minimum()} ~ {sli.maximum()}', self)

        # - `setTickPosition` 를 활용해 수직, 수평 막대를 설정할 수 있습니다. 아래와 같이 int값으로도 표시할 수 있습니다.
        # - setTickPosition(0) = setTickPosition(QSlider.NoTicks) 틱을 표시하지 않음
        # - setTickPosition(1) = setTickPosition(QSlider.TicksAbove) 틱을 수평슬라이더 위쪽에 표시
        # - setTickPosition(2) = setTickPosition(QSlider.TicksBelow) 틱을 수평슬라이더 아래쪽에 표시
        # - setTickPosition(3) = setTickPosition(QSlider.TicksBothSides) 틱을 수평슬라이더 양쪽에 표시
        # - setTickPosition(TicksAbove) = setTickPosition(QSlider.TicksLeft) 틱을 수직슬라이더 왼쪽에 표시
        # - setTickPosition(TicksBelow) = setTickPosition(QSlider.TicksRight) 틱을 수직슬라이더 오른쪽에 표시
        # - valueChanged[int] : 슬라이더가 움직이면 즉, 여기서는 값이 바뀌면 시그널을 보내 changeValue와 연결
        # - setPixmap(QPixmap(사진 위치))
        # - adjustSize() : 사이즈 자동 맞춤

        self.label.move(50,200)

        self.label2 = QLabel(self)
        self.label2.move(50,250)
        self.label2.setFixedWidth(30)

        self.setGeometry (300, 300, 400, 400) 
        self.setWindowTitle ('QSlider') 
        self.show() 

    def changeValue(self,value): # 현재 value에 따른 라벨에 나타나는 그림이 달라지는 함수(슬롯)
        self.label2.setText(str(value))

        if value == 0:
            self.img.setPixmap(QPixmap('chapter4/mute.png')) 
        elif 0 < value <= 30:
            self.img.setPixmap(QPixmap('chapter4/min.png')) 
        elif 30 < value <= 80:
            self.img.setPixmap(QPixmap('chapter4/medium.png'))
        else:
            self.img.setPixmap(QPixmap('chapter4/max.png')) 
             

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 슬라이더위젯()
프로그램무한반복.exec_()