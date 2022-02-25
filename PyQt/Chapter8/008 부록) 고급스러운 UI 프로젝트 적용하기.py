# 아래 2개의 프로젝트를 적용하면 좀 더 고급스러운 UI 연출이 가능

'''
1. Project
 Project Name : Qt-Material
 https://github.com/UN-GCPDS/qt-material
------------------------------------------------------------------------
 Project Name : Dracula
 https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6

2. Code
여기서는 Qt-Material 프로젝트를 사용
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from qt_material import apply_stylesheet # pip install qt-material

def helloworld():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!")
   textLabel.move(150, 200)

   widget.setGeometry(50, 50, 400, 400)
   widget.setWindowTitle("PyQt5 Example")

   apply_stylesheet(app, theme='dark_teal.xml')

   widget.show()
   sys.exit(app.exec_())

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = helloworld()
프로그램무한반복.exec_()