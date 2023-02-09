import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import subprocess as sp
import Scripts.config_functions as cf
import os
import signal

try:
    pid_log = cf.get_pid('Scripts/process/lab_menu_gui_pid')
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM)
    pid = os.getpid()
    log_id = open('Scripts/process/lab_menu_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()   

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/lab_menu_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()
    
root = tk.Tk()
root.title('Laboratory Menu')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 450, 320
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(450, 320)
root.resizable(height = False, width = False)
#root.maxsize(800, 540)

# Frames
mainFrame = tk.LabelFrame(root, text='', width=450, height=320, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='white')
mainFrame.grid(row=0)
mainFrame.grid_propagate(False)

# Images
frame_img = Image.open('Images/lab_menu_1.png')
frame_img_load = ImageTk.PhotoImage(frame_img)

capture_img_1 = Image.open('Images/capture_btn_1.png')
capture_img_1_load = ImageTk.PhotoImage(capture_img_1)
capture_img_2 = Image.open('Images/capture_btn_2.png')
capture_img_2_load = ImageTk.PhotoImage(capture_img_2)

output_control_img_1 = Image.open('Images/output_control_btn_1.png')
output_control_img_1_load = ImageTk.PhotoImage(output_control_img_1)
output_control_img_2 = Image.open('Images/output_control_btn_2.png')
output_control_img_2_load = ImageTk.PhotoImage(output_control_img_2)

calibrate_sdr_img_1 = Image.open('Images/calibrate_sdr_btn_1.png')
calibrate_sdr_img_1_load = ImageTk.PhotoImage(calibrate_sdr_img_1)
calibrate_sdr_img_2 = Image.open('Images/calibrate_sdr_btn_2.png')
calibrate_sdr_img_2_load = ImageTk.PhotoImage(calibrate_sdr_img_2)

# Main Frame Widget
main_bg = tk.Label(mainFrame, image=frame_img_load, width=450, height=320, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='white')
main_bg.grid(row=0, column=0, padx=(0,0), pady=(0,0))

# Common Functions
def subprocess_launcher(file):
    try:
        process = sp.Popen(['python', file], creationflags = sp.CREATE_NEW_CONSOLE, shell=True)

    except:
        print('Failed to launch script!')

def subprocess_launcher_with_console(file):
    try:
        process = sp.Popen(['python', file], creationflags = sp.CREATE_NEW_CONSOLE, shell=False)

    except:
        print('Failed to launch script!')

def subprocess_launcher_add_args(file, arg_list):
    try:
        process = sp.Popen(['python', file] + arg_list, shell=True)
    except:
        pass

def capture_click(clicked):
    capture_btn['image'] = capture_img_2_load
    Thread(target=subprocess_launcher_with_console, args=['Scripts/send_data_online.py']).start()

def capture_rel(released):
    capture_btn['image'] = capture_img_1_load

capture_btn = tk.Button(mainFrame, image=capture_img_1_load, text='capture', width=194, height=50, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
capture_btn.grid(row=0, padx=(0,0), pady=(0,143))
capture_btn.bind('<Button-1>', capture_click)
capture_btn.bind('<ButtonRelease>', capture_rel)

def output_control_click(clicked):
    output_control_btn['image'] = output_control_img_2_load
    Thread(target=subprocess_launcher, args=['antenna_config_gui.pyw']).start()

def output_control_rel(released):
    output_control_btn['image'] = output_control_img_1_load

output_control_btn = tk.Button(mainFrame, image=output_control_img_1_load, text='output and control', width=194, height=50, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
output_control_btn.grid(row=0, padx=(0,0), pady=(7,0))
output_control_btn.bind('<Button-1>', output_control_click)
output_control_btn.bind('<ButtonRelease>', output_control_rel)

def calibrate_sdr_click(clicked):
    calibrate_sdr_btn['image'] = calibrate_sdr_img_2_load
    Thread(target=subprocess_launcher, args=['calibrate_gui.pyw']).start()

def calibrate_sdr_rel(released):
    calibrate_sdr_btn['image'] = calibrate_sdr_img_1_load

calibrate_sdr_btn = tk.Button(mainFrame, image=calibrate_sdr_img_1_load, text='calibrate sdr', width=194, height=50, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
calibrate_sdr_btn.grid(row=0, padx=(0,0), pady=(156,0))
calibrate_sdr_btn.bind('<Button-1>', calibrate_sdr_click)
calibrate_sdr_btn.bind('<ButtonRelease>', calibrate_sdr_rel)

root.mainloop()
