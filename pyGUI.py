import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My firstly GUI")
        self.setGeometry(600,500,700,500) #(x,y,width,height)
        self.initUI()
        # self.setWindowIcon(QIcon("733316.jpg"))
        # label = QLabel("Hello MadaFaka",self)
        # label.setFont(QFont('Times New Roman',35))
        # label.setGeometry(0,0,600,100)
        # label.setStyleSheet('color:salmon;'
        #                     'background-color:gold;'
        #                     'font-weight:semi-bold;'
        #                     'font-style:italic;'
        #                     'text-decoration:underline;'
        #                     )
        # label.setAlignment(Qt.AlignTop)#AlignCenter,AlignBottom,AlignRight,AlignLeft,AlignHCenter
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignCenter)
        # label=QLabel(self)
        # label.setGeometry(0,0,300,250)
        # pixmap=QPixmap("733316.jpg")
        # label.setPixmap(pixmap)
        # label.setScaledContents(True)
        # label.setGeometry((self.width()-label.width())//2,
        #                   (self.height()-label.height())//2,
        #                    label.width(),
        #                    label.height())

    def initUI(self):
            central_widget=QWidget()
            self.setCentralWidget(central_widget)
            label1= QLabel("#1",self)
            label2= QLabel("#2",self)
            label3= QLabel("#3",self)
            label4= QLabel("#4",self)
            label5= QLabel("#5",self)
            label6= QLabel("#6",self)
            label1.setStyleSheet('background-color:orange;')
            label2.setStyleSheet('background-color:red;')
            label3.setStyleSheet('background-color:blue;')             
            label4.setStyleSheet('background-color:purple;') 
            label5.setStyleSheet('background-color:green;') 
            label6.setStyleSheet('background-color:yellow;') 

            # vbox=QVBoxLayout() #can use hbox instead of vbox
            # vbox.addWidget(label1)
            # vbox.addWidget(label2)
            # vbox.addWidget(label3)
            # vbox.addWidget(label4)
            # vbox.addWidget(label5)
            # vbox.addWidget(label6)
            # central_widget.setLayout(vbox)
            grid=QGridLayout() #can use hbox instead of grid
            grid.addWidget(label1,0,0)
            grid.addWidget(label2,0,1)
            grid.addWidget(label3,0,2)
            grid.addWidget(label4,1,0)
            grid.addWidget(label5,1,1)
            grid.addWidget(label6,1,2)
            central_widget.setLayout(grid)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()