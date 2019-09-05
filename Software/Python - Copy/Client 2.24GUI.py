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
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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

    #actually its set input sequence (older version didn't include the sensing and calibration mode bit)
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
                self.cont_readout_thread = threading.Thread(target = self.data_plot)
                self.cont_readout_thread.start()
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
        self.cont_readout_thread.join()
        self.set_cal_button.setText("Set calibration")
        self.set_cal_button.clicked.disconnect(self.stop)
        self.set_cal_button.clicked.connect(self.setCalibration)
        

    #start a new thread for continuous read out
    def data_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        start_time = time.time()
        plot_data = queue.Queue(maxsize=100)
        time_queue = queue.Queue(maxsize=100)
        for i in range(100):
            plot_data.put(0)
            time_queue.put(i-100)
        ani = animation.FuncAnimation(fig, self.cont_readout,interval = 10, fargs = (start_time,ax,plot_data,time_queue))
        
        plt.show()
        

    #function that defines the graph animation
    @staticmethod
    def cont_readout(i,start_time,ax,plot_data,time_queue):
        output = [0]*N_sample
        cmd = "R"
        arduino.write(cmd.encode())
        while not arduino.in_waiting:
            pass                 
        temp = arduino.read(size = 2*N_sample)
        for i in range(N_sample):
            output[i] = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
        arduino.reset_input_buffer()
        plot_data.get()
        plot_data.put(sum(output)/N_sample)
        time_queue.get()
        time_queue.put(time.time()-start_time)
        plot_data_list = list(plot_data.queue)
        time_axis = list(time_queue.queue)
        ax.clear()
        ax.set_ylim(0,5000)
        ax.set_autoscaley_on(False) 
        ax.plot(time_axis,plot_data_list)
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
    MainWindow = CBCM_MainWindow()
    MainWindow.tabWidget.setCurrentIndex(0)
    app.aboutToQuit.connect(cleanUp)
    MainWindow.show()
    sys.exit(app.exec_())


