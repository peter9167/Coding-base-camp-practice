from ast import Expression
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np #pip install numpy
import tensorflow as tf
from PIL import Image, ImageOps

# pip install --upgrade pip 
# pip install tensorflow

# python이 32bit으로 깔려있다면, 오류가 남 -> window에서 지워주시고 다시 64비트로 설치해주세요.
# ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
# ERROR: No matching distribution found for tensorflow

class 마스크경고(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.대표이미지 = QLabel(self)
        self.대표이미지.setPixmap(QPixmap('img/weniv-licat.png').scaled(35, 44))
        self.대표이미지.move(20, 65)
        self.대표이미지.resize(35, 44)

        self.가게이름 = QLabel('라이캣의 무인가게 마스크 경고!', self)
        self.가게이름.setFont(QFont("Decorative", 15)) # QFont 함수를 이용하여 "Decorative"를 15px로 설정
        self.가게이름.adjustSize()
        self.가게이름.move(80, 70)

        self.이미지 = QLabel(self)
        self.이미지.move(200, 100)

        self.가이드 = QLabel('상단바 File을 눌러 모델 추가 후 이미지를 삽입하여 인식합니다.', self)
        self.가이드.move(40, 500) # 가이드 위치 설정
        self.가이드.adjustSize()

        self.마스크경고 = QLabel('마스크를 써주세요!!', self)
        self.마스크경고.move(200, 550)
        self.마스크경고.adjustSize()
        self.마스크경고.setHidden(True) # 마스크 경고 라벨을 Hidden으로 설정하여 보이지 않게 함.

        self.이미지업로드 = QPushButton('파일 업로드', self)
        self.이미지업로드.move(170, 430)
        self.이미지업로드.resize(240, 40)
        self.이미지업로드.setEnabled(False)
        self.이미지업로드.clicked.connect(self.loadImage)

        self.인식모델 = None

        메뉴바 = self.menuBar()
        메뉴바.setNativeMenuBar(False)
        파일메뉴 = 메뉴바.addMenu('File') # 본 구문을 통해서 메뉴바를 생성할 수 있음

        모델불러오기메뉴 = QAction('모델 불러오기', self) # 모델 불러오기 메뉴 생성
        모델불러오기메뉴.setShortcut('Ctrl+L') # 단축키 설정
        모델불러오기메뉴.triggered.connect(self.loadModel) #모델불러오기메뉴와 loadModel 연결
        파일메뉴.addAction(모델불러오기메뉴) # 파일메뉴에 모델불러오기메뉴를 추가

        self.setWindowTitle('(주)캣네생선 무인상점 마스크 경고음 프로그램')
        self.setGeometry(300, 300, 600, 600)
        self.show()

    def loadModel(self):
        try:
            모델파일, _ = QFileDialog.getOpenFileName(self, '모델 추가', '')
            if 모델파일:
                self.인식모델 = load_model('모델파일')
                self.가이드.setText('뫄델 추가 완료!')
            self.이미지업로드.setEnabled(True)
        except:
            self.가이드.setText('모델 파일이 아닙니다!')

    def loadImage(self):
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        이미지이름, _ =QFileDialog.getOpenFileName(self, '모델 추가', '')
        # Replace this with the path to your image
        이미지파일 = QPixmap(이미지이름).scaled(200, 200, aspectRatioMode=Qt.KeepAspectRadio)
        self.이미지.setPixmap(이미지파일)
        self.이미지.adjustSize()

        if 이미지파일:
            image = Image.open('<IMAGE_PATH>')
            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)

            #turn the image into a numpy array
            image_array = np.asarray(image)
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)
            print(prediction)


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 마스크경고()
프로그램무한반복.exec()

