import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QLabel, QComboBox
from PyQt5.QtWidgets import QStyleFactory, QFontDialog, QColorDialog
from PyQt5.QtWidgets import QCalendarWidget, QTextEdit, QFileDialog


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('GUI Interface')
        self.setWindowIcon(QIcon('pyicon.png'))

        exitAction = QAction("Exit", self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit the Application')
        exitAction.triggered.connect(self.close)

        openeditor = QAction('Editor', self)
        openeditor.setShortcut('Ctrl+E')
        openeditor.setStatusTip('Open the Editor')
        openeditor.triggered.connect(self.editor)

        openfile = QAction('Open', self)
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open a File')
        openfile.triggered.connect(self.open_file)

        savefile = QAction('Save', self)
        savefile.setShortcut('Ctrl+S')
        savefile.setStatusTip('Save the File')
        savefile.triggered.connect(self.save_file)
        self.statusBar()
    

        main = self.menuBar()
        file = main.addMenu('File')
        file.addAction(exitAction)
        file.addAction(openfile)
        file.addAction(savefile)
        
        editor = main.addMenu('Editor')
        editor.addAction(openeditor)
        
        self.home()

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close)
        btn.resize(btn.minimumSizeHint())
        btn.move(10,100)

        exitAction = QAction(QIcon('pyicon.png'), 'Exit the Application', self)
        exitAction.triggered.connect(self.close)
        
        tool = self.addToolBar('Exit')
        tool.addAction(exitAction)

        font = QAction(QIcon('pyicon.png'), 'Choose Font', self)
        font.triggered.connect(self.choosefont)
        
        tool.addAction(font)

        color = QColor(0, 0, 0)
        fontcolor = QAction('Font BG Color', self)
        fontcolor.triggered.connect(self.colorpicker)

        tool.addAction(fontcolor)
        

        
        checkBox = QCheckBox('Enlarge Window',self)
        checkBox.move(200, 25)
##        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlargewindow)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(200, 80, 250, 20)

        dbtn = QPushButton('download', self)
        dbtn.move(200, 120)
        dbtn.clicked.connect(self.download)

        self.stylelabel = QLabel('GUI Style', self)

        dropdown = QComboBox(self)
        dropdown.addItem('WindowsVista')
        dropdown.addItem('Windows')
        dropdown.addItem('Fusion')
        dropdown.addItem('WindowsXP')


        dropdown.move(50,200)
        self.stylelabel.move(55,175)
        dropdown.activated[str].connect(self.style)

        cal = QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200,200)
        
        
        self.show()

    def save_file(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textedit.toPlainText()
        file.write(text)
        file.close()
        
    def open_file(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')

        self.editor()

        with file:
            self.textedit.setText(file.read())



        
    def editor(self):
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)



    
    def colorpicker(self):
        color = QColorDialog.getColor()

        self.stylelabel.setStyleSheet('QWidget {background-color: %s}'%color.name())


    def choosefont(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.stylelabel.setFont(font)
        
    def style(self, text):
        QApplication.setStyle(QStyleFactory.create(text))



    def download(self):
        progress = 0

        while progress < 100:
            progress += 0.0001
            self.pbar.setValue(progress)


    def enlargewindow(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def close(self):
        choice = QMessageBox.question(self, 'Exit', 'Exit the Application?',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
def run():
    app = QApplication(sys.argv)
    GUI = window()
    sys.exit(app.exec_())
                               
run()
                       
    
