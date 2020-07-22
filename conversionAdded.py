# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# from currency_in_chars import conversion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QGridLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 100, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setText("Click")
        self.button1.clicked.connect(lambda: self.conversion(654598620.67))
        self.label.setStyleSheet("text-align:center")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setShortcut("")
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.actionNew.triggered.connect(lambda: self.clicked("New Clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save Clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy Clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste Clicked"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def clicked(self,text):
    #     self.label.setText(text)
    #     self.label.adjustSize()

    def clicked(self,val1,val2):
        c = int(val1) + int(val2)
        self.label.setText(str(c))
        # self.label.adjustSize()
        self.label.setStyleSheet("text-align:center")


    def conversion(self,num):
        single = ['','one','two','three','four','five','six','seven','eight','nine','ten']
        double = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']
        tens = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
        cur = ['Thousand','Lakh','Crore']
        # print(num)
        l1 = []
        l2 = ""
        strg = ""
        counter = 0
        i1 = 0
        a = str(num)
        dotop = ""
        if('.' in a):
            b = a.index('.')
            dotop = a[b+1: :] + "/100"
            a = a[0:b:]
        
        a = '0' + a[0: :] if(len(a)%2==0) else a
        for i in range(len(a),0,-1):
            if(i == len(a)-1):
                l1.append(str(a[i-2]) +str(a[i-1]) + str(a[i]))
        i1 = 0
        for j in range(len(a)-3,0,-1):
            if(i1 % 2 != 0):
                l1.append(str(a[j-1]) + str(a[j]))
            i1 += 1

        length = len(l1)
        if(len(l1[0])==3):
            geth = l1[0][0]
            if(geth == '0'):
                
                strg += " "+str(double[int(l1[0][2])])+ "," if l1[0][1]=='1' else " "+str(tens[int(l1[0][1])]) +" "+ str(single[int(l1[0][2])])+ ","
            else:
                strg += " "+str(single[int(l1[0][0])]) + " Hundred " + "and"
                strg += " "+str(double[int(l1[0][2])])+ "," if l1[0][1]=='1' else " "+str(tens[int(l1[0][1])]) +" "+ str(single[int(l1[0][2])])+ ","
            l1.pop(0)

        for k in range(0,len(l1)):
            getm = l1[0]
            strg += " "+str(double[int(l1[0][1])]) + " " + str(cur[0]) + "," if l1[0][0]=='1' else " "+str(tens[int(l1[0][0])]) + " " + str(single[int(l1[0][1])]) + " " + str(cur[0]) + ","    
            cur.pop(0)
            l1.pop(0)

        strg1 = strg.split(',')
        strg1.reverse()
        for i in strg1:
            counter += 1
            l2 = l2 + str(i)  
            if(counter > length):
                break

        # return l2 + " "+dotop
        self.label.setText(l2 + " "+dotop)
        # self.label.adjustSize()
        self.label.setStyleSheet("text-align:center; color:red;margin: auto;horizontal-align:middle;")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
