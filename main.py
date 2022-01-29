import sys
import os

from PyQt5.QtWidgets import *

#MainWindow.ui파일을 .py로 변환한 것을 불러온다.
from DiaryWindow import Ui_MainWindow
from overwriteDialog import Ui_Dialog as Form

class WindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #UI 선언
        self.main_ui =Ui_MainWindow() #Ui_MainWindow()클래스가 메인 윈도우.
        self.main_ui.setupUi(self)
        self.main_ui.saveButton.clicked.connect(self.functionStart)
        self.show()
        #self.pushButton.clicked.connect(self.functionStart)
    
    def functionStart(self):
        diary_title = self.main_ui.diaryTitle.toPlainText()
        diary_date = self.main_ui.dirayDate.text()
        
        self.path = diary_date
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.path = diary_date+"/"+diary_title+".txt"
        
        if os.path.exists(self.path):
            #덮어쓸 것이냐고 물어본다.
            if self.showDialog()==0:
                f = open(self.path,'w')
                diary_content=self.main_ui.diaryText.toPlainText()
                f.write(diary_content)
                f.close()
        else:
            f = open(self.path,'w')
            diary_content=self.main_ui.diaryText.toPlainText()
            f.write(diary_content)
            f.close()
            
    def showDialog(self):
        dialog =QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        #exec_와 show의 차이가 뭐지?...
        return dialog.exec_()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = WindowClass()
    app.exec_()
