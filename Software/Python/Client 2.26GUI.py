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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure








class CBCM_MainWindow(QtWidgets.QMainWindow):
    

    #open port button handler
    def openPort(self):
        try:
            #open port
            p_name = self.port_input.text()   
            self.arduino = serial.Serial(p_name,baudrate = 115200, timeout = 5, writeTimeout = 5)
            text_browser_msg = "port opened on " + self.arduino.name + "\n"
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
            self.arduino.close()
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
            self.arduino.reset_input_buffer()
            if int(self.num_samp_input.text())<2048 and int(self.num_samp_input.text())>0:
                cmd = "S" + self.num_samp_input.text() + "\0"
                self.N_sample = int(self.num_samp_input.text())
                self.arduino.write(cmd.encode())       
                text_browser_msg = "The number of samples for each calibration input is: " + self.arduino.readline().decode()
                self.cmd_line_output.append(text_browser_msg)

                cmd = "F" + self.phi12.currentText() + self.phi3.currentText() #1) send scale ratio; 2) phi3 should have the same scaler as phi1&2
                self.arduino.write(cmd.encode())       
                text_browser_msg = "Phi1 & Phi2 frequency are set to: " + self.phi12.currentText() + "Hz\nPhi3 frequency is set to: " + self.phi3.currentText() + "Hz\n"
                self.cmd_line_output.append(text_browser_msg)                
            else:
                text_browser_msg = "Please input an integer between 0 and 2048 as the number of samples.\nNumber of samples not set"
                self.cmd_line_output.append(text_browser_msg)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)

    #RT-plot section
    #select left or right, swap the plot on the right to a graph that contains all data point up till now, change the y axis scale
    #Y axis auto adjust so that we can observe the tiny changes in the signal
    #the scale can not be too small so that noise is displayed in a too significant way
    def setCalibration(self): 
        try:
            self.arduino.reset_input_buffer()
            if isBinaryString(self.cal_input.text()) and len(self.cal_input.text())==8:
                cmd = "W" + self.cal_input.text()
                self.arduino.write(cmd.encode())
                self.pause.clear()
                text_browser_msg = "Set calibration to: " + self.arduino.readline().decode()
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


    #stop button
    def stop(self):
        self.pause.set()
        self.set_cal_button.setText("Set calibration")
        self.set_cal_button.clicked.disconnect(self.stop)
        self.set_cal_button.clicked.connect(self.setCalibration)

    #work house thread
    def rtRead(self,pause,RT_Plot_Right,RT_Plot_Left):
        N_data = 1
        output = [[0]*N_data*self.N_sample]
        file_data_right = queue.Queue(maxsize=0)
        file_data_left = queue.Queue(maxsize=1000)
        plot_data_right = queue.Queue(maxsize=1000)
        plot_data_left = queue.Queue(maxsize=1000)
        time_queue = queue.Queue(maxsize=1000)
        for i in range(1000):
            plot_data_left.put(0)
            plot_data_right.put(0)
            time_queue.put(0)
        
        while True:
            if not self.pause.isSet():

                #time axis 
                current_t = time_queue.get()
                time_queue.put(current_t+N_sample/int(self.phi12.currentText()))
                time_axis = list(time_queue.queue)
                #right data
                temp = self.arduino.read(size = 2*N_data*self.N_sample) # need to discuss on this part how many dat apoints do we wish to push out each time we update the plot, assuming we push out 2 data point a time
                #parse from byte into int
                for i in range(N_data*self.N_sample):
                    output[i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                    file_data_right.put(output)
                #do the avg
                for i in range(N_data):
                    data_point = sum(output(i*self.N_sample,(i+1)*self.N_sample-1))/self.N_sample
                    plot_data_right.get()
                    plot_data_right.put(data_point)
                plot_data_list_right = list(plot_data_right.queue)

                
                #left data
                temp = self.arduino.read(size = 2*self.N_sample)
                #parse from byte into int
                for i in range(N_data*self.N_sample):
                    output[i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                    file_data_left.put(output)
                #do the avg
                for i in range(N_data):
                    data_point = sum(output(i*self.N_sample,(i+1)*self.N_sample-1))/self.N_sample
                    plot_data_left.get()
                    plot_data_left.put(data_point)
                plot_data_list_left = list(plot_data_left.queue)
                
                #plot section
                RT_Plot_Right.canvas.axes.clear()
                RT_Plot_Right.canvas.axes.plot(time_axis,plot_data_list_right)
                RT_Plot_Right.canvas.axes.set_xlabel('Time(s)')
                RT_Plot_Right.canvas.axes.set_ylabel('Output Reading')
                RT_Plot_Right.canvas.axes.set_title('Right Chip Readout')
                RT_Plot_Right.canvas.draw()
                                
                RT_Plot_Left.canvas.axes.clear()
                RT_Plot_Left.canvas.axes.plot(time_axis,plot_data_list_left)
                RT_Plot_Left.canvas.axes.set_xlabel('Time(s)')
                RT_Plot_Left.canvas.axes.set_ylabel('Output Reading')
                RT_Plot_Left.canvas.axes.set_title('Left Chip Readout')
                RT_Plot_Left.canvas.draw()

            if not file_data_right.empty():
                f = open("RT_records_right.csv","w+")
                for i in range(file_data_right.qsize()):
                    f.write("%s\n" %file_data_right.get())
                f.close()
                
            if not file_data_left.empty():
                f = open("RT_records_left.csv","w+")
                for i in range(file_data_left.qsize()):
                    f.write("%s\n" %file_data_left.get())
                f.close()
                
          

    def testScan(self): #plot and write to file right
        try:
            num_repeat = 1
            rep_interval = 0
            num_repeat = int(self.repeat2_input.text())
            rep_interval = int(self.rep_interval_input.text())
            channel_ind = str(self.channel.currentIndex())
            output_left = [[None]*128*self.N_sample for _ in range(num_repeat)]
            output_right = [[None]*128*self.N_sample for _ in range(num_repeat)]
            self.arduino.reset_input_buffer()
            for j in range(num_repeat):
                self.arduino.reset_input_buffer()
                cmd = "C"+channel_ind # change of plan take note "C0" for left, "C1" for right , for both send "C0"+"C1"
                self.arduino.write(cmd.encode())
                
                while not self.arduino.in_waiting:
                    pass
                
                if channel_ind == '0' or channel_ind == '2':
                    try:
                        temp = self.arduino.read(size = 128*2*2*self.N_sample) #128 cal points * 2 channels left and right * each data points have 2 bytes * number of samples
                        for i in range(128*self.N_sample):
                            output_left[j][i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                        self.arduino.reset_input_buffer()
                    except SerialTimeoutException as ex:
                        output_left[j][i] = 0
                        
                if channel_ind == '1' or channel_ind == '2':
                    try:
                        temp = self.arduino.read(size = 128*2*2*self.N_sample) #128 cal points * 2 channels left and right * each data points have 2 bytes * number of samples
                        for i in range(128*self.N_sample):
                            output_right[j][i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
                        self.arduino.reset_input_buffer()
                    except SerialTimeoutException as ex:
                        output_right[j][i] = 0

                        
                time.sleep(rep_interval)
            text_browser_msg = "scan complete"
            self.cmd_line_output.append(text_browser_msg)


            #No averaging
            #plotting section
            result_left = [[None]*128 for _ in range(num_repeat)]
            result_right = [[None]*128 for _ in range(num_repeat)]
            #for j in range(num_repeat):
            #    for i in range(128):
            #        result_left[j][i] = sum(output_left[j][i*self.N_sample:i*self.N_sample+self.N_sample])/self.N_sample
            #for j in range(num_repeat):
            #    for i in range(128):
            #        result_right[j][i] = sum(output_right[j][i*self.N_sample:i*self.N_sample+self.N_sample])/self.N_sample
            for i in range(num_repeat):
                self.Scan_Plot_Left.canvas.axes.plot(result_left[i])
            for i in range(num_repeat):
                self.Scan_Plot_Right.canvas.axes.plot(result_right[i])
            self.Scan_Plot_Left.canvas.draw()
            self.Scan_Plot_Right.canvas.draw()

            # write to the files
            f = open("test_records_left.csv","w+")
            for item in output_left:
                f.write("%s\n" % item)
            f.close()
            #f = open("test_result_left.csv","w+")
            #for item in result_left:
            #    f.write("%s\n" % item)
            #f.close()
            f = open("test_records_right.csv","w+")
            for item in output_right:
                f.write("%s\n" % item)
            f.close()
            #f = open("test_result_right.csv","w+")
            #for item in result_right:
            #    f.write("%s\n" % item)
            #f.close()
            

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            text_browser_msg = template.format(type(ex).__name__, ex.args)
            self.cmd_line_output.append(text_browser_msg)

    def cleanUp():
        print("thread terminated on exit\n")
        if self.arduino != None:
            self.arduino.close()
            print("port closed on exit\n")
        
    def __init__(self):
        super(CBCM_MainWindow,self).__init__()
        uic.loadUi('GUI.ui',self)

        # draw graph window
        self.RT_Plot_Right.canvas.axes.set_xlabel('Time(s)')
        self.RT_Plot_Right.canvas.axes.set_ylabel('Output Reading')
        self.RT_Plot_Right.canvas.axes.set_title('Right Chip Readout')

        self.RT_Plot_Left.canvas.axes.set_xlabel('Time(s)')
        self.RT_Plot_Left.canvas.axes.set_ylabel('Output Reading')
        self.RT_Plot_Left.canvas.axes.set_title('Left Chip Readout')        
        
        self.Scan_Plot_Left.canvas.axes.set_xlabel('Calibration input')
        self.Scan_Plot_Left.canvas.axes.set_ylabel('Output Scan')
        self.Scan_Plot_Left.canvas.axes.set_title('Left Chip Scan')
        
        self.Scan_Plot_Right.canvas.axes.set_xlabel('Calibration input')
        self.Scan_Plot_Right.canvas.axes.set_ylabel('Output Scan')
        self.Scan_Plot_Right.canvas.axes.set_title('Right Chip Scan')

        #frequency parameter combo box
        self.phi12.addItem("66667")
        self.phi3.addItem("1000000")

        #scan channel combo box
        self.channel.addItem("left")
        self.channel.addItem("right")
        self.channel.addItem("both")

        #setup button behavior
        self.open_port_button.clicked.connect(self.openPort)# connect open port button handler
        self.set_param_button.clicked.connect(self.setParameter)# connect set parameter button handler
        self.set_cal_button.clicked.connect(self.setCalibration)# connect set calibration button handler
        self.scans.clicked.connect(self.testScan)# connect chemical_bio_test button handler

        self.arduino = None
        self.N_sample = 1000

        
        # create realtime reading thread but not starting it till button was clicked
        self.pause = threading.Event()
        self.pause.set()
        self.rt_read = threading.Thread(name='rt_read', target=self.rtRead, args=(self.pause,self.RT_Plot_Right,self.RT_Plot_Left))
        self.rt_read.start()      
            
        
        
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
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CBCM_MainWindow()
    MainWindow.tabWidget.setCurrentIndex(0)
    app.aboutToQuit.connect(MainWindow.cleanUp)
    MainWindow.show()
    sys.exit(app.exec_())


