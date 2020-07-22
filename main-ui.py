# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 525)

        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.centralwidget.setStyleSheet("background-image:url('blue.jpg')")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color:white;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.gridLayout_4.addLayout(self.formLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("color:black;background-color:white")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem4, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.check_1)
        spacerItem6 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 7, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 8, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setStyleSheet("color:white;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_3.addWidget(self.textEdit_2, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 8, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(80, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 8, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 9, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("")
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem14, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setStyleSheet("border:3px solid grey;color:black;background-color:white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        spacerItem15 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.convertfile_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.convertfile_button.setFont(font)
        self.convertfile_button.setStyleSheet("background-color:grey;color:white;width:50px;")
        self.convertfile_button.setObjectName("convertfile_button")
        self.horizontalLayout_3.addWidget(self.convertfile_button)
        self.convertfile_button.clicked.connect(self.check_2)
        spacerItem16 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem17, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_path = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.file_path.setFont(font)
        self.file_path.setStyleSheet("color:white;")
        self.file_path.setObjectName("file_path")
        self.horizontalLayout.addWidget(self.file_path)
        self.lineEdit_file_path = QtWidgets.QLineEdit(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_file_path.setFont(font)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.horizontalLayout.addWidget(self.lineEdit_file_path)
        self.lineEdit_file_path.setStyleSheet("color:white")
        self.browse_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.browse_button.setFont(font)
        self.browse_button.setStyleSheet("background-color:mediumslateblue;color:white;")
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout.addWidget(self.browse_button)
        self.browse_button.clicked.connect(self.path)
        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem18, 2, 0, 1, 1)
        self.res_label = QtWidgets.QLabel(self.tab_4)
        self.res_label.setText("")
        self.res_label.setObjectName("res_label")
        self.gridLayout_5.addWidget(self.res_label, 9, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem19, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.column_no = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.column_no.setFont(font)
        self.column_no.setStyleSheet("color:white;")
        self.column_no.setObjectName("column_no")
        self.horizontalLayout_2.addWidget(self.column_no)
        self.spinBox_file = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_file.setStyleSheet("border:3px solid grey;color:grey;")
        self.spinBox_file.setObjectName("spinBox_file")
        self.horizontalLayout_2.addWidget(self.spinBox_file)
        spacerItem20 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem21, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 18pt \"Yu Gothic UI\";color:white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textEdit_2.setReadOnly(True) 
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.counter_val = 0

    def path(self):
        file_path = QFileDialog.getOpenFileName()
        file_path = list(file_path)
        self.lineEdit_file_path.setText(str(file_path[0]))

    def check_2(self):
        self.counter_val = 2
        column = int(self.spinBox_file.text())-1
        lang = self.comboBox.currentText()
        path_line = self.lineEdit_file_path.text()
        path_line = path_line.split('/')
        file_name = str(path_line[-1])
        try:
            file1 = open(file_name,'r')
            data = file1.readlines()
            data_list = []
            row_data = []
            file1.close() 

            for i in data:
                try:
                    i = i.split(',')        # Use try except to handle index out of range
                    val = str(i[column].split("\n")[0])
                    data_list.append(float(val))
                except:
                    val = ""
                    data_list.append(val)
                i.insert(column,val)
                i.pop(-1)
                row_data.append(i)
                c = 0
                file_name1 = file_name.split('.')[0]
                for j in data_list:
                    # output = "Amount in Characters:{}\n".format(conversion(j))
                    if(j == ""):
                        output = ""
                    else:
                        if(lang == "English"):
                            output = self.conversion(j)
                        elif(lang == "Hindi"):
                            output = self.conv_hindi(j)
                        elif(lang == "Marathi"):
                            output = self.conv_marathi(j)
                    record_file = open(file_name1+'-converted.txt','a', encoding='utf8')
                    row_data[c].insert(len(row_data[c]),output)
                    string = ','.join(row_data[c])
                    record_file.write(string+"\n")
                    record_file.close()
                    c += 1     
                self.res_label.setText("File Created Successfully")
                self.res_label.setStyleSheet("color:green;")
        except FileNotFoundError:
            self.res_label.setText("File not found.")
            self.res_label.setStyleSheet("color:red")
        except PermissionError:
            # print("Can't Perform the Operation because the file is Already Opened in Another Program")
            self.res_label.setText("Can't Perform the Operation because the file is Already Opened in Another Program")
            self.res_label.setStyleSheet("color:red")



    def check_1(self):
        self.counter_val = 1
        num = self.lineEdit.text()
        lang = self.comboBox_2.currentText()
        if(lang == "English"):
            self.conversion(num)
        elif(lang == "Hindi"):
            self.conv_hindi(num)
        elif(lang == "Marathi"):
            self.conv_marathi(num)




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

        if(self.counter_val == 1):
            self.textEdit_2.setText(num+" - "+l2 + " "+dotop)
        elif(self.counter_val == 2):
            return l2 + " "+dotop



    def conv_hindi(self,num):
        dic_hindi = {0:"",1:"एक",2:"दो",3:"तीन",4:"चार",5:"पांच",6:"छह",7:"सात",8:"आठ",9:"नौ",10:"दस",
        11:"ग्यारह",12:"बारह",13:"तेरह",14:"चौदह",15:"पंद्रह",16:"सोलह",17:"सत्रह",18:"अठारह",19:"उन्नीस",20:"बीस",21:"इकीस",22:"बाईस",23:"तेइस",
        24:"चौबीस",25:"पच्चीस",26:"छब्बीस",27:"सताइस",28:"अट्ठाइस",29:"उनतीस",30:"तीस",31:"इकतीस",32:"बतीस",33:"तैंतीस",34:"चौंतीस",35:"पैंतीस",36:"छतीस",
        37:"सैंतीस",38:"अड़तीस",39:"उनतालीस",40:"चालीस",41:"इकतालीस",42:"बयालीस",43:"तैतालीस",44:"चवालीस",45:"पैंतालीस",46:"छयालिस",47:"सैंतालीस",
        48:"अड़तालीस",49:"उनचास",50:"पचास",51:"इक्यावन",52:"बावन",53:"तिरपन",54:"चौवन",55:"पचपन",56:"छप्पन",57:"सतावन",58:"अठावन",59:"उनसठ",
        60:"साठ",61:"इकसठ",62:"बासठ",63:"तिरसठ",64:"चौंसठ",65:"पैंसठ",66:"छियासठ",67:"सड़सठ",68:"अड़सठ",69:"उनहतर",70:"सत्तर",71:"इकहतर",
        72:"बहतर",73:"तिहतर",74:"चौहतर",75:"पचहतर",76:"छिहतर",77:"सतहतर",78:"अठहतर",79:"उन्नासी",80:"अस्सी",81:"इक्यासी",82:"बयासी",83:"तिरासी",
        84:"चौरासी",85:"पचासी",86:"छियासी",87:"सतासी",88:"अट्ठासी",89:"नवासी",90:"नब्बे",91:"इक्यानवे",92:"बानवे",93:"तिरानवे",94:"चौरानवे",95:"पचानवे",
        96:"छियानवे",97:"सतानवे",98:"अट्ठानवे",99:"निन्यानवे",100:"एक सौ"}
        
        a = str(num)
        l1 = []
        list_hindi = ["हज़ार","लाख","करोड़"]
        strg = ""
        number = ""
        l2 = ""
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
                number += l1[0][1] + l1[0][2]
                strg += dic_hindi[int(number)]
            else:
                number += l1[0][1] + l1[0][2]
                strg += dic_hindi[int(l1[0][0])] + "सौ" +" "+ dic_hindi[int(number)] + ","
            l1.pop(0)

        for k in range(0,len(l1)):
            strg += dic_hindi[int(str(l1[0][0])+str(l1[0][1]))] +" "+str(list_hindi[0]) + ","
            list_hindi.pop(0)
            l1.pop(0)

        strg1 = strg.split(',')
        strg1.reverse()
        for i in strg1:
            l2 = l2 +" "+i 

        self.textEdit_2.setText(num+" - "+l2 + " "+dotop)
        # return l2 +" "+dotop


    def conv_marathi(self,num):
        dic_marathi = {0:"शून्य",1:"एक",2:"दोन",3:"तीन",4:"चार",5:"पाच",6:"सहा",7:"सात",8:"आठ",9:"नऊ",10:"दहा",11:"अकरा",
        12:"बारा",13:"तेरा",14:"चौदा",15:"पंधरा",16:"सोळा",17:"सतरा",18:"अठरा",19:"एकोणीस",20:"वीस",21:"एकवीस",22:"बावीस",
        23:"तेवीस",24:"चोवीस",25:"पंचवीस",26:"सव्वीस",27:"सत्तावीस",28:"अठ्ठावीस",29:"एकोणतीस",
        30:"तीस",31:"एकतीस",32:"बत्तीस",33:"तेहेतीस",34:"चौतीस",35:"पस्तीस",36:"छत्तीस",37:"सदतीस",38:"अडतीस",39:"एकोणचाळीस",
        40:"चाळीस",41:"एक्केचाळीस",42:"बेचाळीस",43:"त्रेचाळीस",44:"चव्वेचाळीस",45:"पंचेचाळीस",46:"सेहेचाळीस",47:"सत्तेचाळीस",
        48:"अठ्ठेचाळीस",49:"एकोणपन्नास",50:"पन्नास",51:"एक्कावन्न",52:"बावन्न",53:"त्रेपन्न",54:"चोपन्न",55:"पंचावन्न",56:"छप्पन्न",57:"सत्तावन्न",
        58:"अठ्ठावन्न",59:"एकोणसाठ",60:"साठ",61:"एकसष्ठ",62:"बासष्ठ",63:"त्रेसष्ठ",64:"चौसष्ठ",65:"पासष्ठ",66:"सहासष्ठ",67:"सदुसष्ठ",68:"अडुसष्ठ",
        69:"एकोणसत्तर",70:"सत्तर",71:"एक्काहत्तर",72:"बाहत्तर",73:"त्र्याहत्तर",74:"चौर्‍याहत्तर",75:"पंच्याहत्तर",76:"शहात्तर",77:"सत्याहत्तर",78:"अठ्ठ्याहत्तर",
        79:"एकोण ऐंशी",80:"ऐंशी",81:"एक्क्याऐंशी",82:"ब्याऐंशी",83:"त्र्याऐंशी",84:"चौऱ्याऐंशी",85:"पंच्याऐंशी",
        86:"शहाऐंशी",87:"सत्त्याऐंशी",88:"अठ्ठ्याऐंशी",89:"एकोणनव्वद",90:"नव्वद",91:"एक्क्याण्णव",92:"ब्याण्णव",93:"त्र्याण्णव",
        94:"चौऱ्याण्णव",95:"पंच्याण्णव",96:"शहाण्णव",97:"सत्त्याण्णव",98:"अठ्ठ्याण्णव",99:"नव्व्याण्णव",100:"शंभर"}
        l1 = []
        list_hindi = ["हज़ार","लाख","करोड़"]
        strg = ""
        number = ""
        l2 = ""

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
                number += l1[0][1] + l1[0][2]
                strg += dic_marathi[int(number)]
            else:
                number += l1[0][1] + l1[0][2]
                strg += dic_marathi[int(l1[0][0])] + "शे" +" "+ dic_marathi[int(number)] + ","
            l1.pop(0)

        for k in range(0,len(l1)):
            strg += dic_marathi[int(str(l1[0][0])+str(l1[0][1]))] +" "+str(list_hindi[0]) + ","
            list_hindi.pop(0)
            l1.pop(0)

        strg1 = strg.split(',')
        strg1.reverse()
        for i in strg1:
            l2 = l2 +" "+i 

        # return l2 +" "+dotop
        self.textEdit_2.setText(num+" - "+l2 + " "+dotop)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency to Text Converter"))
        self.label_2.setText(_translate("MainWindow", "Input: "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Hindi"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Marathi"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Convert"))
        self.label_4.setText(_translate("MainWindow", "Language:                  "))
        self.comboBox.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hindi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Marathi"))
        self.convertfile_button.setText(_translate("MainWindow", "Convert"))
        self.file_path.setText(_translate("MainWindow", "File Path: "))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.column_no.setText(_translate("MainWindow", "Enter Column no.: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Insert a File"))
        self.label.setText(_translate("MainWindow", "Welcome to Currency \n"
"   to Text Converter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
