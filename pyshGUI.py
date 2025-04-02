import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My firstly GUI")
        self.setGeometry(600,500,700,500) #(x,y,width,height)
        self.button=QPushButton("Click Me!",self)
        self.label=QLabel("Hi",self)
        self.initUI()
    
    def initUI(self):
        self.button.setGeometry(250,200,200,100)
        self.button.setStyleSheet('font-size:30px;')
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150,200,200,100)
        self.label.setStyleSheet("font-size:30px;")

    def on_click(self):
        self.label.setText("HiYahh")
        print("Button Clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

