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
