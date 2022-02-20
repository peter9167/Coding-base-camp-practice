from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
import sys

class 옵션선택창(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.label = QLabel('옵션을 선택해주세요.', self) # 라벨 생성
        self.label.move(20, 80) # 라벨 위치 지정
        self.label.setFixedSize(400,40) #라벨 전체 사이즈 지정

        self.cbox = QComboBox(self) # ComboBox에 요소 추가시 addItem 매서드를 사용. 안에 들어가는 값은 문자열만 가능
        self.cbox.addItem('Option 1') 
        self.cbox.addItem('Option 2')
        self.cbox.addItem('Option 3')
        self.cbox.addItem('Option 4')

        self.cbox.move(40,40) # 콤보 박스 위치 지정

        # cbox(박스)의 속성이 눌렸을 때(activated[str])  정의된 함수(clicked)가 실행되어 이벤트 처리를 하게 됨. 
        # clicked는 우리가 정의할 함수
        self.cbox.activated[str].connect(self.clicked) 
        # 1. activated[str]에 의해 text인자가 추가로 넘겨오고(즉, 누른 옵션의 문자열)
        # 2. currentIndex()를 활용해 인덱스를 구하고
        # 3. currentText()를 활용해 현재 누른 텍스트의 문자열을 가져와 라벨에 업데이트
        # 4. adjustSize()은 라벨의 크기를 자동 조절 단, 이 경우 창크기도 같이 조절이 될 수 있음
        
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def clicked(self): # cbox와 연결된 함수 clicked를 구현
        index = str(self.cbox.currentIndex()) # currentIndex()를 활용해 인덱스를 구하고
        text = str(self.cbox.currentText())   # currentText()를 활용해 현재 누른 텍스트의 문자열을 가져와 라벨에 업데이트
        self.label.setText("아이템의 " + index + "번째에 있는 "+ text + "를 선택했습니다.") 
        self.adjustSize() # adjustSize()은 라벨의 크기를 자동 조절 단, 이 경우 창크기도 같이 조절이 될 수 있음


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 옵션선택창()
프로그램무한반복.exec_()