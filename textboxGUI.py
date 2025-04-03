import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My firstly GUI")
        self.setGeometry(600,500,700,500) #(x,y,width,height)
        self.line_edit=QLineEdit(self)
        self.button=QPushButton('Submit',self)
        self.initUI()


    def initUI(self):
        self.line_edit.setGeometry(10,10,400,100)
        self.line_edit.setStyleSheet('font-size:30px;'
                                    'font-family:Arial;'
                                        )
        self.button.setGeometry(410,10,100,100)
        self.button.setStyleSheet('font-size:30px;'
                                    'font-family:Arial;'
                                        )
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter whatever you want")
    def submit(self):
        text=self.line_edit.text()
        print(f"You entered: {text}")
 

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

