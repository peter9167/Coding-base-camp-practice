#실행하는데 필요한 모듈 호출
#PyQt 공식 홈페이지 -> https://doc.qt.io/qtforpython/modules.html
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class 대표선출프로그램(QWidget):
    # - 함수 초기화를 시키는 부분 입니다.
    #     self는 class '대표선출프로그램'이라는 객체를 의미합니다.
    # - 'UI초기화'라는 메서드로 UI를 초기화하면서 이미지(), 버튼(), 툴팁(), 대리인번호()라는 메서드들을 호출합니다.
    # - setWindowTitle()은 창 상단에 표시되는 제목을 의미합니다.
    # - setWindowIcon()은 창 상단에 표시되는 아이콘을 변경합니다.
    # - setGeometry()는 윈도우의 크기 및 출력 위치를 변경할 수 있습니다.
    # - show()는 화면에 보여주는 메서드로 pyQt를 실행하기 위해 반드시 필요한 메서드입니다.
    def __init__(self):
        super().__init__()
        self.UI초기화()
    
    def UI초기화(self):
        self.이미지()
        self.버튼()
        self.툴팁()
        self.대리인번호()

        self.setWindowTitle('대표를 선출하라!')
        self.setWindowIcon(QIcon('img/weniv-licat.png'))
        self.setGeometry(500, 500, 400, 400)
        self.show()
    
    def 이미지(self):
        self.대표이미지 = QLabel(self)
        self.대표이미지.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44))
        self.대표이미지.move(10, 10)

    def 버튼(self):
        self.대표선출버튼 = QPushButton('대표 선출', self)
        self.대표선출버튼.setFixedSize(340, 40)
        self.대표선출버튼.move(30, 290)
        self.대표선출버튼.clicked.connect(self.choice)

        self.종료버튼 = QPushButton('종료버튼', self)
        self.종료버튼.setFixedSize(340, 40)
        self.종료버튼.move(30, 340)
        self.종료버튼.clicked.connect(self.close)

    def 툴팁(self):
        # setToolTip : 
        self.대표선출버튼.setToolTip('이 버튼을 누르면 대표를 선출합니다. \n주의하세요. 되돌릴 수 없습니다.')
        self.종료버튼.setToolTip('이 버튼을 누르면 프로그램을 종료합니다.') 
        self.대표이미지.setToolTip('생선가게 대표 라이켓')
        self.setToolTip('이곳은 QWidget')

    def 대리인번호(self):
        # https://doc.qt.io/qtforpython/PySide2/QtGui/QFont.html
        self.대리인번호라벨 = QLabel('000', self)
        self.대리인번호라벨.setFont(QFont("Helvetica", pointSize=75, weight=2))
        self.대리인번호라벨.move(80, 100)

    def choice(self):
        s = str(random.randint(1, 1000))
        print(s)
        self.대리인번호라벨.setText(s)

    def close(self):
        return QCoreApplication.instance().quit()

프로그램무한반복 = QApplication(sys.argv) # 무한반복을 하기 위한 선언
실행인스턴스 = 대표선출프로그램() # 대표선출프로그램 인스턴스 생성 하면서 클래스 구문 실행
프로그램무한반복.exec_() # 본 구문을 통하여 클래스 코드 무한 동작
# 만약 프로그램무한반복.exec_() 구문이 없다면 클래스 구문이 단 한 번밖에 실행되지 않음.