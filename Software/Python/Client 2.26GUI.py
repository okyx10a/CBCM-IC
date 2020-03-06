# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import serial
import time
import sys
import struct
import threading
import queue
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


arduino = None





class CBCM_MainWindow(QtWidgets.QMainWindow):
    
    global N_sample
    N_sample = 1000
    
    
    def __init__(self):
        super(CBCM_MainWindow,self).__init__()
        uic.loadUi('GUI.ui',self)
        
        self.open_port_button.clicked.connect(self.openPort)# connect open port button handler
        self.set_param_button.clicked.connect(self.setParameter)# connect set parameter button handler
        self.set_cal_button.clicked.connect(self.setCalibration)# connect set calibration button handler
        self.start_scan_botton.clicked.connect(self.scanCalibration)# connect scan calibration button handler
        self.chemical_bio_test.clicked.connect(self.testScan)# connect chemical_bio_test button handler
        
    #open port button handler
    def openPort(self):
        try:
            #open port
            p_name = self.port_input.text()   
            b_rate = int(self.baudrate_input.text())   
            t_out = int(self.timeout_input.text())
            global arduino
            arduino = serial.Serial(p_name,baudrate = b_rate, timeout = t_out, writeTimeout = 5)
            text_browser_msg = "port opened on " + arduino.name + "\n"
            self.cmd_line_output.append(text_browser_msg)
            #change button to let it close port
            self.open_port_button.clicked.disconnect()# connect close port button handler
            self.open_port_button.setText("Close port")
            self.open_port_button.clicked.connect(self.closePort)# connect close port button handler
            
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
            self.open_port_button.clicked.disconnect()
            self.open_port_button.setText("Open port")
            self.open_port_button.clicked.connect(self.openPort)# connect close port button handler
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

    #RT-plot section
    def setCalibration(self): 
        try:
            global arduino
            global N_sample
            arduino.reset_input_buffer()
            if isBinaryString(self.cal_input.text()) and len(self.cal_input.text())==8:
                cmd = "W" + self.cal_input.text()
                arduino.write(cmd.encode())
                text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)
                self.set_cal_button.setText("Stop")
                self.set_cal_button.clicked.disconnect(self.setCalibration)
                self.set_cal_button.clicked.connect(self.stop)
                
            else:
                text_browser_msg = "Please input a 8-bit binary string as input sequence.\nCalibration not set"
                self.cmd_line_output.append(text_browser_msg)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)
            
            
    #scan calibration button handler
    def scanCalibration(self):
        try:
            #self.start_scan_botton.setEnabled(False)
            global arduino
            global N_sample   
            num_repeat = int(self.repeat_input.text())
            cs_bit = self.cs_bit_input.text()
            if not isBinaryString(cs_bit):
                cs_bit = ' '
            output = [[None]*128*N_sample for _ in range(num_repeat)]
            start_time = time.time()
            for j in range(num_repeat):
                arduino.reset_input_buffer()
                for x in range(128):
                    #arduino.reset_input_buffer()
                    cmd = "W"+str(format(x,'07b'))+cs_bit
                    arduino.write(cmd.encode())
                    #time.sleep(0.03)
                    text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                    # the above line ensures the arduino has finished writing the calibration sequence
                    self.cmd_line_output.append(text_browser_msg)
                    #time.sleep(0.01)
                    cmd = "R"
                    arduino.write(cmd.encode())
                    #time.sleep(0.01)
                    while not arduino.in_waiting:
                        pass                 
                    temp = arduino.read(size = 2*N_sample)
                    for i in range(N_sample):
                        output[j][x*N_sample+i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                    arduino.reset_input_buffer()
            text_browser_msg = "scan complete"
            self.cmd_line_output.append(text_browser_msg)
            time_spent = time.time()-start_time
            text_browser_msg = "time spent:" + str(time_spent) + "s"
            self.cmd_line_output.append(text_browser_msg)
            result = [[None]*128 for _ in range(num_repeat)]
            for j in range(num_repeat):
                for i in range(128):
                    result[j][i] = sum(output[j][i*N_sample:i*N_sample+N_sample])/N_sample
            for i in range(num_repeat):
                plt.plot(result[i])
            plt.show()
            if cs_bit == ' ':
                CCO = self.res_CCO_input.text()
                if CCO == "":
                    CCO = "111"
                file_name = "left "+CCO+".csv"
                f = open(file_name,"w+")
            else:
                CCO = self.res_CCO_input.text()
                if CCO == "":
                    CCO = "111"
                file_name = "right "+CCO+" "+cs_bit+".csv"
                f = open(file_name,"w+")
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

    def testScan(self):
        try:
            global arduino
            global N_sample
            num_repeat = int(self.repeat2_input.text())
            rep_interval = int(self.rep_interval_input.text())
            output_left = [[None]*128*N_sample for _ in range(num_repeat)]
            output_right = [[None]*128*N_sample for _ in range(num_repeat)]
            start_time = time.time()
            arduino.reset_input_buffer()
            for j in range(num_repeat):
                try:
                    #scanning left side
                    arduino.reset_input_buffer()
                    for x in range(128):
                        #arduino.reset_input_buffer()
                        cmd = "W"+str(format(x,'07b'))+ " "
                        arduino.write(cmd.encode())
                        #time.sleep(0.03)
                        text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                        # the above line ensures the arduino has finished writing the calibration sequence
                        #self.cmd_line_output.append(text_browser_msg)
                        #time.sleep(0.01)
                        cmd = "R"
                        arduino.write(cmd.encode())
                        #time.sleep(0.01)
                        while not arduino.in_waiting:
                            pass                 
                        temp = arduino.read(size = 2*N_sample)
                        for i in range(N_sample):
                            output_left[j][x*N_sample+i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                        arduino.reset_input_buffer()
                except SerialTimeoutException as ex:
                        output_left[j][x*N_sample+i] = 0

                try:
                    #scanning right side
                    arduino.reset_input_buffer()
                    for x in range(128):
                        #arduino.reset_input_buffer()
                        cmd = "W"+str(format(x,'07b'))+ "1"
                        arduino.write(cmd.encode())
                        #time.sleep(0.03)
                        text_browser_msg = "Set calibration to: " + arduino.readline().decode()
                        # the above line ensures the arduino has finished writing the calibration sequence
                        #self.cmd_line_output.append(text_browser_msg)
                        #time.sleep(0.01)
                        cmd = "R"
                        arduino.write(cmd.encode())
                        #time.sleep(0.01)
                        while not arduino.in_waiting:
                            pass                 
                        temp = arduino.read(size = 2*N_sample)
                        for i in range(N_sample):
                            output_right[j][x*N_sample+i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                        arduino.reset_input_buffer()
                except SerialTimeoutException as ex:
                    output_right[j][x*N_sample+i] = 0
                    
                time.sleep(rep_interval)
            text_browser_msg = "scan complete"
            self.cmd_line_output.append(text_browser_msg)
            time_spent = time.time()-start_time
            text_browser_msg = "time spent:" + str(time_spent) + "s"
            self.cmd_line_output.append(text_browser_msg)
            result_left = [[None]*128 for _ in range(num_repeat)]
            result_right = [[None]*128 for _ in range(num_repeat)]
            for j in range(num_repeat):
                for i in range(128):
                    result_left[j][i] = sum(output_left[j][i*N_sample:i*N_sample+N_sample])/N_sample
            for j in range(num_repeat):
                for i in range(128):
                    result_right[j][i] = sum(output_right[j][i*N_sample:i*N_sample+N_sample])/N_sample
            for i in range(num_repeat):
                plt.plot(result_left[i])
            for i in range(num_repeat):
                plt.plot(result_right[i])
            plt.show()
            
            f = open("test_records_left.csv","w+")
            for item in output_left:
                f.write("%s\n" % item)
            f.close()
            f = open("test_result_left.csv","w+")
            for item in result_left:
                f.write("%s\n" % item)
            f.close()
            f = open("test_records_right.csv","w+")
            for item in output_right:
                f.write("%s\n" % item)
            f.close()
            f = open("test_result_right.csv","w+")
            for item in result_right:
                f.write("%s\n" % item)
            f.close()
            

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
    MainWindow = CBCM_MainWindow()
    MainWindow.tabWidget.setCurrentIndex(0)
    app.aboutToQuit.connect(cleanUp)
    MainWindow.show()
    sys.exit(app.exec_())


