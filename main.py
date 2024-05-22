import sys
from PyQt5.QtWidgets import QApplication, QWidget
class Calculator(QWidget):
      
    def __init__(self):
        super().__init__()                          # 부모 클래스 Qwidget을 초기화
        self.initUI()                               # 나머지 초기화는 initUI 함수의 정의
    
    def initUI(self):         
        self.setWindowTitle('Calculator')           # 윈도에 표시되는 타이틀
        self.resize(256, 256)                       # 원도 사이즈
        self.show()                                 # 원도 화면이 표시되도록 호출

if __name__=='__main__':                            
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
