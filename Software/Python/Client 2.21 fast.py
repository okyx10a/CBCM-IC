import serial
import time
import sys
import struct
import matplotlib.pyplot as plt
N_sample = 1000  

arduino = serial.Serial('COM6',baudrate = 115200, timeout=1)
print("port opened on " + arduino.name+"\n")

while 1:
    arduino.reset_input_buffer()
    arduino.reset_output_buffer()
    calseq = input("1) \"W#######\" for input calibration sequence\n2) \"G###\" for changing CCO resolution\n3) \"complete test\" for a reading all output for each input ranging from 0-127\n4) \"S###\"to change the number of samples for each calibration input\n5) \"quit\" to quit program. \nPlease input your command:")
    if calseq == "quit":
        arduino.close()
        sys.exit()
        
    elif calseq == "complete test":
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
    elif calseq[0] == "G" :
        arduino.write(calseq[1:4].encode())
        
    elif calseq[0] == "W" :
        arduino.write(calseq.encode())
        output = [0]*N_sample
        for i in range(N_sample):
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
    elif calseq[0] == "S":
        arduino.write(calseq.encode())
        #arduino.write('t'.encode())
        
        N_sample = int(calseq[1:])
        print(N_sample)
        #print(arduino.readline().decode())
        #print("done\n")
        print("The number of samples for each calibration input is: ")
        print(arduino.readline().decode())
    
    
