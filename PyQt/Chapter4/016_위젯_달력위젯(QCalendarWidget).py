from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QCalendarWidget,QPushButton
from PyQt5.QtCore import Qt, QDate
import sys

# QCalendarWidget은 달력을 표시할 수 있는 위젯 
# 이를 통해 날짜별 다양한 연산을 수행할 수 있습니다. 공식문서, Slots, Signals를 함께 개시

class 달력위젯(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.cal = QCalendarWidget() 
        self.cal.setGridVisible(True) 
        self.cal.setDateRange(QDate(2020, 1, 1), QDate.currentDate()) 
        self.cal.clicked[QDate].connect(self.PastDate)  

        # - setGridVisivle(True/Flase) : 격자 표시 설정
        # - clicked[QDate]를 통해 달력내 날짜가 눌리면 PasteDate 호출

        self.label1 = QLabel(self)
        self.date = self.cal.selectedDate() 
        self.label1.setText(self.date.toString())  

        self.label2 = QLabel(self) 
        previousBtn = QPushButton('이전 달')
        previousBtn.clicked.connect(self.preMonth)
        nextBtn = QPushButton('다음 달')
        nextBtn.clicked.connect(self.nextMonth)

        # selectedDate() : 현재 선택된 날짜를 반환

        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(previousBtn)
        vbox.addWidget(nextBtn)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 500, 400)
        self.show()

    def PastDate(self, date):  
        self.label1.setText(date.toString()) 
        self.label2.setText(f'2020년 1월 1일부터 {QDate(2020,1,1).daysTo(date)}일이 지났습니다.') 

        # - toStirng()을 통해 라벨에 선택된 날짜 표시
        # - 시작날짜.daysTo(날짜) : 시작날짜로부터 선택된 날짜까지의 일 수를 반환

    def preMonth(self):
        self.cal.showPreviousMonth()    # showPreviousMonth() : 현재 월 기준 1달전 달력을 보여줌

    def nextMonth(self):
        self.cal.showNextMonth()        #  showNextMonth() : 현재 월 기준 1달후 달력을 보여줌


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 달력위젯()
프로그램무한반복.exec_()