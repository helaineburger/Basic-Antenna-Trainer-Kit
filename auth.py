####################
## Import Modules ##
####################

from cryptography.fernet import Fernet
import mysql.connector
import sys

###########################
## Check Running Process ##
###########################

try:
    pid_log = cf.get_pid('Scripts/process/auth_pid') # read process id
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/auth_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/auth_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()
    
###########################
## MySQL Database Config ##
###########################

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

############################################################
## Get Enryption Key And Encrypted Password From Database ##
############################################################

try:
    create_table = 'CREATE TABLE enc(enc_pword BINARY(120), enc_key VARBINARY(44), id int PRIMARY KEY AUTO_INCREMENT)' # create mysql table
    db_cursor.execute(create_table)
    db.commit()

except:
    print('Error creating table!')
    pass

query = "SELECT * FROM enc ORDER BY id DESC LIMIT 1" # get enryption key and encrypted database password from database
db_cursor.execute(query)
result = db_cursor.fetchone();

enc_pword = bytes(result[0]) # encryption key
key = bytes(result[1]) # encrypted password
fernet = Fernet(key)
#pword = fernet.decrypt(enc_pword).decode() # decrypted password

cred = open('cred', 'w+')
cred.write(str(key)[2:(len(key)+2)] + '\n' + str(enc_pword)[2:(len(enc_pword)+2)]) # write encryption key and encrypted password to cred file in main directory
cred.close()

cred = open('Scripts/cred', 'w+')
cred.write(str(key)[2:(len(key)+2)] + '\n' + str(enc_pword)[2:(len(enc_pword)+2)]) # write encryption key and encrypted password to cred file in Scripts directory
cred.close()

sys.exit() # terminate script

