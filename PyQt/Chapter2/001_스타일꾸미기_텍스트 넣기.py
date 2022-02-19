import sys  #실행하는데 필요한 모듈 호출

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont #그림 그리기, 색상 제어, 폰트 제어
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.pyqtUI()

    def pyqtUI(self):
        self.text = 'Hello Weniv World!!' # text를 설정하여도 위치를 지정하지 않으면 실행되지 않음
        self.setGeometry(300, 300, 500, 500) # 창 셋팅 : setGeometry : (window 창에서 X좌표, window 창에서 Y좌표, window창에서 지정된 좌표부터 X좌표, window창에서 지정된 좌표부터 X좌표)
        self.setWindowTitle('QPainter!') # 실행 창 제목 설정 (default : Python으로 지정) 
        self.show() 

        # pyqtUI에서 paintEvent를 호출하지 않아도 되는 이유는 painEvent는 기본으로 설정됨.
        # 본 코드에서는 painEvent를 재정의 함.

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawText(event, paint)
        paint.end()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10))
        paint.setFont(QFont('Decorative', 10)) #QFont를 이용하여 Font를 지정함(Font 초기화 설정). Decorative : Font Name 지정함, 10 : 10px로 지정함.
        paint.drawText(130, 100, 'hello world!!') # X: 130, Y: 100 위치에 'hello world!!' 문구 출력 
        paint.drawText(event.rect(), Qt.AlignCenter, self.text) # event.rect : 직사각형, Qt.AlignCenter : 가운데 정렬, self.text에 설정


프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기 위한 선언
실행인스턴스 = myapp() # 대표선출프로그램 인스턴스 생성 하면서 클래스 구문 실행
프로그램무한반복.exec_() # 본 구문을 통하여 클래스 코드 무한 동작
# 만약 프로그램무한반복.exec_() 구문이 없다면 클래스 구문이 단 한 번밖에 실행되지 않음.