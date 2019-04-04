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
import threading
import queue
import matplotlib.pyplot as plt


arduino = None


class Ui_MainWindow(object):
    
    global N_sample
    N_sample = 1000
    
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
        
        self.set_port_input_layout = QtWidgets.QHBoxLayout()
        self.set_port_input_layout.setObjectName("set_port_input_layout")
                #port label
        self.port_label = QtWidgets.QLabel(self.general_parameters)
        self.port_label.setObjectName("port_label")
        self.set_port_input_layout.addWidget(self.port_label)
                #port input
        self.port_input = QtWidgets.QLineEdit(self.general_parameters)
        self.port_input.setObjectName("port_input")
        self.set_port_input_layout.addWidget(self.port_input)
                #baudrate label
        self.baudrate_label = QtWidgets.QLabel(self.general_parameters)
        self.baudrate_label.setObjectName("baudrate_label")
        self.set_port_input_layout.addWidget(self.baudrate_label)
                #baudrate input
        self.baudrate_input = QtWidgets.QLineEdit(self.general_parameters)
        self.baudrate_input.setObjectName("baudrate_input")
        self.set_port_input_layout.addWidget(self.baudrate_input)
                #timeout label
        self.timeout_label = QtWidgets.QLabel(self.general_parameters)
        self.timeout_label.setObjectName("timeout_label")
        self.set_port_input_layout.addWidget(self.timeout_label)
                #timeout input
        self.timeout_input = QtWidgets.QLineEdit(self.general_parameters)
        self.timeout_input.setObjectName("timeout_input")
        self.set_port_input_layout.addWidget(self.timeout_input)
        self.gen_param_layout.addLayout(self.set_port_input_layout)
                #open port button
        self.port_button = QtWidgets.QPushButton(self.general_parameters)
        self.port_button.setObjectName("port_button")
        self.gen_param_layout.addWidget(self.port_button)
        self.port_button.clicked.connect(self.openPort)# connect open port button handler
                
        self.set_param_input_layout = QtWidgets.QHBoxLayout()
        self.set_param_input_layout.setObjectName("set_param_input_layout")
                #number of samples label
        self.num_samp_label = QtWidgets.QLabel(self.general_parameters)
        self.num_samp_label.setObjectName("num_samp_label")
        self.set_param_input_layout.addWidget(self.num_samp_label)
                #number of samples input
        self.num_samp_input = QtWidgets.QLineEdit(self.general_parameters)
        self.num_samp_input.setObjectName("num_samp_input")
        self.set_param_input_layout.addWidget(self.num_samp_input)
                #CCO resolution label
        self.res_CCO_label = QtWidgets.QLabel(self.general_parameters)
        self.res_CCO_label.setObjectName("res_CCO_label")
        self.set_param_input_layout.addWidget(self.res_CCO_label)
                #COO resolution input
        self.res_CCO_input = QtWidgets.QLineEdit(self.general_parameters)
        self.res_CCO_input.setObjectName("res_CCO_input")
        self.set_param_input_layout.addWidget(self.res_CCO_input)
                
        self.gen_param_layout.addLayout(self.set_param_input_layout)
                #set parameter button
        self.set_param_button = QtWidgets.QPushButton(self.general_parameters)
        self.set_param_button.setObjectName("set_param_button")
        self.gen_param_layout.addWidget(self.set_param_button)
        self.set_param_button.clicked.connect(self.setParameter)# connect set parameter button handler
                #spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gen_param_layout.addItem(spacerItem)   
        self.verticalLayout_7.addLayout(self.gen_param_layout)

            #set calibration tab
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
        self.cal_label = QtWidgets.QLabel(self.set_cal)
        self.cal_label.setObjectName("cal_label")
        self.set_cal_layout.addWidget(self.cal_label)
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
        self.start_scan_botton = QtWidgets.QPushButton(self.scan_cal)
        self.start_scan_botton.setObjectName("start_scan_botton")
        self.scan_cal_layout.addWidget(self.start_scan_botton)
        self.start_scan_botton.clicked.connect(self.scanCalibration)# connect scan calibration button handler
        
        self.verticalLayout_9.addLayout(self.scan_cal_layout)
        self.tabWidget.addTab(self.scan_cal, "")
        self.overall_layout.addWidget(self.tabWidget)
        self.tabWidget.setCurrentIndex(2)
        
        #command line output
        self.cmd_line_output = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd_line_output.sizePolicy().hasHeightForWidth())
        self.cmd_line_output.setSizePolicy(sizePolicy)
        self.cmd_line_output.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.cmd_line_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.cmd_line_output.setObjectName("cmd_line_output")
        self.overall_layout.addWidget(self.cmd_line_output)
        self.verticalLayout_3.addLayout(self.overall_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Canada))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "CBCM IC"))
        self.authors.setText(_translate("MainWindow", "BioSA, E.Ghafar-Zadeh, K.Qiao"))
        self.port_label.setText(_translate("MainWindow", "Port="))
        self.baudrate_label.setText(_translate("MainWindow", "Baudrate="))
        self.timeout_label.setText(_translate("MainWindow", "Timeout ="))
        self.port_button.setText(_translate("MainWindow", "Open port"))
        self.num_samp_label.setText(_translate("MainWindow", "Number of samples"))
        self.res_CCO_label.setText(_translate("MainWindow", "CCO resulution"))
        self.set_param_button.setText(_translate("MainWindow", "Set parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_parameters), _translate("MainWindow", "General parameters"))
        self.cal_label.setText(_translate("MainWindow", "Please enter calibration sequence in binary:"))
        self.set_cal_button.setText(_translate("MainWindow", "Set calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_cal), _translate("MainWindow", "Set calibration"))
        self.start_scan_botton.setText(_translate("MainWindow", "Start Scanning"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan_cal), _translate("MainWindow", "Scan calibration "))

        
    #open port button handler
    def openPort(self):
        try:
            #open port
            p_name = self.port_input.text()   
            b_rate = int(self.baudrate_input.text())   
            t_out = int(self.timeout_input.text())
            global arduino
            arduino = serial.Serial(p_name,baudrate = b_rate, timeout = t_out)
            text_browser_msg = "port opened on " + arduino.name + "\n"
            self.cmd_line_output.append(text_browser_msg)
            #change button to let it close port
            self.port_button.clicked.disconnect()# connect close port button handler
            self.port_button.setText("Close port")
            self.port_button.clicked.connect(self.closePort)# connect close port button handler
            
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)
            
    #close port button handler
    def closePort(self):
        try:
            global arduino
            arduino.close()
            text_browser_msg = "port closed\n"
            self.cmd_line_output.append(text_browser_msg)
            self.port_button.clicked.disconnect()
            self.port_button.setText("Open port")
            self.port_button.clicked.connect(self.openPort)# connect close port button handler
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)
        
    #set parameter button handler
    def setParameter(self):
        try:
            global arduino
            global N_sample
            arduino.reset_input_buffer()
            if isBinaryString(self.res_CCO_input.text()) and len(self.res_CCO_input.text())==3: 
                cmd = "G"+self.res_CCO_input.text()
                arduino.write(cmd.encode())
                text_browser_msg = "The CCO resolution configuration is: " + arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)
            else:
                text_browser_msg = "Please input a 3-bit binary string as CCO resolution.\nCCO resolution not set"
                self.cmd_line_output.append(text_browser_msg)
            if int(self.num_samp_input.text())<2048 and int(self.num_samp_input.text())>0:
                cmd = "S" + self.num_samp_input.text() + "\0"
                N_sample = int(self.num_samp_input.text())
                arduino.write(cmd.encode())       
                text_browser_msg = "The number of samples for each calibration input is: " + arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)
            else:
                text_browser_msg = "Please input an integer between 0 and 2048 as the number of samples.\nNumber of samples not set"
                self.cmd_line_output.append(text_browser_msg)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)

    #set calibration button handler
    def setCalibration(self): 
        try:
            global arduino
            global N_sample
            arduino.reset_input_buffer()
            if isBinaryString(self.cal_input.text()) and len(self.cal_input.text())==7:
                cmd = "W" + self.cal_input.text()
                arduino.write(cmd.encode())
                text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)
                self.cont_readout_thread = threading.Thread(target = self.cont_readout)
                self.cont_readout_thread.start()
                self.set_cal_button.setText("Stop")
                self.set_cal_button.clicked.disconnect(self.setCalibration)
                self.set_cal_button.clicked.connect(self.stop)
                
            else:
                text_browser_msg = "Please input a 7-bit binary string as calibration sequence.\nCalibration not set"
                self.cmd_line_output.append(text_browser_msg)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)

    #stop button
    def stop(self):
        self.cont_readout_thread.join()
        self.set_cal_button.setText("Set calibration")
        self.set_cal_button.clicked.connect(self.setCalibration)
        self.set_cal_button.clicked.disconnect(self.stop)

    #start a new thread for continuous read out
    def cont_readout(self):
        output = [0]*N_sample
        plot_data = queue.Queue(maxsize=100)
        for i in range(100):
            plot_data.put(0)
        plot_data_list = list(plot_data.queue)
        plt.plot(plot_data_list)
        plt.show()
        while True:
            cmd = "R"
            arduino.write(cmd.encode())
            time.sleep(0.01)
            while not arduino.in_waiting:
                pass                 
            temp = arduino.read(size = 2*N_sample)
            for i in range(N_sample):
                output[i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
            arduino.reset_input_buffer()
            plot_data.get()
            plot_data.put(sum(output)/1000)
            plot_data_list = list(plot_data.queue)
            plt.plot(plot_data_list)
            plt.draw()      
            f = open("ST_records.csv","w+")
            for item in output:
                f.write("%s\n" % item)
            f.close()

    #scan calibration button handler
    def scanCalibration(self):
        try:
            #self.start_scan_botton.setEnabled(False)
            global arduino
            global N_sample
            arduino.reset_input_buffer()
            #text_browser_msg = "scanning..."
            #self.cmd_line_output.append(text_browser_msg)
            output = [None]*128*N_sample
            for x in range(128):
                cmd = "W"+str(format(x,'07b'))
                arduino.write(cmd.encode())
                text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)
                cmd = "R"
                arduino.write(cmd.encode())
                time.sleep(0.01)
                while not arduino.in_waiting:
                    pass                 
                temp = arduino.read(size = 2*N_sample)
                for i in range(N_sample):
                    output[x*N_sample+i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                arduino.reset_input_buffer()
            text_browser_msg = "scan complete"
            self.cmd_line_output.append(text_browser_msg)
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
            self.start_scan_botton.setEnabled(True)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)
#end of Ui_MainWindow class

def isBinaryString(string): 
    # set function convert string 
    # into set of characters . 
    p = set(string) 
      
    # declare set of '0', '1' . 
    s = {'0', '1'} 
      
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one conditon 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}: 
        return True 
    else : 
        return False
    

def cleanUp():
    global arduino
    if arduino != None:
        arduino.close()
        print("port closed on exit\n")
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tabWidget.setCurrentIndex(0)
    app.aboutToQuit.connect(cleanUp)
    MainWindow.show()
    sys.exit(app.exec_())


