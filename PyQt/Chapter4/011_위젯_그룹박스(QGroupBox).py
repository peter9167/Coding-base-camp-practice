from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QRadioButton, QCheckBox, QPushButton, QGridLayout, QVBoxLayout, QMenu, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

# 그룹 박스는 여러가지 Object, 가령 Label이나 PushButton 등을 모아서 하나의 그룹을 만들 수 있는 기능
# QGroupBox를 통해 만들 수 있음. 여기서는 각각의 그룹을 모듈화 하여 만듬

class 그룹박스(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        # - 라벨에 이미지를 업데이트하고 GridLayout를 활용해 만들어진 함수들을 넣습니다.
        # - label(그림)은 0행 1열에서 1행 1열 까지 확장
        # - 마지막 PushButtonGroup는 2행 0열에서 2행 1열 확장
        img = QPixmap('img/pyqt.png') # 이미지를 img에 저장
        label = QLabel() # 라벨 생성 
        label.setPixmap(img) # 라벨에 이미지 로드
        label.setAlignment(Qt.AlignCenter) # label(img label) 가운데 정렬

        grid = QGridLayout()
        grid.addWidget(self.RadioGroup(), 0, 0)
        grid.addWidget(self.CheckGroup(), 1, 0)
        grid.addWidget(label, 0, 1, 2, 1)
        grid.addWidget(self.PushButtonGroup(), 2, 0, 2, 2)

        self.setLayout(grid)

        self.setWindowTitle('QGroupBox')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def RadioGroup(self):
        # - 라디오버튼으로만 구성된 그룹을 함수로 만들어 적용
        # - radio2는 프로그램 실행시 체크된 상태로 나타남
        # - **리턴을 해주어야 QGroupBox에서 적용가능**
        RadioGroupBox = QGroupBox('라디오 버튼 그룹')

        radio1 = QRadioButton('Radio 버튼 1')
        radio2 = QRadioButton('Radio 버튼 2')
        radio3 = QRadioButton('Radio 버튼 3')
        radio2.setChecked(True) 

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        RadioGroupBox.setLayout(vbox)

        return RadioGroupBox  

    def CheckGroup(self):
        # - setCheckable : 사용자가 체크기능을 허락하는 지 여부 만약 False값이 라면 하위 버튼들도 선택 불가, 기본적으로는 박스가 없이 생성 (하위 버튼들은 선택 가능)
        # - setChecked(False) : 이 체크박스 그룹은 체크가 안된 상태로 실행
        # - setTristate: 3개의 값을 가진 체크박스를 생성 [체크,미체크,네모]
        CheckBoxGroup = QGroupBox('체크박스 그룹')
        CheckBoxGroup.setCheckable(True) 
        CheckBoxGroup.setChecked(False)

        checkbox1 = QCheckBox('체크박스1')
        checkbox1.setChecked(True)
        checkbox2 = QCheckBox('체크박스2')

        tristatebox = QCheckBox('체크박스3')
        tristatebox.setTristate(True)

        hbox = QHBoxLayout()

        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        hbox.addWidget(tristatebox)
        CheckBoxGroup.setLayout(hbox)

        return CheckBoxGroup

    def PushButtonGroup(self):
        # - setFlat : 버튼을 눌렀을때에만 버튼의 모양이 나오는 옵션
        # - QMenu를 활용, PopupButton에 메뉴를 추가
        PushButtonGroupBox = QGroupBox('푸시버튼 그룹')
        PushButtonGroupBox.setAlignment(Qt.AlignCenter)
       
        PushButton = QPushButton('기본 버튼') 
        PushButton.setStyleSheet("color: green;"
                          "border-style: solid;"
                          "border-width: 3px;"
                          "background-color: beige;"
        )

        CheckedButton = QPushButton('체크 표시 버튼')
        CheckedButton.setCheckable(True) 
        CheckedButton.setChecked(True)  

        FlatButton = QPushButton('Flat 버튼')
        FlatButton.setFlat(True)

        PopupButton = QPushButton('팝업 창 버튼') 
        menu = QMenu(self) 
        menu.addAction('옵션 1')
        menu.addAction('옵션 2')
        PopupButton.setMenu(menu) 

        vbox = QVBoxLayout()
        vbox.addWidget(PushButton)
        vbox.addWidget(CheckedButton)
        vbox.addWidget(FlatButton)
        vbox.addWidget(PopupButton)
        PushButtonGroupBox.setLayout(vbox)

        return PushButtonGroupBox


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그룹박스()
프로그램무한반복.exec_()