from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class 이벤트함수(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        self.label = QLabel('키를 입력하세요 \n\nESC: 종료 \nF11: 위젯 300, 300위치로 옮기기 \nF1: 라벨 텍스트 변경 \n0: 위젯 100,100위치로 옮기기\n1: 위젯 추가') 
        # 각 키보드를 누를때 마다 슬롯이 실행 되게 만듦
        # 전에 써왔던 connect가 없다면 미리 정의된 슬롯(함수)을 써보면 됨.

        '''
        대표적인 정의된 이벤트(슬롯)

        1. keyPressEvent : 키보드를 눌렀을 때 동작합니다.
        2. keyReleaseEvent : 키보드를 눌렀다가 뗄 때 동작합니다.
        3. mouseDoubleClickEvent : 마우스를 더블클릭할 때 사용합니다.
        4. mouseMoveEvent : 마우스를 움직일 때 동작합니다.
        5. mousePressEvent : 마우스를 누를 때 사용합니다.
        6. mouseReleaseEvent : 마우스를 눌렀다가 뗄 때 동작합니다.
        7. moveEvent : 위젯이 이동할 때 동작합니다.
        8. resizeEvent : 위젯의 크기를 변경할 때 동작합니다.
        '''

        self.label2 = QLabel()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label,alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.label2)

        self.setLayout(self.vbox)
        self.setWindowTitle('Reimplementing Event Handler')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def keyPressEvent(self,event):
        # - 프로그램 실행 중 키보드가 눌렸을 때 실행되는 슬롯
        # - 인자로 event를 명시해서 이벤트처리
        # - Qt 라이브러리를 활용해 해당되는 키값을 눌렸으면 아래 기능을 수행하고 키 입력 힌트를 다시 나옴
        if event.key() == Qt.Key_Escape: 
            self.close()  

        elif event.key() == Qt.Key_F11:
            self.move(300, 300) 
            self.label.setText('키 입력하세요 \n\nESC: 종료 \nF11: 위젯 300, 300위치로 옮기기 \nF1: 라벨 텍스트 변경 \n0: 위젯 100,100위치로 옮기기 \n1: 위젯 추가')
        
        elif event.key() == Qt.Key_F1: 
            self.label.setText("F1이 눌렸어요! 되돌아가길 원하시면 0번을 눌러주세요")
        
        elif event.key() == Qt.Key_0:
            self.move(100,100)
            self.label.setText('키 입력하세요 \n\nESC: 종료 \nF11: 위젯 300, 300위치로 옮기기 \nF1: 라벨 텍스트 변경 \n0: 위젯 100,100위치로 옮기기 \n1: 위젯 추가')

    def keyReleaseEvent(self,event):
        # - 이 함수는 키를 눌러서 땔 때 실행되는 함수, 즉 키가 눌려진 상태에서는 이벤트가 실행이 되지 않음
        # - 1번을 눌리면 레이아웃에 라벨을 계속 추가함 → 쌓이게 됨
        if event.key() == Qt.Key_1: 
            self.label2 = QLabel('키가 눌렀다 떼어졌어요!') # 라벨 추가
            self.vbox.addWidget(self.label2) # 라벨을 위젯에 더함


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 이벤트함수()
프로그램무한반복.exec_()