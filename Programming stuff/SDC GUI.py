# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SDC.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
from datetime import timedelta
import pandas as pd
import pandas_datareader.data as web
import csv


years = 1
days_per_year = 365.24

start = dt.date.today() - dt.timedelta(days=(years*days_per_year))
end = dt.date.today()

writer = pd.ExcelWriter('StockData.xlsx')



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

    #Add Stock Tab

        #Stock Code
        
        self.stocklabel = QtWidgets.QLabel(self.addtab)
        self.stocklabel.setGeometry(QtCore.QRect(20, 20, 361, 16))
        self.stocklabel.setObjectName("stocklabel")

        self.stockinput = QtWidgets.QLineEdit(self.addtab)
        self.stockinput.setGeometry(QtCore.QRect(20, 40, 91, 20))
        self.stockinput.setObjectName("stockinput")
        self.stockinput.setPlaceholderText('Stock Code')

        #Data Source
        
        self.sourcelabel = QtWidgets.QLabel(self.addtab)
        self.sourcelabel.setGeometry(QtCore.QRect(20, 80, 261, 16))
        self.sourcelabel.setObjectName("sourcelabel")
        
        self.sourceinput = QtWidgets.QLineEdit(self.addtab)
        self.sourceinput.setGeometry(QtCore.QRect(20, 100, 91, 20))
        self.sourceinput.setObjectName("sourceinput")
        self.sourceinput.setPlaceholderText('Data Source')
        self.sourceinput.setText('Google')

        #Add Button
        
        self.addbtn = QtWidgets.QPushButton(self.addtab)
        self.addbtn.setGeometry(QtCore.QRect(270, 20, 111, 121))
        self.addbtn.setObjectName("addbtn")
        #Define Add Button MYCODE
        self.addbtn.clicked.connect(self.add_stock)
        self.addbtn.setAutoDefault(True)
      
        self.tabWidget.addTab(self.addtab, "")

    #Update Stock Tab
        
        #Update Button
        
        self.updatetab = QtWidgets.QWidget()
        self.updatetab.setObjectName("updatetab")
        
        self.updatebtn = QtWidgets.QPushButton(self.updatetab)
        self.updatebtn.setGeometry(QtCore.QRect(30, 10, 75, 23))
        self.updatebtn.setObjectName("updatebtn")
        #Define Update Button MYCODE
        self.updatebtn.clicked.connect(self.update)
        
        #Stock list display
        self.stocklist = QtWidgets.QTextEdit(self.updatetab)
        self.stocklist.setGeometry(QtCore.QRect(120, 10, 271, 141))
        self.stocklist.setObjectName("stocklist")
        self.tabWidget.currentChanged.connect(self.updatelist)

        self.savebtn = QtWidgets.QPushButton(self.updatetab)
        self.savebtn.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.savebtn.setObjectName('Save')
        self.savebtn.clicked.connect(self.savelist)
        

        self.tabWidget.addTab(self.updatetab, "")

    #Other        
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Add Stock Method
    def add_stock(self):
        source=self.sourceinput.text()
        stock_code=self.stockinput.text()
        with open('Stock_list.csv', 'r') as Stock_list:
            reader = csv.reader(Stock_list)
            if ([stock_code, source] in reader) is False and (source is not "" and stock_code is not "") :
                with open('Stock_list.csv', 'a', newline="") as Stock_add:
                    csv_writer = csv.writer(Stock_add)
                    csv_writer.writerow([stock_code, source])
        self.stockinput.clear()

    def update(self):
        with open('Stock_list.csv', 'r') as Stock_list:
            reader = csv.reader(Stock_list)
            for [stock_code, source] in reader:
                print("Updating: {}".format(stock_code))
                df = web.DataReader(stock_code, source, start, end)
                df.to_excel(writer, sheet_name="{}".format(stock_code))
                writer.save()
                print("Updated: {}".format(stock_code))

    def updatelist(self):
        stocklist = open('Stock_list.csv', 'r')
        self.stocklist.setText(stocklist.read())

    def savelist(self):
        stocklist = open('Stock_list.csv', 'w')
        text = self.stocklist.toPlainText()
        stocklist.write(text)
        stocklist.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Data Compiler"))
        self.stocklabel.setText(_translate("MainWindow", "Stock Code (TSLA for Tesla etc.):"))
        self.sourcelabel.setText(_translate("MainWindow", "Data Source (Google for Google Finance etc.)"))
        self.addbtn.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addtab), _translate("MainWindow", "Add Stock"))
        self.updatebtn.setText(_translate("MainWindow", "Update"))
        self.savebtn.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updatetab), _translate("MainWindow", "Update Stock"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

