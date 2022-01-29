import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#MainWindow.ui파일을 .py로 변환한 것을 불러온다.
from MainWindow import Ui_MainWindow

class WindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #UI 선언
        self.main_ui =Ui_MainWindow() #Ui_MainWindow()클래스가 메인 윈도우.
        self.main_ui.setupUi(self)
        self.main_ui.pushButton.clicked.connect(self.functionStart)
        self.show()
        #self.pushButton.clicked.connect(self.functionStart)
    
    def functionStart(self):
        f = open('일기장이름.txt','w')
        diary_content=self.main_ui.plainTextEdit.toPlainText()
        f.write(diary_content)
        f.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = WindowClass()
    app.exec_()
