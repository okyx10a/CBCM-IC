import os, time
import threading, Queue


class RtRead(threading.Thread):

    
    def __init__(self, result_q, arduino, N_sample):
        super(WorkerThread, self).__init__()
        self.result_q = result_q
        self.arduino = arduino
        self.N_sample = N_sample
        self.pauserequest = threading.Event()
        self.stoprequest = threading.Event()

    def run(self):
        #send cal_sequence
        #request read
        #
        #
        output = [0]*self.N_sample
        while not self.stoprequest.isSet():
            self.arduino.write(cmd.encode())
            while not self.arduino.in_waiting:
                pass                 
            temp = self.arduino.read(size = 2*self.N_sample)
            for i in range(self.N_sample):
                output = int.from_bytes( temp[2*i:2*i+2], byteorder='big')
            self.arduino.reset_input_buffer()
            #output put into result_q
        
    def join(self, timeout=None):
        self.stoprequest.set()
        super(RtRead, self).join(timeout)
        
