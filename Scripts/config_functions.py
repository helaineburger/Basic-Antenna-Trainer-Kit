import mysql.connector
import math
import subprocess as sp
import numpy as np
import pickle
from threading import Thread
import sys
import psutil

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = 'AVNS_KtBYvuN3xrywbxjVmBz'
db_database = 'signaldata'

def subprocess_launcher(file, arg_list):
    try:
        process = sp.Popen(['python', file] + arg_list, creationflags = sp.CREATE_NEW_CONSOLE, shell=True)
    except:
        print('Failed to launch script!')

def servo_x_y_get():
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1"
        db_cursor.execute(query)
        result = db_cursor.fetchone();

        x = result[0]
        y = result[1]

        db.commit()
        db_cursor.close()
        db.close()

        
        print('Data retrieved.')
        return (x, y)
    
    except:
        print('Error retrieving servo axis data!')

def servo_x_y_send(x, y):
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        try:
            query = 'CREATE TABLE cur_ax(x_val INT(255), y_val INT(255), id INT PRIMARY KEY AUTO_INCREMENT)'
            db_cursor.execute(query)

        except:
            pass
                
            val = (x, y)
            send_data = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
            db_cursor.execute(send_data, val)
            db.commit()
            db_cursor.close()
            db.close()
            print('Data sent.')
            
    except:
        location = 'error_prompt.pyw'
        img_name = 'Images/e_sending_servo.png'
        alert = 'Error sending servo axis data!'
        arg_list = [img_name, alert, x, y]
        Thread(target=subprocess_launcher, args=[location, arg_list]).start()

def servo_x_y_incr(direction):
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()
        
        if direction == 'up':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1"
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                x = result[0]
                y = result[1]
                db.commit()
                
                y = y + 5
                if y > 180:
                    y = 180
                    
                else:
                    pass

                val = (x, y)
                query = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'down':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1"
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                x = result[0]
                y = result[1]
                db.commit()
                
                y = y - 5
                if y < 0:
                    y = 0
                    
                else:
                    pass

                val = (x, y)
                query = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'left':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1"
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                x = result[0]
                y = result[1]
                db.commit()
                
                x = x - 5
                if x < 0:
                    x = 0
                    
                else:
                    pass

                val = (x, y)
                query = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'right':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1"
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                x = result[0]
                y = result[1]
                db.commit()
                
                x = x + 5
                if x > 180:
                    x = 180
                    
                else:
                    pass

                val = (x, y)
                query = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'rst':
            try:
                x = 90
                y = 90
                val = (x, y)
                query = "INSERT INTO cur_ax(x_val, y_val) VALUES (%s, %s)"
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

    except:
        location = 'error_prompt.py'
        img_name = 'Images/e_sending_servo.png'
        alert = 'Error sending servo axis data!'
        arg_list = [img_name, alert, x, y]
        Thread(target=subprocess_launcher, args=[location, arg_list]).start()
        
