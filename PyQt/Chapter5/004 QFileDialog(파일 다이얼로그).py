from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QFileDialog,\
                            QVBoxLayout, QPushButton, QLabel                   # QFileDialog를 사용할 수 있게 하는 모듈
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

from pathlib import Path  # 경로를 쉽게 접근 할 수있도록 제공하는 라이브러리

# 파일 입출력은 앞에서 한 color나 font보다 선택할 수 있는 매서드가 많다. 
# 예를 들어 특정 파일만 열리게 할 수도 있음. 
# 파일이 존재하는지, 존재하지 않는지, 읽기만 할 것인지 등에 대한 메서드가 자세하게 정의되어 있으니, 아래 문서를 참고
# 공식문서(QFileDialog) : https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html

class 파일다이얼로그(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.textEdit = QTextEdit("이곳에 파일 내용이 들어갑니다.")
        self.label = QLabel("이곳에는 그림이 들어갑니다.")

        btn_open = QPushButton('파일 불러오기')
        btn_open.clicked.connect(self.loadFile)
        btn_img = QPushButton('이미지 불러오기')
        btn_img.clicked.connect(self.loadImg)
        # 각 버튼을 누르면 파일 및 이미지를 불러올수 있도록 함

        vbox = QVBoxLayout()
        vbox.addWidget(self.textEdit)
        vbox.addWidget(btn_open)

        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(btn_img)

        self.setLayout(vbox)
        self.setGeometry(300, 100, 600, 800)
        self.setWindowTitle('QFileDialog')
        self.show()

    def loadFile(self):

        Openfile = QFileDialog.getOpenFileName(self,\
                   '파일 열기', './', filter="Python Files(*.py)")
        
        if Openfile[0]:
            f = open(Openfile[0], 'r', encoding='utf-8')  

            with f:  
                data = f.read()  
                self.textEdit.setText(data) 
        '''
        - getOpenFileName(부모위젯,창 이름,기본 경로,옵션: 필터(파일확장자)), 이 경우 현재 작업하고 있는 공간의 최상단을 보여줌
        - 필터로 선택할 수 있는 파일 확장자를 설정, 여러가지를 추가할 경우 옵션을 ;; 로 구분
        - openfile[0] 값이 있다면 f라는 변수에 open함수를 활용해 데이터를 가져옵니다.
        - 'r'옵션은 read 즉,읽기 전용

        - with는 파일 입출력시 많이 사용되는 명령어 ,쉽게 말해 파일을 open부터 close까지 해주는 함수
        - 읽은 값을 변수에 read()를 활용해 저장
        - textEdit에 표시
        '''

    def loadImg(self):
        home_dir = str(Path.home()) 

        Openfile = QFileDialog.getOpenFileName(
            self, "이미지 열기", directory=home_dir, filter="Images (*.png *.jpg)")

        self.label.setPixmap(QPixmap(Openfile[0]))

        '''
        - Path.home()을 통해 최상단 디렉토리 주소를 가져옵니다.
        - 최상단 디렉토리에서 확장자가 png, jpg 파일만 가져올 수 있도록 합니다.
        - QPixmap()을 활용해 가져온 이미지로 라벨에 업데이트
        '''


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 파일다이얼로그()
프로그램무한반복.exec_()