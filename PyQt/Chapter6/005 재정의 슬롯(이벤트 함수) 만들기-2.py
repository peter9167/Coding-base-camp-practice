from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class 이벤트함수(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        x = 0 # x : 마우스 좌표를 구하기 위한  변수 
        y = 0 # y : 마우스 좌표를 구하기 위한  변수 

        self.location = f"x좌표는 : {x}, y좌표는 : {y}" 
        self.label1 = QLabel(self.location, self)
        self.label1.setFont(QFont("Decorative",20))
        self.label2 = QLabel("마우스를 클릭 또는 더블클릭 해보세요")

        self.setMouseTracking(True) # self.setMouseTracking :마우스 위치를 트래킹(추적) 기본값은 False

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.setLayout(self.vbox)
        self.setWindowTitle('Reimplementing Event Handler2')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def keyPressEvent(self,event):
        # - 프로그램 실행 중 키보드가 눌렸을 때 실행되는 슬롯
        # - 인자로 event를 명시해서 이벤트처리
        if event.key() == Qt.Key_Escape: 
            self.close()  
   
    def mousePressEvent(self, event):
        self.label2.setText('마우스를 클릭했습니다.')
        # 마우스가 눌렸을 때 동작하는 슬롯은 자주 사용하는 슬롯. 이미 정의되어 있는 슬롯이며, 본 구문은 재정의

    def mouseDoubleClickEvent(self, event):
        self.label2.setText('마우스를 더블클릭했습니다.') # 마우스를 더블클릭 했을 때 동작하는 슬롯


    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        location = 'x좌표는 : {0}, y좌표는 : {1}'.format(x, y) 

        self.label1.setText(location)
        # - 프로그램내에서 마우스가 움직이면 마우스 좌표를 구해 라벨에 업데이트
        # - `.foramt(value1, value2, value3, ...)` 해당 메서드는 str에 내장되어 있는 메서드


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 이벤트함수()
프로그램무한반복.exec_()