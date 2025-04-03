import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00:00",self)
        self.start_button=QPushButton('Start',self)
        self.stop_button=QPushButton('Stop',self)
        self.reset_button=QPushButton('Reset',self)
        self.timer=QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stop Watch")
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
        QPushButton,QLabel{
            padding:20px;
            font-weight:bold;                   
        }
        QPushButton {
            font-size: 50px;
        }
        QLabel {
            font-size: 100px;
            color: hsl(111, 100%, 50%);
            background-color: black;
            border-radius:20px;
        }
    """)

    def start(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def format_time(self,time):
        pass

    def update_display(self):
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    clock=StopWatch()
    clock.show()
    sys.exit(app.exec_())