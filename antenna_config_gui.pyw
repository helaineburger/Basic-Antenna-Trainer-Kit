####################
## Import Modules ##
####################

import tkinter as tk
import Scripts.config_functions as cf
from PIL import Image, ImageTk
from time import sleep
from threading import Thread
import subprocess as sp
import os
import signal
import mysql.connector
import time
import Scripts.dec as dec

###########################
## Check Running Process ##
###########################

try:
    pid_log = cf.get_pid('Scripts/process/antenna_config_gui_pid') # read process id
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/antenna_config_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/antenna_config_gui_pid', 'w+')
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
db_cursor.execute(drop_table)'''

##############################################
## Get Signal Parameters Data from database ##
##############################################

try:
    create_table = 'CREATE TABLE iq_signal_data(theta_data BLOB, phi_data BLOB, data_id int PRIMARY KEY AUTO_INCREMENT)' # create mysql table
    db_cursor.execute(create_table)
    
except:
    pass

try:
    get_sig_param = 'SELECT * FROM signal_param ORDER BY id DESC LIMIT 1'  # get data from database table
    db_cursor.execute(get_sig_param)
    sig_param = db_cursor.fetchone(); # index 0 is center frequency while index 1 is sample rate

    if sig_param[0] >= 1e9:
        cent_freq_val = str(sig_param[0]/1e9) + ' GHz' # convert float to GHz format
        
    elif sig_param[0] >= 1e6:
        cent_freq_val = str(sig_param[0]/1e6) + ' MHz' # convert float to MHz format

    elif sig_param[0] >= 1e3:
        cent_freq_val = str(sig_param[0]/1e3) + ' kHz' # convert float to kHz format

    else:
        cent_freq_val = str(sig_param[0]) + ' Hz' # convert float Hz formmat

    if sig_param[1] >= 1e6: 
        samp_rate_val = str(sig_param[1]/1e6) + ' MHz' # convert float to Mhz format
        
    elif sig_param[1] >= 1e3:
        samp_rate_val = str(sig_param[1]/1e3) + ' kHz' # convert float to kHz format

    else:
        samp_rate_val = str(sig_param[1]) + ' Hz' # convert float to Hz format

except:
    pass

#################
## Load Images ##
#################

# Images
frame_img = Image.open('Images/ant_conf.png')
frame_img_load = ImageTk.PhotoImage(frame_img)

set_1_img_1 = Image.open('Images/set_1_btn_1.png')
set_1_img_1_load = ImageTk.PhotoImage(set_1_img_1)
set_1_img_2 = Image.open('Images/set_1_btn_2.png')
set_1_img_2_load = ImageTk.PhotoImage(set_1_img_2)

set_2_img_1 = Image.open('Images/set_2_btn_1.png')
set_2_img_1_load = ImageTk.PhotoImage(set_2_img_1)
set_2_img_2 = Image.open('Images/set_2_btn_2.png')
set_2_img_2_load = ImageTk.PhotoImage(set_2_img_2)

live_img_1 = Image.open('Images/live_btn_1.png')
live_img_1_load = ImageTk.PhotoImage(live_img_1)
live_img_2 = Image.open('Images/live_btn_2.png')
live_img_2_load = ImageTk.PhotoImage(live_img_2)

snap_img_1 = Image.open('Images/snapshot_btn_1.png')
snap_img_1_load = ImageTk.PhotoImage(snap_img_1)
snap_img_2 = Image.open('Images/snapshot_btn_2.png')
snap_img_2_load = ImageTk.PhotoImage(snap_img_2)

up_img_1 = Image.open('Images/up_btn_1.png')
up_img_1_load = ImageTk.PhotoImage(up_img_1)
up_img_2 = Image.open('Images/up_btn_2.png')
up_img_2_load = ImageTk.PhotoImage(up_img_2)

down_img_1 = Image.open('Images/down_btn_1.png')
down_img_1_load = ImageTk.PhotoImage(down_img_1)
down_img_2 = Image.open('Images/down_btn_2.png')
down_img_2_load = ImageTk.PhotoImage(down_img_2)

left_img_1 = Image.open('Images/left_btn_1.png')
left_img_1_load = ImageTk.PhotoImage(left_img_1)
left_img_2 = Image.open('Images/left_btn_2.png')
left_img_2_load = ImageTk.PhotoImage(left_img_2)

right_img_1 = Image.open('Images/right_btn_1.png')
right_img_1_load = ImageTk.PhotoImage(right_img_1)
right_img_2 = Image.open('Images/right_btn_2.png')
right_img_2_load = ImageTk.PhotoImage(right_img_2)

rst_img_1 = Image.open('Images/rst_btn_1.png')
rst_img_1_load = ImageTk.PhotoImage(rst_img_1)
rst_img_2 = Image.open('Images/rst_btn_2.png')
rst_img_2_load = ImageTk.PhotoImage(rst_img_2)

###########################
## Create Tkinter Window ##
###########################

root = tk.Tk()
root.title('Antenna Configuration')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 560, 560
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(560, 560)
root.resizable(height = False, width = False)
#root.maxsize(800, 540)

# Frames
parentFrame = tk.Frame(root, width=560, height=560, bg='#083414')
parentFrame.grid()
parentFrame.grid_propagate(False)

mainFrame = tk.LabelFrame(parentFrame, text='', width=540, height=540, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='#083414')
mainFrame.grid(row=0, column=0, padx=10, pady=10)
mainFrame.grid_propagate(False)

main_bg = tk.Label(mainFrame, image=frame_img_load, width=540, height=540) # set main Frame Background
main_bg.grid(row=0)

######################
## Common Functions ##
######################

def update(): # update dynamic variables
    while(True):
        curr_angle = cf.servo_theta_phi_get()
        data_phi_val = cf.get_sig_data()[1]
        sig_str = round(data_phi_val[512], 2) # signal strength (dbm) reading
        dBm_txt.set(sig_str)
        theta_val = curr_angle[0]
        phi_val = curr_angle[1]
        curr_angle_theta.set(theta_val)
        curr_angle_phi.set(phi_val)
        #sleep(0.5) # increase or decrease update speed

def subprocess_launcher(file): # launch subprocess
    try:
        process = sp.Popen(['python', file], shell=True, creationflags=sp.CREATE_NEW_CONSOLE)

    except:
        pass
        
####################
## Create Widgets ##
####################

#--------------------Parameters Panel--------------------

cent_freq_txt = tk.StringVar(value=cent_freq_val) # center frequency data from database
cent_freq = tk.Entry(mainFrame, textvariable=cent_freq_txt, bg='white', justify='center', borderwidth=0) # create center frequency entry box
cent_freq.grid(row=0, column=0, padx=(0,250), pady=(0,343))

samp_rate_txt = tk.StringVar(value=samp_rate_val) # sample rate data from database
samp_rate = tk.Entry(mainFrame, textvariable=samp_rate_txt, bg='white', justify='center', borderwidth=0) # create sample rate entry box
samp_rate.grid(row=0, column=0, padx=(0,250), pady=(0,224))

def set_1_click(clicked): # when set_1_btn is clicked
    set_1_btn['image'] = set_1_img_2_load

def set_1_rel(released): # when set_1_btn is released
    set_1_btn['image'] = set_1_img_1_load
    Thread(target=cf.signal_param_send, args=(cent_freq.get(), samp_rate.get())).start() # send center frequency and sample rate entries to database

set_1_btn = tk.Button(mainFrame, image=set_1_img_1_load, text='SET_1', width=94, height=26, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create set button for center frequency and sample rate inputs
set_1_btn.grid(row=0, column=0, padx=(0,253), pady=(0,97))
set_1_btn.bind('<Button-1>', set_1_click)
set_1_btn.bind('<ButtonRelease>', set_1_rel)

#--------------------------------------------------------

#-------------------Servo Control Panel------------------

curr_angle_theta = tk.StringVar(value='') # value of theta from database
curr_angle_phi = tk.StringVar(value='') # value of phi form database

curr_theta_axis = tk.Label(mainFrame, textvariable=curr_angle_theta, width=12, bg='white')
curr_theta_axis.place(x=340, y=109)

curr_phi_axis = tk.Label(mainFrame, textvariable=curr_angle_phi, width=12, bg='white')
curr_phi_axis.place(x=340, y=144)

conf_theta_axis_txt = tk.StringVar() # default value (empty) of theta axis entry box
conf_theta_axis = tk.Entry(mainFrame, textvariable=conf_theta_axis_txt, bg='white', width=14, justify='center', borderwidth=0) # create theta axis angle entry box
conf_theta_axis.grid(row=0, column=0, padx=(227,0), pady=(0,70))

conf_phi_axis_txt = tk.StringVar() # default value (empty) of phi axis entry box
conf_phi_axis = tk.Entry(mainFrame, textvariable=conf_phi_axis_txt, bg='white', width=14, justify='center', borderwidth=0) # create phi axis angle entry box 
conf_phi_axis.grid(row=0, column=0, padx=(227,0), pady=(0,0))

def set_2_click(clicked): # when set_2_btn is clicked
    set_2_btn['image'] = set_2_img_2_load  
    Thread(target=cf.servo_theta_phi_send, args=(conf_theta_axis.get(), conf_phi_axis.get())).start() # send theta and phi axis angle entries to database

def set_2_rel(released): # when set_2_btn is released
    set_2_btn['image'] = set_2_img_1_load

set_2_btn = tk.Button(mainFrame, image=set_2_img_1_load, text='', width=74, height=20, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create set button for theta and phi axis angle entries
set_2_btn.grid(row=0, column=0, padx=(189,0), pady=(70,0))
set_2_btn.bind('<Button-1>', set_2_click)
set_2_btn.bind('<ButtonRelease>', set_2_rel)

def up_click(clicked): # when up_btn is clicked
    up_btn['image'] = up_img_2_load
    Thread(target=cf.servo_theta_phi_incr, args=('up',)).start() # send phi axis angle of 5 degrees increment to database

def up_rel(released): # when up_btn is released
    up_btn['image'] = up_img_1_load

up_btn = tk.Button(mainFrame, image=up_img_1_load, text='', width=31, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)  # create up button
up_btn.grid(row=0, column=0, padx=(189,0), pady=(145,0))
up_btn.bind('<Button-1>', up_click)
up_btn.bind('<ButtonRelease>', up_rel)

def down_click(clicked): # when down_btn is clicked
    down_btn['image'] = down_img_2_load
    Thread(target=cf.servo_theta_phi_incr, args=('down',)).start() # send phi axis angle of 5 degrees decrement to database

def down_rel(released): # when down_btn is released
    down_btn['image'] = down_img_1_load

down_btn = tk.Button(mainFrame, image=down_img_1_load, text='', width=31, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create down button
down_btn.grid(row=0, column=0, padx=(189,0), pady=(288,0)) # send theta axis angle of 5 degrees increment to database
down_btn.bind('<Button-1>', down_click)
down_btn.bind('<ButtonRelease>', down_rel)

def left_click(clicked): # when left_btn is clicked
    left_btn['image'] = left_img_2_load
    Thread(target=cf.servo_theta_phi_incr, args=('left',)).start() # send theta axis angle of 5 degrees decrement to database

def left_rel(released): # when left_btn is released
    left_btn['image'] = left_img_1_load

left_btn = tk.Button(mainFrame, image=left_img_1_load, text='', width=31, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create left button
left_btn.grid(row=0, column=0, padx=(120,0), pady=(217,0))
left_btn.bind('<Button-1>', left_click)
left_btn.bind('<ButtonRelease>', left_rel)

def right_click(clicked): # when right_btn is clicked
    right_btn['image'] = right_img_2_load
    Thread(target=cf.servo_theta_phi_incr, args=('right',)).start() # send theta axis angle of 5 degrees increment to database

def right_rel(released): # when right_btn is released
    right_btn['image'] = right_img_1_load

right_btn = tk.Button(mainFrame, image=right_img_1_load, text='', width=31, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create right button
right_btn.grid(row=0, column=0, padx=(261,0), pady=(217,0))
right_btn.bind('<Button-1>', right_click)
right_btn.bind('<ButtonRelease>', right_rel)

def rst_click(clicked): # when rst_btn is clicked
    rst_btn['image'] = rst_img_2_load
    Thread(target=cf.servo_theta_phi_incr, args=('rst',)).start() # send theta and phi angle of both 90 degrees to database

def rst_rel(released): # when rst_btn is released
    rst_btn['image'] = rst_img_1_load

rst_btn = tk.Button(mainFrame, image=rst_img_1_load, text='', width=31, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create reset button
rst_btn.grid(row=0, column=0, padx=(189,0), pady=(217,0))
rst_btn.bind('<Button-1>', rst_click)
rst_btn.bind('<ButtonRelease>', rst_rel)
    
#--------------------------------------------------------

#----------------------Output Panel----------------------

dBm_txt = tk.StringVar(value='') # value of signal strength from database
dBm = tk.Label(mainFrame, textvariable=dBm_txt, width=12, bg='white') # create signal strength label
dBm.place(x=119, y=317)

def live_click(clicked): # when live_btn is clicked
    live_btn['image'] = live_img_2_load
    Thread(target=subprocess_launcher, args=['Scripts/anim_plot_online.pyw']).start() # launch frequency spectrum live graph

def live_rel(released): # when live_btn is released
    live_btn['image'] = live_img_1_load

live_btn = tk.Button(mainFrame, image=live_img_1_load, text='', width=134, height=34, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create live graph button
live_btn.grid(row=0, column=0, padx=(0,251), pady=(256,0))
live_btn.bind('<Button-1>', live_click)
live_btn.bind('<ButtonRelease>', live_rel)

def snap_click(clicked): # when snap_btn is clicked
    snap_btn['image'] = snap_img_2_load
    Thread(target=subprocess_launcher, args=['Scripts/static_plot_online.pyw']).start() # launch frequency spectrum static graph

def snap_rel(released): # when snap_btn is released
    snap_btn['image'] = snap_img_1_load

snap_btn = tk.Button(mainFrame, image=snap_img_1_load, text='', width=134, height=34, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create graph snapshot button
snap_btn.grid(row=0, column=0, padx=(0,251), pady=(330,0))
snap_btn.bind('<Button-1>', snap_click)
snap_btn.bind('<ButtonRelease>', snap_rel)

#--------------------------------------------------------

update_thr = Thread(target=update) # update data
update_thr.start()
root.mainloop() # run tkinter window
