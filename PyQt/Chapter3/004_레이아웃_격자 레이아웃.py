import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout  
from PyQt5.QtCore import Qt


class 격자레이아웃(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

    # 1. setSpacing(위젯간 간격) : 설정하지 않을 경우 위젯끼리 겹침
    # 2. addWidget(추가할 위젯, 행, 열) 
    # 3. addWidget(추가할 위젯, 행, 열, 확장시킬 행, 확장시킬 열)
        # - 즉,  2행 0열에서 2행 2열(3-1)까지 확장
        # - 특히, 레이아웃에 위젯을 추가할 때, alignment=Qt.Align{위치}처럼 인자를 주어 정렬이 가능
        # 아래 링크 확인
        # /img/alignment.png

        insert = QPushButton('Insert') 
        home = QPushButton('Home')
        pageUp = QPushButton('Page Up')
        delete = QPushButton('Delete')
        end = QPushButton('End')
        pageDown = QPushButton('Page Down')
        keyboard = QLabel('KeyBoard')

        grid = QGridLayout()
        grid.setSpacing(15) # 간격 크기 지정 / 설정하지 않으면 위젯끼리 겹침 - 필수 작성

        grid.addWidget(insert, 0, 0)    # 레이아웃 생성 / addWidget(추가할 위젯, Y, X) <- 표처럼 레이아웃 설정 시
        grid.addWidget(home, 0, 1) 
        grid.addWidget(pageUp, 0, 2)

        grid.addWidget(delete, 1, 0)
        grid.addWidget(end, 1, 1)
        grid.addWidget(pageDown,1,2)

        grid.addWidget(keyboard, 2, 0, 2, 3, alignment=Qt.AlignHCenter) # addWidget(추가할 위젯, 행, 열, 확장시킬 행, 확장시킬 열, alignment=Qt.AlignHCenter <- 중앙 정렬)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Review')
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 격자레이아웃()
프로그램무한반복.exec_()