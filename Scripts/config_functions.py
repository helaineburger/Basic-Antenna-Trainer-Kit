####################
## Import Modules ##
####################

import mysql.connector
import math
import subprocess as sp
import numpy as np
import pickle
from threading import Thread
import sys
import psutil
import dec

###########################
## MySQL Database Config ##
###########################

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = dec.cred()
db_database = 'signaldata'

###################
## Function List ##
###################

def subprocess_launcher(file, arg_list): # launch subprocess
    try:
        process = sp.Popen(['python', file] + arg_list)
    except:
        print('Failed to launch script!')

def servo_theta_phi_get(): # get servo axis data
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1" # get current axis data from database
        db_cursor.execute(query)
        result = db_cursor.fetchone();

        theta = result[0]
        phi = result[1]

        db.commit()
        db_cursor.close()
        db.close()

        
        print('Data retrieved.')
        return (theta, phi)
    
    except:
        print('Error retrieving servo axis data!')

def servo_theta_phi_send(theta, phi): # send servo axis data
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        try:
            query = 'CREATE TABLE cur_ax(theta_val INT(255), phi_val INT(255), id INT PRIMARY KEY AUTO_INCREMENT)' # create servo axis table in database
            db_cursor.execute(query)

        except:
            pass
                
            val = (theta, phi)
            send_data = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload theta and phi servo axis values to database
            db_cursor.execute(send_data, val)
            db.commit()
            db_cursor.close()
            db.close()
            print('Data sent.')
            
    except:
        location = 'error_prompt.pyw'
        img_name = 'Images/e_sending_servo.png'
        alert = 'Error sending servo axis data!'
        arg_list = [img_name, alert, theta, phi]
        Thread(target=subprocess_launcher, args=[location, arg_list]).start() # launch error gui

def servo_theta_phi_incr(direction): # increment/decrement/reset servo axis data
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()
        
        if direction == 'up':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1" # get current axis data from database
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                theta = result[0]
                phi = result[1]
                db.commit()
                
                phi = phi + 5 # increment phi data by 5 degrees
                if phi > 180:
                    phi = 180
                    
                else:
                    pass

                val = (theta, phi)
                query = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload axis data input into database
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'down':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1" # get current axis data from database
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                theta = result[0]
                phi = result[1]
                db.commit()
                
                phi = phi - 5 # decrement phi value by 5 degrees
                if phi < 0:
                    phi = 0
                    
                else:
                    pass

                val = (theta, phi)
                query = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload axis data input into database
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'left':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1" # get current axis data from database
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                theta = result[0]
                phi = result[1]
                db.commit()
                
                theta = theta - 5 # decrement theta value by 5 degrees
                if theta < 0:
                    theta = 0
                    
                else:
                    pass

                val = (theta, phi)
                query = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload axis data input into database
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'right':
            try:
                query = "SELECT * FROM cur_ax ORDER BY id DESC LIMIT 1" # get current axis data from database
                db_cursor.execute(query)
                result = db_cursor.fetchone();
                theta = result[0]
                phi = result[1]
                db.commit()
                
                theta = theta + 5 # increment theta value by 5 degrees
                if theta > 180:
                    theta = 180
                    
                else:
                    pass

                val = (theta, phi)
                query = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload axis data input into database
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

        elif direction == 'rst':
            try:
                theta = 90 # reset theta value to default (90 degrees)
                phi = 90 # reset phi value to default (90 degrees)
                val = (theta, phi)
                query = "INSERT INTO cur_ax(theta_val, phi_val) VALUES (%s, %s)" # upload axis data input into database
                db_cursor.execute(query, val)
                db.commit()
                
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                pass

    except:
        location = 'error_prompt.pyw'
        img_name = 'Images/e_sending_servo.png'
        alert = 'Error sending servo axis data!'
        arg_list = [img_name, alert, theta, phi]
        Thread(target=subprocess_launcher, args=[location, arg_list]).start() # launch error gui
        
def signal_param_send(cf, fs): # send signal parameters to database
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
        db_cursor = db.cursor()

        try:
            query = 'CREATE TABLE signal_param(cent_freq BIGINT(255), samp_rate BIGINT(255), id INT PRIMARY KEY AUTO_INCREMENT)' # create signal paramaters database table
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
                cf = cf.replace('khz', '') # convert khz format to float
                cf = float(cf) * 1e3
                cf = math.ceil(cf)
                print(cf, 'khz')

            elif 'mhz' in cf:
                cf = cf.replace('mhz', '') # convert mhz format to float
                cf = float(cf) * 1e6
                cf = math.ceil(cf)
                print(cf, 'mhz')

            elif 'ghz' in cf:
                cf = cf.replace('ghz', '') # convert ghz format to float
                cf = float(cf) * 1e9
                cf = math.ceil(cf)
                print(cf, 'ghz')
                
            else:
                print('Invalid center frequency input!')
                cf = ''
                pass

        try:
            fs = float(fs)
            fs = math.ceil(fs)
            print(fs, 'flt')
            
        except:
            if 'khz' in fs:
                fs = fs.replace('khz', '') # convert khz format to float
                fs = float(fs) * 1e3
                fs = math.ceil(fs)
                print(fs, 'khz')

            elif 'mhz' in fs:
                fs = fs.replace('mhz', '') # convert mhz format to float
                fs = float(fs) * 1e6
                fs = math.ceil(fs)
                print(fs, 'mhz')

            elif 'ghz' in fs:
                fs = fs.replace('ghz', '') # convert ghz format to float
                fs = float(fs) * 1e9
                fs = math.ceil(fs)
                print(fs, 'ghz')
                
            else:
                print('Invalid sample rate input!')
                fs = ''
                
        if (cf == '') or (fs == ''):
            print('Invalid input!')

        elif (cf < 24e6):
            print('Center frequency is below designated limit! (Limit = 24 MHz)')
            
        elif (fs <= 900e3):
            print('Samping rate is below designated limit! (Limit > 900 KHz)')

        elif (fs >= 3.2e6):
            print('Sampling rate is above designated limit! (Limit < 3.2 MHz)')
            
        elif (cf > 1.7e9):
            print('Center frequency is above designated limit! (Limit = 1.7 GHz')

        else:
            try:
                val = (cf, fs)
                send_data = "INSERT INTO signal_param(cent_freq, samp_rate) VALUES (%s, %s)" # send ceneter frequency and sample rate data into database
                db_cursor.execute(send_data, val)
                db.commit()
                db_cursor.close()
                db.close()
                print('Data sent.')

            except:
                print('An error has occured!')
        
    except:
        print('Sending failed!')

