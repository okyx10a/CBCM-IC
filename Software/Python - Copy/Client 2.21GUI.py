# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import sys
import struct
import matplotlib.pyplot as plt
import atexit
N_sample = 1000  



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 712)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.overall_layout = QtWidgets.QVBoxLayout()
        self.overall_layout.setContentsMargins(5, 5, 5, 5)
        self.overall_layout.setSpacing(5)
        self.overall_layout.setObjectName("overall_layout")

        #title section
        self.title_layout = QtWidgets.QHBoxLayout()
        self.title_layout.setContentsMargins(5, 5, 5, 5)
        self.title_layout.setSpacing(5)
        self.title_layout.setObjectName("title_layout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title.setObjectName("title")
        self.title_layout.addWidget(self.title)
        self.authors = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authors.sizePolicy().hasHeightForWidth())
        self.authors.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authors.setFont(font)
        self.authors.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.authors.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.authors.setObjectName("authors")
        self.title_layout.addWidget(self.authors)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setPixmap(QtGui.QPixmap("rsz_3lassonde_300.jpg"))
        self.logo.setObjectName("logo")
        self.title_layout.addWidget(self.logo)
        self.overall_layout.addLayout(self.title_layout)

        #tab section
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")

        #general parameter tab
        self.general_parameters = QtWidgets.QWidget()
        self.general_parameters.setObjectName("general_parameters")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.general_parameters)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gen_param_layout = QtWidgets.QVBoxLayout()
        self.gen_param_layout.setContentsMargins(5, 5, 5, 5)
        self.gen_param_layout.setSpacing(5)
        self.gen_param_layout.setObjectName("gen_param_layout")

            #number of samples label
        self.num_samp_hint = QtWidgets.QLabel(self.general_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_samp_hint.sizePolicy().hasHeightForWidth())   
        self.num_samp_hint.setSizePolicy(sizePolicy)
        self.num_samp_hint.setObjectName("num_samp_hint")
        self.gen_param_layout.addWidget(self.num_samp_hint)

            #number of samples line edit
        self.num_samp = QtWidgets.QLineEdit(self.general_parameters)
        self.num_samp.setObjectName("num_samp")
        self.gen_param_layout.addWidget(self.num_samp)

            #CCO resolution label
        self.res_CCO_hint = QtWidgets.QLabel(self.general_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_CCO_hint.sizePolicy().hasHeightForWidth())
        self.res_CCO_hint.setSizePolicy(sizePolicy)
        self.res_CCO_hint.setObjectName("res_CCO_hint")
        self.gen_param_layout.addWidget(self.res_CCO_hint)

            #COO resolution line edit
        self.res_CCO = QtWidgets.QLineEdit(self.general_parameters)
        self.res_CCO.setObjectName("res_CCO")
        self.gen_param_layout.addWidget(self.res_CCO)

            #set parameters button
        self.set_param = QtWidgets.QPushButton(self.general_parameters)
        self.set_param.setObjectName("set_param")
        self.gen_param_layout.addWidget(self.set_param)
        self.set_param.clicked.connect(self.setParameter)# connect set parameter button handler

            #spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gen_param_layout.addItem(spacerItem)

        #set calibration tab
        self.verticalLayout_7.addLayout(self.gen_param_layout)
        self.tabWidget.addTab(self.general_parameters, "")
        self.set_cal = QtWidgets.QWidget()
        self.set_cal.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.set_cal.setObjectName("set_cal")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.set_cal)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.set_cal_layout = QtWidgets.QVBoxLayout()
        self.set_cal_layout.setContentsMargins(5, 5, 5, 5)
        self.set_cal_layout.setSpacing(5)
        self.set_cal_layout.setObjectName("set_cal_layout")

            #calibration input label
        self.cal_input_hint = QtWidgets.QLabel(self.set_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_input_hint.sizePolicy().hasHeightForWidth())
        self.cal_input_hint.setSizePolicy(sizePolicy)
        self.cal_input_hint.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cal_input_hint.setObjectName("cal_input_hint")
        self.set_cal_layout.addWidget(self.cal_input_hint)

            #calibration input line edit
        self.cal_input = QtWidgets.QLineEdit(self.set_cal)
        self.cal_input.setObjectName("cal_input")
        self.set_cal_layout.addWidget(self.cal_input)

            #set calibration button
        self.set_cal_button = QtWidgets.QPushButton(self.set_cal)
        self.set_cal_button.setObjectName("set_cal_button")
        self.set_cal_layout.addWidget(self.set_cal_button)
        self.set_cal_button.clicked.connect(self.setCalibration)# connect set calibration button handler
        
            #spacer
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.set_cal_layout.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.set_cal_layout)

        #scan calibration tab
        self.tabWidget.addTab(self.set_cal, "")
        self.scan_cal = QtWidgets.QWidget()
        self.scan_cal.setObjectName("scan_cal")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scan_cal)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scan_cal_layout = QtWidgets.QVBoxLayout()
        self.scan_cal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scan_cal_layout.setContentsMargins(5, 5, 5, 5)
        self.scan_cal_layout.setSpacing(5)
        self.scan_cal_layout.setObjectName("scan_cal_layout")

            #scan calibration button
        self.start_scan = QtWidgets.QPushButton(self.scan_cal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_scan.sizePolicy().hasHeightForWidth())
        self.start_scan.setSizePolicy(sizePolicy)
        self.start_scan.setObjectName("start_scan")
        self.scan_cal_layout.addWidget(self.start_scan)
        self.start_scan.clicked.connect(self.scanCalibration)# connect scan calibration button handler
        
        self.verticalLayout_9.addLayout(self.scan_cal_layout)
        self.tabWidget.addTab(self.scan_cal, "")
        self.overall_layout.addWidget(self.tabWidget)
        
        #text browser
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setObjectName("textBrowser")
        self.overall_layout.addWidget(self.textBrowser)

        
        self.verticalLayout_3.addLayout(self.overall_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "CBCM IC"))
        self.authors.setText(_translate("MainWindow", "BioSA, E.Ghafar-Zadeh, K.Qiao"))
        self.num_samp_hint.setText(_translate("MainWindow", "Number of samples"))
        self.res_CCO_hint.setText(_translate("MainWindow", "CCO resulution"))
        self.set_param.setText(_translate("MainWindow", "Set parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_parameters), _translate("MainWindow", "General parameters"))
        self.cal_input_hint.setText(_translate("MainWindow", "Please enter calibration sequence in binary"))
        self.set_cal_button.setText(_translate("MainWindow", "Set calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_cal), _translate("MainWindow", "Set calibration"))
        self.start_scan.setText(_translate("MainWindow", "Start Scanning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_cal), _translate("MainWindow", "Scan calibration "))

    #set parameter button handler
    def setParameter(self): 
        arduino.write("G".encode())
        arduino.write(self.res_CCO.text().encode())
        time.sleep(0.01)
        arduino.write("S".encode())
        arduino.write(self.num_samp.text().encode())
        print("The number of samples for each calibration input is: ")
        print(arduino.readline().decode())

    #set calibration button handler
    def setCalibration(self):
        arduino.write("W".encode())
        arduino.write(self.cal_input.text().encode())
        output = [0]*N_sample
        cmd = "R"
        arduino.write(cmd.encode())
        time.sleep(0.01)
        while not arduino.in_waiting:
            pass                 
        temp = arduino.read(size = 2*N_sample)
        for i in range(N_sample):
            output[i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
        arduino.reset_input_buffer()  
        plt.plot(output)
        plt.show()      
        f = open("ST_records.csv","w+")
        for item in output:
            f.write("%s\n" % item)
        f.close()

    #scan calibration button handler
    def scanCalibration(self):
        output = [None]*128*N_sample
        try:
            for x in range(128):
                cmd = "W"+str(format(x,'07b'))
                arduino.write(cmd.encode())
                cmd = "R"
                arduino.write(cmd.encode())
                time.sleep(0.01)
                while not arduino.in_waiting:
                    pass                 
                temp = arduino.read(size = 2*N_sample)
                for i in range(N_sample):
                    output[x*N_sample+i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                arduino.reset_input_buffer()    
            plt.plot(output)
            plt.show()
            result = list()
            for i in range(128):
                result.append(sum(output[i*N_sample:i*N_sample+N_sample])/N_sample)
            plt.plot(result,'bo')
            plt.show()
            f = open("CT_records.csv","w+")
            for item in output:
                f.write("%s\n" % item)
            f.close()
            f = open("CT_results.csv","w+")
            for item in result:
                f.write("%s\n" % item)
            f.close()
        except KeyboardInterrupt:
            time.sleep(1)
            plot(output)
            pass

def closePort():
    arduino.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #open serial port on GUI creation
    arduino = serial.Serial('COM6',baudrate = 115200, timeout=1)
    print("port opened on " + arduino.name+"\n")
    #close serial port on GUI exit
    atexit.register(closePort)
    sys.exit(app.exec_())

