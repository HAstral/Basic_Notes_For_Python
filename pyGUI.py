import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My firstly GUI")
        self.setGeometry(600,500,700,500) #(x,y,width,height)
        self.setWindowIcon(QIcon("733316.jpg"))
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
        label=QLabel(self)
        label.setGeometry(0,0,300,250)
        pixmap=QPixmap("733316.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width()-label.width())//2,
                          (self.height()-label.height())//2,
                           label.width(),
                           label.height())
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()