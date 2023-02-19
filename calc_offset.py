####################
## Import Modules ##
####################

import mysql.connector
import pickle
import Scripts.config_functions as cf
import os
import signal
import Scripts.dec as dec

###########################
## Check Running Process ##
###########################

try:
    pid_log = cf.get_pid('Scripts/process/calc_offset_pid') # read process id
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/calc_offset_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/calc_offset_pid', 'w+')
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

#################################
## Get Center Frequency Offset ##
#################################

trans_off = input('Turn transmitter off. Enter any key to continue: ') # user input

query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1" # get frequency spectrum x and y array values from database
db_cursor.execute(query)
result = db_cursor.fetchone();
db.commit()

x_off = pickle.loads(result[0]) # x array values when transmitter is off
y_off = pickle.loads(result[1]) # y array values when transmitter is off


trans_on = input('Turn transmitter on. Enter any key to continue: ') # user input
    
while True:
    query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1" # get frequency spectrum x and y array values from database
    db_cursor.execute(query)
    result = db_cursor.fetchone();
    db.commit()

    x_on = pickle.loads(result[0]) # x array values when transmitter is on
    y_on = pickle.loads(result[1]) # y array values when transmitter is on


    query = "SELECT * FROM signal_param ORDER BY id DESC LIMIT 1" # get signal parameters from database
    db_cursor.execute(query)
    result = db_cursor.fetchone();
    db.commit()

    cent_freq = result[0] # center frequency

    offset = cf.calc_offset(y_off, y_on, x_on, cent_freq) # calculate offset
    print(offset)
    
    if offset == 'retry':
        print('Retrying...')
        pass

    else:
        cf.send_offset(offset)
        break

db_cursor.close()
db.close()