def signal_param_send(cf, fs):
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        try:
            query = 'CREATE TABLE signal_param(cent_freq BIGINT(255), samp_rate BIGINT(255), id INT PRIMARY KEY AUTO_INCREMENT)'
            db_cursor.execute(query)

        except:
            pass

        cf = cf.lower().replace(' ', '')
        fs = fs.lower().replace(' ', '')

        try:
            cf = float(cf)
            cf = math.ceil(cf)
            print(cf, 'flt')
            
        except:
            if 'khz' in cf:
                cf = cf.replace('khz', '')
                cf = float(cf) * 1e3
                cf = math.ceil(cf)
                print(cf, 'khz')

            elif 'mhz' in cf:
                cf = cf.replace('mhz', '')
                cf = float(cf) * 1e6
                cf = math.ceil(cf)
                print(cf, 'mhz')

            elif 'ghz' in cf:
                cf = cf.replace('ghz', '')
                cf = float(cf) * 1e9
                cf = math.ceil(cf)
                print(cf, 'ghz')
                
            else:
                print('Invalid center frequency input!') # Error popup
                cf = ''
                pass

        try:
            fs = float(fs)
            fs = math.ceil(fs)
            print(fs, 'flt')
            
        except:
            if 'khz' in fs:
                fs = fs.replace('khz', '')
                fs = float(fs) * 1e3
                fs = math.ceil(fs)
                print(fs, 'khz')

            elif 'mhz' in fs:
                fs = fs.replace('mhz', '')
                fs = float(fs) * 1e6
                fs = math.ceil(fs)
                print(fs, 'mhz')

            elif 'ghz' in fs:
                fs = fs.replace('ghz', '')
                fs = float(fs) * 1e9
                fs = math.ceil(fs)
                print(fs, 'ghz')
                
            else:
                print('Invalid sample rate input!') # Error popup
                fs = ''
                
        if (cf == '') or (fs == ''):
            print('Invalid input!') # Error popup

        elif (cf < 24e6):
            print('Center frequency is below designated limit! (Limit = 24 MHz)') # Error popup
            
        elif (fs <= 900e3):
            print('Samping rate is below designated limit! (Limit > 900 KHz)') # Error popup

        elif (fs >= 3.2e6):
            print('Sampling rate is above designated limit! (Limit < 3.2 MHz)') # Error popup
            
        elif (cf > 1.7e9):
            print('Center frequency is above designated limit! (Limit = 1.7 GHz') # Error popup

        else:
            try:
                val = (cf, fs)
                send_data = "INSERT INTO signal_param(cent_freq, samp_rate) VALUES (%s, %s)"
                db_cursor.execute(send_data, val)
                db.commit()
                db_cursor.close() # SEEEEEEE MEEEE NEWLY ADDED TEST MEEE!!!!
                db.close()
                print('Data sent.')

            except:
                print('An error has occured!') # Error popup
        
    except:
        print('Sending failed!') # Error popup

def get_sig_data():
##    try:
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1"
    db_cursor.execute(query)
    result = db_cursor.fetchone();
    db.commit()
    db_cursor.close()
    db.close()
    
    x = pickle.loads(result[0])
    y = pickle.loads(result[1])

    return (x, y)
    
##    except:
##        print('Error recieving signal data!')
##        pass

def calc_offset(off_y, on_y, on_x, cent_freq):
    delta = np.subtract(off_y, on_y)
    max_val = np.max(delta)
    max_val_index = np.where(delta == max_val)
    uncalib_freq = on_x[max_val_index[0]]
    offset = ((cent_freq / 1e6) - uncalib_freq) * 1e6
    print(offset)

    return offset

def calibrate(offset, signal, samp_rate):   
    shift_correction = np.exp(-1.0j * 2.0 * np.pi * offset / samp_rate * np.arange(len(signal)))
    x = signal * shift_correction

    return x

#def sig_strength():

def send_offset(offset):
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        try:
            query = 'CREATE TABLE offset(offset FLOAT, id INT PRIMARY KEY AUTO_INCREMENT)'
            db_cursor.execute(query)
            db.commit()
            
        except:
            pass

        val = [offset]
        query = "INSERT INTO offset(offset) VALUES (%s)"
        db_cursor.execute(query, val)
        db.commit()
        db_cursor.close()
        db.close()
        print('Offset data sent.')

    except:
        print('Error sending offset data!')

def get_offset():
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = "SELECT * FROM offset ORDER BY id DESC LIMIT 1"
        db_cursor.execute(query)
        result = db_cursor.fetchone();
        db.commit()
        db_cursor.close()
        db.close()

        return result[0]

    except:
        result = 'No data!'
        return result
        print('Error recieving offset data!')

def check_pid_status(pid):
    status = psutil.pid_exists(pid)
    return status

def get_pid(filename):
    file = open(filename, 'a+')
    file.seek(0)
    pid = int(file.readlines()[0])
    return pid

def send_annc(text):
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = 'CREATE TABLE announcement(text VARCHAR(3000), id INT PRIMARY KEY AUTO_INCREMENT)'
        db_cursor.execute(query)
        db.commit()
        
    except:
        pass

    val = [text]
    query = "INSERT INTO announcement(text) VALUES (%s)"
    db_cursor.execute(query, val)
    db.commit()
    db_cursor.close()
    db.close()
    print('Annoucement data sent.')

def get_annc():
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = "SELECT * FROM announcement ORDER BY id DESC LIMIT 1"
        db_cursor.execute(query)
        result = db_cursor.fetchone();
        db.commit()
        db_cursor.close()
        db.close()

        return result[0]
        
    except:
        result=''
        return result
