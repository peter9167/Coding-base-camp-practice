from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, \
                            QLabel, QTimeEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime
import sys

# QTime, QDate, QDateTime 라이브러리는 같이 활용되는 함수(현재시간,날짜 구하기 등)

class 시간날짜편집기(QWidget):

    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        #### QTimeEdit ####
        label = QLabel('QTimeEdit')
        label.setAlignment(Qt.AlignCenter)

        time = QTimeEdit(self)
        time.setTime(QTime.currentTime())
        time.setTimeRange(QTime(00, 00, 00), QTime.currentTime())
        time.setDisplayFormat('a:hh:mm:ss.zzz')
        
        '''
        - CurrentTime() : 현재 시간 값 , default = 00 시 00분 00초 000밀리초 ~ 23시 59분 59초 999초
        - setTimeRange(시작값,마지막 값) : 위와 같이 설정하면 프로그램을 실행한 시간 이후로는 선택이 불가능
        - setDisplayFormat(표현식) : 보여질 표현식 설정 a = 오후,오전 표기 , zzz= 밀리초 표기
        '''

        #### /QTimeEdit ####

        #### QDateEdit ####
        label2 = QLabel('QDateEdit')
        label2.setAlignment(Qt.AlignCenter)

        date_edit = QDateEdit(self)
        date_edit.setDate(QDate.currentDate()) 
        date_edit.setDateRange(QDate(2000, 1, 1), QDate.currentDate())
        date_edit.dateChanged.connect(self.dateChange)

        label3 = QLabel('이곳에 QDateEdit에서 선택된 값이 나타납니다.')
        label3.setAlignment(Qt.AlignCenter)

        '''
        - CurrentDate() : 현재 날짜를 반환
        - setDateRange(시작 날짜, 끝 날짜) : 여기서는 2000년 1월 1일 부터 현재 날짜 까지 선택 가능
        - dataChanged : 날짜가 변경되면 시그널 발생
        '''

        #### /QDateEdit ####

        #### QDateTimeEdit (QDateEdit + QTimeEdit) ####
        label4 = QLabel('QDateTimeEdit')
        label4.setAlignment(Qt.AlignCenter)

        label5 = QLabel(self)
        label5.setAlignment(Qt.AlignCenter)
        label5.setText(f'QDateTime \n 현재 시간은 {QDateTime.currentDateTime().toString("yyyy년 MMMM d월 ap hh시 mm분 ss초.zzz")} 입니다.')

        dt_edit = QDateTimeEdit(self)

        dt_edit.setDateTimeRange(QDateTime(2020, 1, 1, 00, 00, 00),\
                                 QDateTime(2021, 1, 1, 00, 00, 00))
        dt_edit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        '''
        - CurrentDateTime() : 현재 날짜와 시간을 반환
        - setDateTimeRange(시작값,끝값) : 위와 같은 경우 2020년 1월 1일 00시 00분 00초 부터 2021년 1월 1일 00시 00분 00 초 까지 선택가능
        '''

        #### /QDateTimeEdit (QDateEdit + QTimeEdit) ####

        vbox = QVBoxLayout()

        vbox.addWidget(label)
        vbox.addWidget(time)
        vbox.addWidget(label2)
        vbox.addWidget(date_edit)
        vbox.addWidget(label3)
        vbox.addWidget(label5)
        vbox.addWidget(dt_edit)

        self.setLayout(vbox)

        self.setWindowTitle('Q Time,Date Edit')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def dateChange(self): # toString(표현식) 으로 현재 선택된 날짜를 라벨에 업데이트
        self.label3.setText(self.date_edit.date().toString('yyyy년 MMMM d일'))


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 시간날짜편집기()
프로그램무한반복.exec_()