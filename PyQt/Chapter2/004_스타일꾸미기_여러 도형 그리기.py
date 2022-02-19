import sys  #실행하는데 필요한 모듈 호출

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QPen, QBrush #그림 그리기, 색상 제어, 폰트 제어, 펜 제어, 도형 그리기
from PyQt5.QtCore import Qt
import random


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.pyqtUI()

    def pyqtUI(self):
        self.setGeometry(300, 300, 500, 500) # 창 셋팅 : setGeometry : (window 창에서 X좌표, window 창에서 Y좌표, window창에서 지정된 좌표부터 X좌표, window창에서 지정된 좌표부터 X좌표)
        self.setWindowTitle('도형 그리기!') # 실행 창 제목 설정 (default : Python으로 지정) 
        self.show() 

        # pyqtUI에서 paintEvent를 호출하지 않아도 되는 이유는 painEvent는 기본으로 설정됨.
        # 본 코드에서는 painEvent를 재정의 함.

    def paintEvent(self, event):
        paint = QPainter() # QPainter : 그림판 같은 역할을 하는 모듈
        paint.begin(self)
        self.drawFigure(paint) # 그리기 동작 코드
        paint.end()

    def drawFigure(self, paint):
        # QPainter : 그림판 같은 역할을 하는 모듈

        # QColor : Color와 관련된 모듈 / 아래 링크 확인
        # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html

        # QPen : 그림판의 펜과 같은 역할
        # https://doc.qt.io/qtforpython-5/PySide2/QtGui/QPen.html

        # QFont : 폰트와 같은 설정. 굵기와 폰트 스타일 등을 지정. 상세 설정은 공식문서 참고.
        # https://doc.qt.io/qtforpython-5/PySide2/QtGui/QFont.html

        # QBrush : 패턴을 채울 수 있음. 디자인 패턴 이름은 아래 공식 문서를 참고

        paint.setBrush(QColor(10, 255, 40)) # 도형 채우기 색 지정 (방법1: RGB
        paint.setPen(QPen(QColor(Qt.red)))  # 도형 선 색 지정     (방법2: 색상 설정
        paint.drawRect(20, 30, 100, 100)    # drawRect : 직사각형 도형 생성, (창 X좌표, 창 Y좌표, 도형 X 크기, 도형 Y 크기)

        paint.setBrush(QColor(10, 255, 40)) # 도형 채우기 색 지정 (방법1: RGB
        paint.setPen(QPen(QColor(Qt.red)))  # 도형 선 색 지정     (방법2: 색상 설정
        paint.drawRoundedRect(150, 20, 100, 100, 30, 30)    # drawRoundedRect : 둥근 직사각형 도형 생성, (창 X좌표, 창 Y좌표, 도형 X 크기, 도형 Y 크기, 둥근 모서리 X px 지정, 둥근 모서리 Y px 지정)

        paint.setBrush(QBrush(Qt.CrossPattern)) # 디자인 패턴 설정
        paint.drawRoundedRect(300, 100, 100, 100, 30, 30)    # drawRoundedRect : 둥근 직사각형 도형 생성, (창 X좌표, 창 Y좌표, 도형 X 크기, 도형 Y 크기, 둥근 모서리 X px 지정, 둥근 모서리 Y px 지정)

        paint.setBrush(QColor(Qt.darkGreen)) # 도형 채우기 색 지정
        paint.setPen(QPen(QColor(Qt.red), 2, Qt.DotLine))  # 도형 선 색 지정, 2px, 점선
        paint.drawEllipse(180, 200, 180, 220) # drawEllipse : 원 생성, 위치지정XY, 도형크기XY
        

프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기 위한 선언
실행인스턴스 = myapp() # 대표선출프로그램 인스턴스 생성 하면서 클래스 구문 실행
프로그램무한반복.exec_() # 본 구문을 통하여 클래스 코드 무한 동작
# 만약 프로그램무한반복.exec_() 구문이 없다면 클래스 구문이 단 한 번밖에 실행되지 않음.