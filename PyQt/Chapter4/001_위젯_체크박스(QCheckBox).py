import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel

class 체크박스(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.cbox = QCheckBox('체크박스1', self)
        self.cbox.move(40, 30)

        self.cbox.stateChanged.connect(self.changeBox1)

        self.cbox2 = QCheckBox('체크박스2', self)
        self.cbox2.move(150, 30)
        
        self.cbox2.stateChanged.connect(self.changeBox2)

        self.result = QLabel('체크 박스를 선택해주세요.', self)
        self.result.setFixedWidth(300)
        self.result.move(40, 100)

        self.cbox2.toggle() # 체크 박스의 상태 변경 / 자세한 내용은 아래 확인
                # 여러가지 형태 옵션
                    # text() 체크 박스의 라벨 텍스트를 반환*
                    # setText() 체크 박스의 라벨 텍스트를 설정*
                    # isChecked()체크 박스의 상태를 반환 (True/False)*
                    # checkState() 체크 박스의 상태를 반환 (2/1/0) (선택/변경없음/해제)*
                    # toggle() 체크 박스의 상태를 변경

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QCheckBox')  
        self.show()

    def changeBox1(self, state):
        if state == Qt.Checked:
            self.result.setText('체크박스1이 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')

    def changeBox2(self, state):
        if state == Qt.Checked:
            self.result.setText('체크박스2이 선택되었습니다.')
        else:
            self.result.setText('체크박스를 선택해주세요.')

    # cbox가 stateChanged(시그널)을 발생하면 changeBox1이라는 정의 함수(슬롯)와 connect(연결)하여 실행하는 코드
    # stateChanged는 체크박스의 상태가 바뀔 때 신호가 발생하는 시그널

    # 시그널과 슬롯에 대해서는 6장에서 자세히 다룰 예정


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 체크박스()
프로그램무한반복.exec_()