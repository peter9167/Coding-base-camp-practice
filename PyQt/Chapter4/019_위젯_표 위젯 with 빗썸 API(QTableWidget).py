from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
import json
import requests # 모듈이 없으실 경우 pip3 install requests
# 빗썸 API와 통신하기 위해 requests를 사용하고 받아온 Data를 json형태로 다룸

class 표위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.table = QTableWidget(150, 5, self)
        header = ['종목', '전일 종가', '변동가', '변동률', '시가']

        '''
        - 행 150열의 테이블을 만듦
        - table.rowCount(5) : 5행 설정으로도 사용 가능
        - table.colorCount(150) : 150열 설정으로도 사용 가능
        - header = 열을 나타내는 데이터를 표시[종목,전일 종가,최근 24시간 변동률,변동가, 현재 시가]
        '''

        bithumbUrl = 'https://api.bithumb.com/public/ticker/ALL_KRW'
        # 빗썸 오픈 API : https://apidocs.bithumb.com/docs/ticker 참고
        data = json.loads(requests.get(bithumbUrl).text)
        # - json.loads(가져온 data)로 데이터를 처리

        # print(data)
        for index, coin in enumerate(data['data']):
            if coin == 'date':
                break
            self.table.setItem(index, 0, QTableWidgetItem(coin)) 
            self.table.setItem(index, 1, QTableWidgetItem(data['data']\
                                         [coin]['prev_closing_price']+'원'))
            self.table.setItem(index, 2, QTableWidgetItem(data['data']\
                                         [coin]['fluctate_24H']+'원'))
            self.table.setItem(index, 3, QTableWidgetItem(data['data']\
                                         [coin]['fluctate_rate_24H']+" %"))
            self.table.setItem(index, 4, QTableWidgetItem(data['data']\
                                         [coin]['opening_price']+"원"))
            '''
            - enumerate로 인덱스와 해당 Data를 다룰수 있도록 반복
            - 받아온 jSON  data의 마지막 키가 date를 만나면 종료
            - setItem(행,열,QTableWidgetItem(데이터)) 를 활용해 데이터를 넣어줌
            '''
        
        self.table.setHorizontalHeaderLabels(header)
        self.table.cellClicked.connect(self.showCellPosition)
        # - setHorizontalHeaderLabels(header) : 열의 라벨을 파라미터의 값으로 설정합니다.
        # - cellClicekd : 셀을 클릭하면 시그널 발생

        self.label = QLabel()
        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 300, 720, 500)
        self.show()

    def showCellPosition(self): # 선택된 행과 열을 반환하여 라벨에 업데이트
        행 = self.table.currentColumn()
        열 = self.table.currentRow()
        self.label.setText(f'{행} 행, {열} 열입니다.')
        

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 표위젯()
프로그램무한반복.exec_()