# GET RTL-SDR DATA

import matplotlib.pyplot as plt
import numpy as np
import pickle
from rtlsdr import *
import time
import mysql.connector

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = 'AVNS_KtBYvuN3xrywbxjVmBz'
db_database = 'signaldata'

db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
db_cursor = db.cursor()

'''
drop_table = 'DROP TABLE iq_signal_data'
db_cursor.execute(drop_table)'''

try:
    create_table = 'CREATE TABLE iq_signal_data(x_data BLOB, y_data BLOB, data_id int PRIMARY KEY AUTO_INCREMENT)'
    db_cursor.execute(create_table)
    
except:
    pass

sdr = RtlSdr()

samp_rate = 2.4e6
cent_freq = 440e6
gain = 4

def get_data(sample_rate, cent_freq, gain):
    
    sdr.sample_rate = samp_rate
    sdr.center_freq = cent_freq
    sdr.gain = gain

    try:
        samples = sdr.read_samples(256*1024)
        fig, (ax) = plt.subplots(1,1)
        ax.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6, data=samples)
        line = ax.lines[0]
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        np.save('x_data', x_data, allow_pickle=True, fix_imports=True)
        np.save('y_data', y_data, allow_pickle=True, fix_imports=True)
        print('Data gathered.')
        plt.close() # Do not remove to prevent memory leak!!!
        #time.sleep(3)
        
    except:
        pass

def send_data():
    x = np.load('x_data.npy', allow_pickle=True)
    y = np.load('y_data.npy', allow_pickle=True)
            
    p_x_data = pickle.dumps(x)
    p_y_data = pickle.dumps(y)
    #time.sleep(1)

    t = pickle.loads(p_y_data)

    try:
        val = (p_x_data, p_y_data)
        send_data_db = "INSERT INTO iq_signal_data (x_data, y_data) VALUES (%s, %s)"
        db_cursor.execute(send_data_db, val)
        db.commit()
        print('Data sent.')
        
    except:
        print("Error updating.")

    
try:
    while True:
        get_data(samp_rate, cent_freq, gain)
        send_data()
        
except:
    print('Invalid frequency configuration.')

