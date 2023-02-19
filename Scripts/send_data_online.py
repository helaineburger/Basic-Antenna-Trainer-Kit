#####################
## Import Database ##
#####################

import matplotlib.pyplot as plt
import numpy as np
import pickle
from rtlsdr import *
import mysql.connector
import config_functions as cf
import os
import signal
from threading import Thread
from time import sleep
import sys
import ast
import dec

###########################
## Check Running Process ##
###########################

try:
    pid_log = cf.get_pid('Scripts/process/send_data_online_pid') # read process id
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/send_data_online_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/send_data_online_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()
    
###########################
## MySQL Database Config ##
###########################


db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = dec.cred()
db_database = 'signaldata'

db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
db_cursor = db.cursor()

'''
drop_table = 'DROP TABLE iq_signal_data'
db_cursor.execute(drop_table)
'''

###################################
## Get Signal Data From Database ##
###################################

try:
    create_table = 'CREATE TABLE iq_signal_data(x_data BLOB, y_data BLOB, data_id int PRIMARY KEY AUTO_INCREMENT)' # create signal data table in database
    db_cursor.execute(create_table)
    
except:
    pass

def get_sig_param():
    try:
        get_sig_param = 'SELECT * FROM signal_param ORDER BY id DESC LIMIT 1' # get signal paramaters data from database
        db_cursor.execute(get_sig_param)
        sig_param = db_cursor.fetchone();
    
    except:
        pass
        
    sig_param_log = open('param', 'w+')
    sig_param_log.write(str(sig_param))
    sig_param_log.close()

print('Initializing...')
get_sig_param()

###################################
## Send RTL-SDR Data To Database ##
###################################

try:
    sdr = RtlSdr() # load rtl sdr
    gain = 4

    def get_data():
        sig_param_read = open('param', 'a+') # read rtl-sdr parameters from param file
        sig_param_read.seek(0)
        sig_param_data = sig_param_read.readlines()[0]

        sig_param = ast.literal_eval(sig_param_data)
        offset = cf.get_offset()
        sdr.sample_rate = sig_param[1] # sample rate
        sdr.center_freq = sig_param[0] # center frequency
        sdr.gain = gain # signal gain

        try:
            samples = sdr.read_samples(256*1024)

            # Offset Correction
            offset = cf.get_offset() # get offset
            samples = cf.calibrate(offset, samples, sig_param[1]) # calibrate samples
            
            fig, (ax) = plt.subplots(1,1)
            ax.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, data=samples) # plot iq signal
            line = ax.lines[0]
            x_data = line.get_xdata() # get x array values from plot
            y_data = line.get_ydata() # get y array values from plot
            np.save('x_data', x_data, allow_pickle=True, fix_imports=True) # write x array values to file
            np.save('y_data', y_data, allow_pickle=True, fix_imports=True) # write y array values to file
            print('Data gathered.')
            plt.close() # Do not remove to prevent memory leak!!!
        
        except:
            print('error correcting samples')
            pass

    def send_data():
        x = np.load('x_data.npy', allow_pickle=True) # read x array values
        y = np.load('y_data.npy', allow_pickle=True) # read y array values
                
        p_x_data = pickle.dumps(x)
        p_y_data = pickle.dumps(y)

        try:
            val = (p_x_data, p_y_data)
            send_data_db = "INSERT INTO iq_signal_data (x_data, y_data) VALUES (%s, %s)" # send x and y array values to database
            db_cursor.execute(send_data_db, val)
            db.commit()
            print('Data sent.')
            
        except:
            print("Error updating.")

        
    try:
        while True:
            Thread(target=get_sig_param, args=[]).start()
            get_data()
            send_data()
            
    except:
        pass

except:
    print('RTL-SDR not detected! Re-insert and try again.')
    sleep(3)
    sys.exit() # terminate script
    
