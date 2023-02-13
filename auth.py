from cryptography.fernet import Fernet
import mysql.connector
import sys

try:
    pid_log = cf.get_pid('Scripts/process/auth_pid')
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!') # Error prompt
    os.kill(pid_log, signal.SIGTERM)
    pid = os.getpid()
    log_id = open('Scripts/process/auth_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/auth_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

db_host = 'db-mysql-sgp1-91308-do-user-11790312-0.b.db.ondigitalocean.com'
db_port = '25060'
db_user = 'client'
db_pass = # Insert database password
db_database = 'signaldata'

db = mysql.connector.connect(host = db_host, port = db_port,
                             user = db_user, passwd = db_pass,
                             database = db_database)
db_cursor = db.cursor()

'''
drop_table = 'DROP TABLE enc'
db_cursor.execute(drop_table)'''

try:
    create_table = 'CREATE TABLE enc(enc_pword BINARY(120), enc_key VARBINARY(44), id int PRIMARY KEY AUTO_INCREMENT)'
    db_cursor.execute(create_table)
    db.commit()

except:
    print('Error creating table!')
    pass

query = "SELECT * FROM enc ORDER BY id DESC LIMIT 1"
db_cursor.execute(query)
result = db_cursor.fetchone();

enc_pword = bytes(result[0])
key = bytes(result[1])
fernet = Fernet(key)
pword = fernet.decrypt(enc_pword).decode()

cred = open('cred', 'w+')
cred.write(str(key)[2:(len(key)+2)] + '\n' + str(enc_pword)[2:(len(enc_pword)+2)])
cred.close()

cred = open('Scripts/cred', 'w+')
cred.write(str(key)[2:(len(key)+2)] + '\n' + str(enc_pword)[2:(len(enc_pword)+2)])
cred.close()

sys.exit()

