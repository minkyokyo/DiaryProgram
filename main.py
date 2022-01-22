import sys
from PyQt5.QtWidgets import *
#from PyQt5 import uic

app = QApplication(sys.argv)

#form_class = uic.loadUiType("MainWindow.ui")[0]
#print(form_class)

window = QWidget()
window.show()

app.exec_()
'''
class WindowClass(QMainWindow, form_class):
    def __init(self):
        super.setupUi(self)
        self.pushButton.clicked.connect(self.functionStart)
    
    def functionStart(self):
        f = open('일기장이름.txt','w')
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    Window = WindowClass()
    Window.show()
    app.exec_()
'''