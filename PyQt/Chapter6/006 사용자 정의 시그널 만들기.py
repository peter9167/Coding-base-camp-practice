from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QPushButton, QLabel, QMainWindow 
from PyQt5.QtCore import Qt, pyqtSignal, QObject # 새로운 시그널(신호)을 만들기 위해 pyqtSignal을, 모든 위젯의 상위에 있는 QObject를 추가
import sys

class Signal(QObject):
    # - 여러 시그널을 담기 위해 따로 클래스로 정의
    # - 각 시그널을 pyqtSignal() 정의
    closeProgram = pyqtSignal()
    addText = pyqtSignal()

class 사용자정의시그널(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UI초기화()
    
    def UI초기화(self):

        self.signal1 = Signal()
        self.signal1.closeProgram.connect(self.close)
        # - 클래스를 활용해 signal1이라는 인스턴스를 생성
        # - 그 객체 안에 closeProgram이라는 시그널을 호출

        '''
        앞에서 사용했던 예제
        btn = QPushButton('클릭')
        btn.clicked.connect(self.changeLabel) #changeLabel은 슬롯(slot)
        '''

        self.label1 = QLabel('시그널을 알아볼까요?', self)
        self.label1.setFixedSize(300, 20)
        self.label1.move(40, 100)

        self.signal2 = Signal()
        self.signal2.addText.connect(self.changelabel)
        # Signal()을 통해 새로운 signal2 인스턴스를 생성

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mouseDoubleClickEvent(self, event):
        self.signal1.closeProgram.emit()
        # 마우스를 더블클릭하면 closeProgram시그널을 emit()를 통해 동작
        # 결국 self.close로 프로그램을 종료

    def mousePressEvent(self, event):
        self.signal2.addText.emit()
        # 마우스가 눌렸다면 addText라는 시그널을 발생(emit()). 이는 changelabel 슬롯을 호출

    def changelabel(self): # 해당 함수에서는 라벨을 변경
        self.label1.setText('마우스가 눌렸습니다!')

    def close(self):
        super().close()
    # 즉 시그널을 만들고(pyqtSignal) 그 시그널을 발생(emit)시키는 어떤 동작함수를 만들어 연결시킨(connect) 슬롯의 동작을 수행


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 사용자정의시그널()
프로그램무한반복.exec_()