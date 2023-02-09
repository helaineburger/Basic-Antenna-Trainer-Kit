import mysql.connector
import pickle
import Scripts.config_functions as cf
import os
import signal

try:
    pid_log = cf.get_pid('Scripts/process/calc_offset_pid')
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM)
    pid = os.getpid()
    log_id = open('Scripts/process/calc_offset_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/calc_offset_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = 'AVNS_KtBYvuN3xrywbxjVmBz'
db_database = 'signaldata'

db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
db_cursor = db.cursor()

trans_off = input('Turn transmitter off. Enter any key to continue: ')

query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1"
db_cursor.execute(query)
result = db_cursor.fetchone();
db.commit()

x_off = pickle.loads(result[0])
y_off = pickle.loads(result[1])


trans_on = input('Turn transmitter on. Enter any key to continue: ')

query = "SELECT * FROM iq_signal_data ORDER BY data_id DESC LIMIT 1"
db_cursor.execute(query)
result = db_cursor.fetchone();
db.commit()

x_on = pickle.loads(result[0])
y_on = pickle.loads(result[1])


query = "SELECT * FROM signal_param ORDER BY id DESC LIMIT 1"
db_cursor.execute(query)
result = db_cursor.fetchone();
db.commit()

cent_freq = result[0]

offset = cf.calc_offset(y_off, y_on, x_on, cent_freq)
print(offset[0])

cf.send_offset(offset[0])

db_cursor.close()
db.close()
