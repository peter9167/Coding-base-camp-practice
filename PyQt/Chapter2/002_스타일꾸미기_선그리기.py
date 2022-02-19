import sys  #실행하는데 필요한 모듈 호출

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen #그림 그리기, 색상 제어, 폰트 제어, 펜 제어
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.pyqtUI()

    def pyqtUI(self):
        self.setGeometry(300, 300, 500, 500) # 창 셋팅 : setGeometry : (window 창에서 X좌표, window 창에서 Y좌표, window창에서 지정된 좌표부터 X좌표, window창에서 지정된 좌표부터 X좌표)
        self.setWindowTitle('QPainter!') # 실행 창 제목 설정 (default : Python으로 지정) 
        self.show() 

        # pyqtUI에서 paintEvent를 호출하지 않아도 되는 이유는 painEvent는 기본으로 설정됨.
        # 본 코드에서는 painEvent를 재정의 함.

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        self.drawLine(paint) # 그리기 동작 코드
        paint.end()

    def drawLine(self, paint):
        pen = QPen(Qt.blue, 4, Qt.SolidLine) #파란색, 4px, 실선 생성
        paint.setPen(pen) # pan과 연결
        paint.drawLine(100, 40, 400, 40) # 생성 위치 지정

        # 선의 종류/스타일 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=y4769&logNo=220436834078
        # QColor 색 목록 : https://doc.qt.io/archives/3.3/qcolor.html
        pen.setStyle(Qt.DashLine) # setSytle : 다양한 속성 스타일을 지정할 수 있으나 pen 스타일 속성을 지정하고 있기 때문에 선 스타일 지정, DashLine : 파선
        pen.setColor(Qt.yellow) # 선색 : Yellow(노란색)
        paint.setPen(pen) # pan과 연결
        paint.drawLine(100, 80, 400, 80) # 생성 위치 지정

        pen.setStyle(Qt.DashDotLine) # DashDotLine : 1점 쇄선
        pen.setColor(Qt.red) # 선색 : Yellow(노란색)
        paint.setPen(pen) # pan과 연결
        paint.drawLine(100, 120, 400, 120) # 생성 위치 지정

        pen.setStyle(Qt.DashDotDotLine) # DashDotLine : 2점 쇄선
        pen.setColor(Qt.darkMagenta)
        paint.setPen(pen) # pan과 연결
        paint.drawLine(100, 160, 400, 160) # 생성 위치 지정

        pen.setStyle(Qt.DashLine) # DashLine : 점선
        pen.setColor(Qt.darkGreen) 
        paint.setPen(pen) # pan과 연결
        paint.drawLine(100, 200, 400, 200) # 생성 위치 지정

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4]) # 사용자 지정 대시 및 공백의 길이를 지정하는 실수 배열에 대한 포인터 -> [1(선길이), 4(공백 길이), 5(선길이), 4(공백 길이)]
        pen.setColor(Qt.darkGray)
        pen.setWidth(8)
        paint.setPen(pen)
        paint.drawLine(100, 240, 400, 240) # 생성 위치 지정


프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기 위한 선언
실행인스턴스 = myapp() # 대표선출프로그램 인스턴스 생성 하면서 클래스 구문 실행
프로그램무한반복.exec_() # 본 구문을 통하여 클래스 코드 무한 동작
# 만약 프로그램무한반복.exec_() 구문이 없다면 클래스 구문이 단 한 번밖에 실행되지 않음.