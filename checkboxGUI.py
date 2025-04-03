import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My firstly GUI")
        self.setGeometry(600,500,700,500) #(x,y,width,height)
        self.checkbox=QCheckBox("Do you like Python?",self)
        self.initUI()
    
    def initUI(self):
        self.checkbox.setGeometry(20,0,500,100)
        self.checkbox.setStyleSheet('font-size:30px;'
                                    'font-family:Times New Roman')
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)


    def checkbox_changed(self,state):
        if state == Qt.Checked:
            print("You like Python")
        else:
            print("You don't like Python")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

