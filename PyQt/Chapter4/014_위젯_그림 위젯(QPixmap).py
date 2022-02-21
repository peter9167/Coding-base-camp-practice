from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import urllib.request 

# QtGui 중에서도 대표적인 기능 중 하나인 QPixmap은 이미지 처리와 관련된 여러 기능들을 지원
# 저장, 사이즈 변경 등에 다양한 메서드를 지원하니 공식 문서도 한 번 참고
# 여기서는 이미지 출력, 이미지 저장, 사이즈 지정 출력에 대해 실습
# 공식 문서 : https://doc.qt.io/qtforpython-5/PySide2/QtGui/QPixmap.html


class 그림위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.img = QPixmap() 
     
        url ='http://www.paullab.co.kr/images/logo_weniv.png'
        webImg = urllib.request.urlopen(url).read()

        self.img.loadFromData(webImg) 
       
        self.label_img = QLabel()  
        self.label_img.setPixmap(self.img)  
        self.label_img.setAlignment(Qt.AlignCenter)  
        self.label_size = QLabel(f'가로 : {self.img.width()}/세로 : {self.img.height()}')  
        self.label_size.setAlignment(Qt.AlignCenter)

        '''
        - urlib.request : 라이브러리를 통해 웹 이미지 크롤링을 할 수 있도록 함
        - urlopen(웹 주소).read() : 주소에 따른 리소스를 가져옵니다. 여기서는 이미지
        - width(), height()를 통해 : 현재 이미지의 가로, 세로 값을 구해 표시
        '''

        loadBtn = QPushButton('이미지 변경')
        loadBtn.clicked.connect(self.changeImage)

        saveBtn = QPushButton('저장')
        saveBtn.clicked.connect(self.saveImage)

        # 각 버튼이 클릭되면 이미지 변경, 저장 기능을 수행하는 함수와 연결

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_img)
        vbox.addWidget(self.label_size)
        vbox.addWidget(loadBtn)
        vbox.addWidget(saveBtn)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def changeImage(self): # 저장된 이미지를 불러와 라벨에 업데이트하고, 가로 세로를 구해 표시
        self.img.load('img/weniv-mura.png') 
        self.label_img.setPixmap(self.img)
        self.label_size.setText(f'가로 : {self.img.width()}/세로 : {self.img.height()}') 

    def saveImage(self): 
        self.img = self.label_img.pixmap() 
        self.img.save('저장된 이미지.png')        
        # - pixmap(): 라벨에서 그림을 가져옴
        # - save() :파라미터에 있는 문자열의 이름을 가진 파일을 저장, 보통 현재 실행하는 코드의 파일이 있는곳에 생성합니다.


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 그림위젯()
프로그램무한반복.exec_()