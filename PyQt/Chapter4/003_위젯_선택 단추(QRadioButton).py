from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton
import sys

class 선택단추(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        rbtn = QRadioButton(self) 
        rbtn.setText('라디오 버튼1') 
        rbtn.move(60,50) # 라디오 버튼 위치 지정
        
        rbtn_2 = QRadioButton('라디오 버튼2', self)
        rbtn_2.move(60,80) # 라디오 버튼 위치 지정
        rbtn_2.setChecked(True) 

        # setChecked : 프로그램 실행시 체크된 상태로 표시
        # setAutoExclusive: 기본적으로 autoExclusive(True)로 설정 되어 있으나 False를 주면 단추 복수로 선택 가능.

        rbtn_3 = QRadioButton('라디오 버튼3', self)
        rbtn_3.move(60,110) # 라디오 버튼 위치 지정
        rbtn_3.setAutoExclusive(False) 

        self.setGeometry(300, 300, 300, 200)         
        self.setWindowTitle('QRadioButton')
        self.show()


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 선택단추()
프로그램무한반복.exec_()