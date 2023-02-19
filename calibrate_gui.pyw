####################
## Import Modules ##
####################

import tkinter as tk
import Scripts.config_functions as cf
from PIL import Image, ImageTk
from threading import Thread
import subprocess as sp
import os
import signal

############################
##  Check Running Process ##
############################

try:
    pid_log = cf.get_pid('Scripts/process/calibrate_gui_pid') # read process
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/calibrate_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/calibrate_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

#################
## Load Images ##
#################

# Images
frame_img = Image.open('Images/calibrate.png')
frame_img_load = ImageTk.PhotoImage(frame_img)

calibrate_img_1 = Image.open('Images/calibrate_btn_1.png')
calibrate_img_1_load = ImageTk.PhotoImage(calibrate_img_1)
calibrate_img_2 = Image.open('Images/calibrate_btn_2.png').convert('RGBA')
calibrate_img_2_load = ImageTk.PhotoImage(calibrate_img_2)

man_calibrate_img_1 = Image.open('Images/man_calibrate_btn_1.png')
man_calibrate_img_1_load = ImageTk.PhotoImage(man_calibrate_img_1)
man_calibrate_img_2 = Image.open('Images/man_calibrate_btn_2.png').convert('RGBA')
man_calibrate_img_2_load = ImageTk.PhotoImage(man_calibrate_img_2)

###########################
## Create Tkinter Window ##
###########################

root = tk.Tk()
root.title('Frequency Calibration')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 540, 340
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(540, 340)
root.resizable(height = False, width = False)
#root.maxsize(800, 540)

# Frames
parentFrame = tk.Frame(root, width=540, height=340, bg='#083414')
parentFrame.grid()
parentFrame.grid_propagate(False)

mainFrame = tk.LabelFrame(parentFrame, text='', width=520, height=320, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='#083414')
mainFrame.grid(row=0, column=0, padx=10, pady=10)
mainFrame.grid_propagate(False)

# Main Frame Background
main_bg = tk.Label(mainFrame, image=frame_img_load, width=520, height=320)
main_bg.grid(row=0)

######################
## Common Functions ##
######################

def update(): # update dynamic variables
    while(True):
        offset_val = cf.get_offset() # get center frequency offset value from database
        curr_offset.set(offset_val)

def subprocess_launcher(file): # launch subprocess
    try:
        process = sp.Popen(['python', file], creationflags = sp.CREATE_NEW_CONSOLE)

    except:
        print('Failed to launch script!')
    
####################
## Create Widgets ##
####################

curr_offset = tk.StringVar(value='') # current offset value from database

offset_label_box = tk.Label(mainFrame, textvariable=curr_offset, width=16, bg='white') # create offset value label
offset_label_box.place(x=203, y=73)

man_input_txt = tk.StringVar(value='') # default value (empty) of offset entry box
man_input = tk.Entry(mainFrame, textvariable=man_input_txt, bg='white', width=20, justify='center', borderwidth=0) # create offset entry box
man_input.grid(row=0, column=0, padx=(0,228), pady=(53,0))

def man_cal_click(clicked): # when man_calibrate_btn is clicked
    man_calibrate_btn['image'] = man_calibrate_img_2_load
    
def man_cal_rel(released): # when man_calibrate_btn is released
    man_calibrate_btn['image'] = man_calibrate_img_1_load
    Thread(target=cf.send_offset(man_input.get())).start() # send offset value from entry box to database

man_calibrate_btn = tk.Button(mainFrame, image=man_calibrate_img_1_load, text='calibrate', width=137, height=34, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create manual calibration button
man_calibrate_btn.grid(row=0, padx=(0,229), pady=(175,0))
man_calibrate_btn.bind('<Button-1>', man_cal_click)
man_calibrate_btn.bind('<ButtonRelease>', man_cal_rel)

def cal_click(clicked): # when calibrate_btn is clicked
    calibrate_btn['image'] = calibrate_img_2_load
    Thread(target=subprocess_launcher, args=['calc_offset.py']).start() # launch automatic calibration script
    
def cal_rel(released): # when calibrate_btn is released
    calibrate_btn['image'] = calibrate_img_1_load
    

calibrate_btn = tk.Button(mainFrame, image=calibrate_img_1_load, text='calibrate', width=137, height=34, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create automatic calibration button
calibrate_btn.grid(row=0, padx=(226,0), pady=(111,0))
calibrate_btn.bind('<Button-1>', cal_click)
calibrate_btn.bind('<ButtonRelease>', cal_rel)

#--------------------------------------------------------

update_thr = Thread(target=update) # update data
update_thr.start()
root.mainloop() # run tkinter window
