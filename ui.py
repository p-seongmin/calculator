from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QMessageBox, QPlainTextEdit, 
                             QHBoxLayout, QLineEdit, QComboBox)   # 애플리케이션 핸들러와 빈 GUI 위젯
from PyQt5.QtGui import QIcon                       # icon을 추가하기 위한 라이브러리
from PyQt5 import QtCore

class View(QWidget):
      
    def __init__(self):
        super().__init__()                          # 부모 클래스 Qwidget을 초기화
        self.initUI()                               # 나머지 초기화는 initUI 함수의 정의
    
    def initUI(self):         

        self.te1=QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1=QPushButton("Message", self)              # 버튼 추가
        self.btn2=QPushButton("Clear", self)

        self.le1=QLineEdit('0', self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        self.le2=QLineEdit('0', self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        self.cb.addItems(['=', '-', '*', '/'])

        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()                        # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)                          # 빈 공간

        self.setLayout(vbox)                        # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle("Calculator")           # 윈도에 표시되는 타이틀
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)                       # 원도 사이즈
        self.show()                                 # 원도 화면이 표시되도록 호출

    def activateMessage(self, text):
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()