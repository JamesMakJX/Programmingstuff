# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SDC.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 206)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 411, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.addtab = QtWidgets.QWidget()
        self.addtab.setToolTip("")
        self.addtab.setObjectName("addtab")
        self.stocklabel = QtWidgets.QLabel(self.addtab)
        self.stocklabel.setGeometry(QtCore.QRect(20, 20, 361, 16))
        self.stocklabel.setObjectName("stocklabel")
        self.sourceinput = QtWidgets.QLineEdit(self.addtab)
        self.sourceinput.setGeometry(QtCore.QRect(20, 100, 91, 20))
        self.sourceinput.setObjectName("sourceinput")
        self.sourcelabel = QtWidgets.QLabel(self.addtab)
        self.sourcelabel.setGeometry(QtCore.QRect(20, 80, 261, 16))
        self.sourcelabel.setObjectName("sourcelabel")
        self.stockinput = QtWidgets.QLineEdit(self.addtab)
        self.stockinput.setGeometry(QtCore.QRect(20, 40, 91, 20))
        self.stockinput.setObjectName("stockinput")
        self.addbtn = QtWidgets.QPushButton(self.addtab)
        self.addbtn.setGeometry(QtCore.QRect(270, 20, 111, 121))
        self.addbtn.setObjectName("addbtn")
        self.tabWidget.addTab(self.addtab, "")
        self.updatetab = QtWidgets.QWidget()
        self.updatetab.setObjectName("updatetab")
        self.updatebtn = QtWidgets.QPushButton(self.updatetab)
        self.updatebtn.setGeometry(QtCore.QRect(30, 10, 75, 23))
        self.updatebtn.setObjectName("updatebtn")
        self.stocklist = QtWidgets.QTableView(self.updatetab)
        self.stocklist.setGeometry(QtCore.QRect(120, 10, 271, 141))
        self.stocklist.setObjectName("stocklist")
        self.tabWidget.addTab(self.updatetab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Data Compiler"))
        self.stocklabel.setText(_translate("MainWindow", "Stock Code (TSLA for Tesla etc.):"))
        self.sourcelabel.setText(_translate("MainWindow", "Data Source (Yahoo for Yahoo Finance etc.)"))
        self.addbtn.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addtab), _translate("MainWindow", "Add Stock"))
        self.updatebtn.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updatetab), _translate("MainWindow", "Update Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

