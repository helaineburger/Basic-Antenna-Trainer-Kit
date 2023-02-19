####################
## Import Modules ##
####################

import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from threading import Thread
import subprocess as sp
import os
import signal
import Scripts.config_functions as cf

###########################
## Check Running Process ##
###########################

try:
    pid_log = cf.get_pid('Scripts/process/main_gui_pid') # read process id
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!')
    os.kill(pid_log, signal.SIGTERM) # kill existing duplicate process
    pid = os.getpid()
    log_id = open('Scripts/process/main_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/main_gui_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()
    
########################
## Read Login Details ##
########################

login_file = open('login', 'a+')
login_file.seek(0)
login = login_file.readlines()[0]

#################
## Load Images ##
#################

# Images
classroom_img_1 = Image.open('Images/classroom_btn_1.png')
classroom_img_1_load = ImageTk.PhotoImage(classroom_img_1)
classroom_img_2 = Image.open('Images/classroom_btn_2.png').convert('RGBA')
classroom_img_2_load = ImageTk.PhotoImage(classroom_img_2)

laboratory_img_1 = Image.open('Images/laboratory_btn_1.png')
laboratory_img_1_load = ImageTk.PhotoImage(laboratory_img_1)
laboratory_img_2 = Image.open('Images/laboratory_btn_2.png').convert('RGBA')
laboratory_img_2_load = ImageTk.PhotoImage(laboratory_img_2)

courses_img_1 = Image.open('Images/courses_btn_1.png')
courses_img_1_load = ImageTk.PhotoImage(courses_img_1)
courses_img_2 = Image.open('Images/courses_btn_2.png').convert('RGBA')
courses_img_2_load = ImageTk.PhotoImage(courses_img_2)

go_img_1 = Image.open('Images/go_btn_1.png')
go_img_1_load = ImageTk.PhotoImage(go_img_1)
go_img_2 = Image.open('Images/go_btn_2.png').convert('RGBA')
go_img_2_load = ImageTk.PhotoImage(go_img_2)

leftframe_img = Image.open('Images/leftframe.png')
leftframe_img_load = ImageTk.PhotoImage(leftframe_img)

rightframe_admin_img = Image.open('Images/rightframe_admin.png')
rightframe_admin_img_load = ImageTk.PhotoImage(rightframe_admin_img)
rightframe_student_img = Image.open('Images/rightframe_student.png')
rightframe_student_img_load = ImageTk.PhotoImage(rightframe_student_img)

logout_img_1 = Image.open('Images/logout_btn_1.png')
logout_img_1_load = ImageTk.PhotoImage(logout_img_1)
logout_img_2 = Image.open('Images/logout_btn_2.png')
logout_img_2_load = ImageTk.PhotoImage(logout_img_2)

about_img = Image.open('Images/about_btn.png')
about_img_load = ImageTk.PhotoImage(about_img)

contact_img = Image.open('Images/contact_btn.png')
contact_img_load = ImageTk.PhotoImage(contact_img)

###########################
## Create Tkinter Window ##
###########################

root = tk.Tk()
root.title('HyFlex Class Portal')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 800, 535
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(800,540)
root.resizable(height = False, width = False)

# Frames
mainFrame = tk.Frame(root, width=800, height=540, bg='#083414')
mainFrame.grid()
mainFrame.grid_propagate(False)

left_frame = tk.LabelFrame(mainFrame, text='', width=575, height=520,highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='#083414')
left_frame.grid(row=0, column=0, padx=10, pady=10)
left_frame.grid_propagate(False)

right_frame = tk.LabelFrame(mainFrame, text='', width=195, height=520, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='#083414')
right_frame.grid(row=0, column=1, padx=(0,10), pady=10)
right_frame.grid_propagate(False)

######################
## Common Functions ##
######################

def browser(link): # launch browser link
    webbrowser.open(link)

def subprocess_launcher(file): # launch subprocess
    try:
        process = sp.Popen(['python', file], shell=True, creationflags = sp.CREATE_NEW_CONSOLE)

    except:
        pass
    
####################
## Create Widgets ##
####################

# Left Frame Widgets
left_main_bg = tk.Label(left_frame, image=leftframe_img_load, width=569, height=514)
left_main_bg.grid(row=0)

def cm_b_click(clicked): # when classroom_btn is clicked
    classroom_btn['image'] = classroom_img_2_load

def cm_b_rel(released): # when classroom_btn is released
    classroom_btn['image'] = classroom_img_1_load
    Thread(target=browser, args=('meet.google.com',)).start() # open google meet link in a browser

classroom_btn = tk.Button(left_frame, image=classroom_img_1_load, text='CLASSROOM', width=154, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create classroom button
classroom_btn.grid(row=0, padx=(0,275), pady=(360,0))
classroom_btn.bind('<Button-1>', cm_b_click)
classroom_btn.bind('<ButtonRelease>', cm_b_rel)

def lb_b_click(clicked): # when laboratory_btn is clicked
    laboratory_btn['image'] = laboratory_img_2_load
    
def lb_b_rel(released): # when laboratory_btn is released
    laboratory_btn['image'] = laboratory_img_1_load
    Thread(target=subprocess_launcher, args=['lab_menu_gui.pyw']).start() # launch laboratory menu gui

laboratory_btn = tk.Button(left_frame, image=laboratory_img_1_load, text='LABORATORY', width=142, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create laboratory button
laboratory_btn.grid(row=0, padx=(25,0), pady=(360,0))
laboratory_btn.bind('<Button-1>', lb_b_click)
laboratory_btn.bind('<ButtonRelease>', lb_b_rel)

def cr_b_click(clicked): # when courses_btn is clicked
    courses_btn['image'] = courses_img_2_load

def cr_b_rel(released): # when courses_btn is released
    courses_btn['image'] = courses_img_1_load
    Thread(target=browser, args=('lsu.instructure.com/courses',)).start() # open lsu canvas link in a browser

courses_btn = tk.Button(left_frame, image=courses_img_1_load, text='COURSES', width=127, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create courses button
courses_btn.grid(row=0, padx=(299,0), pady=(360,0))
courses_btn.bind('<Button-1>', cr_b_click)
courses_btn.bind('<ButtonRelease>', cr_b_rel)

# Right Frame Widgets
if login == 'admin':
    right_main_bg = tk.Label(right_frame, image=rightframe_admin_img_load, width=191, height=514) # set right frame background
    right_main_bg.grid(row=0)

    annc_text = tk.Text(right_frame, height=12, width=19, bg='#eceeef', fg='#282828', borderwidth=0, highlightthickness=0, wrap=tk.WORD) # create announcement text box
    annc_text.grid(row=0, padx=(1,0), pady=(62,0))
    default_val = cf.get_annc()
    annc_text.insert(tk.END, default_val)

    def ok_b_click(clicked): # when go_btn is clicked
        go_btn['image'] = go_img_2_load
        
    def ok_b_rel(released): # when go_btn is released
        go_btn['image'] = go_img_1_load
        Thread(target=cf.send_annc(annc_text.get('1.0', tk.END))).start() # send announcement data from announcement text box to database

    go_btn = tk.Button(right_frame, image=go_img_1_load, text='GO', width=125, height=32, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
    go_btn.grid(row=0, padx=(0,0), pady=(330,0))
    go_btn.bind('<Button-1>', ok_b_click)
    go_btn.bind('<ButtonRelease>', ok_b_rel)

elif login ==  'student':
    right_main_bg = tk.Label(right_frame, image=rightframe_student_img_load, width=191, height=514) # set right frame background
    right_main_bg.grid(row=0)

    annc_text = tk.Text(right_frame, height=15, width=19, bg='#eceeef', fg='#282828', borderwidth=0, highlightthickness=0, wrap=tk.WORD) # create announcement text box
    annc_text.grid(row=0, padx=(1,0), pady=(108,0))
    default_val = cf.get_annc() # get announcement string from database
    annc_text.insert(tk.END, default_val) # load announcement string to annoucenment text box
    annc_text.config(state=tk.DISABLED)

def logout_click(clicked): # when logout_btn is clicked
    logout_btn['image'] = logout_img_2_load

def logout_release(released): # when logout_btn is released
    logout_btn['image'] = logout_img_1_load
    Thread(target=subprocess_launcher, args=['login.pyw']).start() # launch login gui
    root.destroy() # terminate tkinter window

logout_btn = tk.Button(right_frame, image=logout_img_1_load, text='logout', width=30, height=31, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0, background='#083414', activebackground='#083414') # create logout button
logout_btn.grid(row=0, padx=(133,0), pady=(0,475))
logout_btn.bind('<Button-1>', logout_click)
logout_btn.bind('<ButtonRelease>', logout_release)
    
def abt_b_click(clicked): # when about_btn is clicked
    about_btn['image'] = about_img_load
    Thread(target=subprocess_launcher, args=['about.pyw']).start() # launch about gui

about_btn = tk.Button(right_frame, image=about_img_load, text='ABOUT', width=32, height=6, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create about button
about_btn.grid(row=0, padx=(0,0), pady=(406,0))
about_btn.bind('<Button-1>', abt_b_click)

def cnt_b_click(clicked): # when contact_btn is clicked
    contact_btn['image'] = contact_img_load
    Thread(target=subprocess_launcher, args=['contact.pyw']).start() # launch contact gui

contact_btn = tk.Button(right_frame, image=contact_img_load, text='CONTACT', width=53, height=8, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0) # create contact button
contact_btn.grid(row=0, padx=(0,0), pady=(436,0))
contact_btn.bind('<Button-1>', cnt_b_click)

root.mainloop() # run tkinter window
