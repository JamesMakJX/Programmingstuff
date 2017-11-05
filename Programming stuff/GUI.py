import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("GUI Interface")
        self.setWindowIcon(QtGui.QIcon('pyicon.png'))
        
        extractAction = QtGui.QActionEvent('exit', self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)
        
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)
        
        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        
        btn.resize(btn.minimumsizeHint())
        btn.move(0, 100)

        self.show()

    def close_application(self):
        print("closed")
        sys.exit()

def run():                                                  
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