def get_sig_data(): # get signal data from database
    try:
        db = mysql.connector.connect(host = db_host, port = db_port,
                                     user = db_user, passwd = db_pass,
                                     database = db_database)
        db_cursor = db.cursor()

        query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1" # get signal data from database
        db_cursor.execute(query)
        result = db_cursor.fetchone();
        db.commit()
        db_cursor.close()
        db.close()
        
        x = pickle.loads(result[0])
        y = pickle.loads(result[1])

        return (x, y)

    except:
        print('Error retrieving signal data!')

def calc_offset(off_y, on_y, on_x, cent_freq): # calculate center frequency offset
    print('Calibrating...')
    
    delta = np.subtract(on_y, off_y) # delta between max y with transmitter on and max y value with transmitter off
    if len(delta) == len(on_x):
        max_on = np.max(on_y) # get max y value with transmitter on
        max_on_index = np.where(on_y == max_on) # get max y value index with transmitter on
        
        max_val = np.max(delta) # get max y value from delta
        max_val_index = np.where(delta == max_val) # get mx y value index from delta

        if (len(max_val_index) == 1) and (len(max_on_index) == 1):
            if max_val_index == max_on_index:
                uncalib_freq = on_x[max_val_index[0][0]]
                offset = ((cent_freq / 1e6) - uncalib_freq) * -1e6
                print("Offset: ", offset)
                
                retry = input('Retry (y/n): ')
                if (retry == 'y') or (retry == 'Y'):
                    return ('retry')
                
                elif (retry == 'n') or (retry == 'N'):
                    return offset

                else:
                    print('Invalid input, retrying.')
                    return ('retry')

            else:
                return ('retry')

        else:
            return('retry')
            
    else:
        return ('retry')

def calibrate(offset, signal, samp_rate):  # calibrate center frequency using offset data
    shift_correction = np.exp(-1.0j * 2.0 * np.pi * offset / samp_rate * np.arange(len(signal)))
    x = signal * shift_correction

    return x

def send_offset(offset): # send offset value to database
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        try:
            query = 'CREATE TABLE offset(offset FLOAT, id INT PRIMARY KEY AUTO_INCREMENT)' # create offset table in database
            db_cursor.execute(query)
            db.commit()
            
        except:
            pass

        val = [offset]
        query = "INSERT INTO offset(offset) VALUES (%s)" # upload offset data to database
        db_cursor.execute(query, val)
        db.commit()
        db_cursor.close()
        db.close()
        print('Offset data sent.')

    except:
        print('Error sending offset data!')

def get_offset(): # get offset data from database
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = "SELECT * FROM offset ORDER BY id DESC LIMIT 1" # get offset data from database
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

def check_pid_status(pid): # check process id status
    status = psutil.pid_exists(pid)
    return status

def get_pid(filename): # read process id
    file = open(filename, 'a+')
    file.seek(0)
    pid = int(file.readlines()[0])
    return pid

def send_annc(text): # upload annoucement value to database
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = 'CREATE TABLE announcement(text VARCHAR(3000), id INT PRIMARY KEY AUTO_INCREMENT)' # create announcement table in database
        db_cursor.execute(query)
        db.commit()
        
    except:
        pass

    val = [text]
    query = "INSERT INTO announcement(text) VALUES (%s)" # upload announcement value to database
    db_cursor.execute(query, val)
    db.commit()
    db_cursor.close()
    db.close()
    print('Annoucement data sent.')

def get_annc(): # get announcement data from database
    db = mysql.connector.connect(host = db_host, port = db_port,
                                 user = db_user, passwd = db_pass,
                                 database = db_database)
    db_cursor = db.cursor()

    try:
        query = "SELECT * FROM announcement ORDER BY id DESC LIMIT 1" # get announcement value from database
        db_cursor.execute(query)
        result = db_cursor.fetchone();
        db.commit()
        db_cursor.close()
        db.close()

        return result[0]
        
    except:
        result=''
        return result
