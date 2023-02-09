import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import os
import subprocess as sp
import signal

try:
    pid_log = cf.get_pid('Scripts/process/login_pid')
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!') # Error prompt
    os.kill(pid_log, signal.SIGTERM)
    pid = os.getpid()
    log_id = open('Scripts/process/login_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/login_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

root = tk.Tk()
root.title('Login')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 560, 320
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(560, 320)
root.resizable(height = False, width = False)
#root.maxsize(800, 540)

# Frames
mainFrame = tk.LabelFrame(root, text='', width=560, height=320, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='white')
mainFrame.grid(row=0)
mainFrame.grid_propagate(False)

# Images
frame_img = Image.open('Images/login_1.png')
frame_img_load = ImageTk.PhotoImage(frame_img)

admin_img_1 = Image.open('Images/admin_btn_1.png')
admin_img_1_load = ImageTk.PhotoImage(admin_img_1)
admin_img_2 = Image.open('Images/admin_btn_2.png')
admin_img_2_load = ImageTk.PhotoImage(admin_img_2)

student_img_1 = Image.open('Images/student_btn_1.png')
student_img_1_load = ImageTk.PhotoImage(student_img_1)
student_img_2 = Image.open('Images/student_btn_2.png')
student_img_2_load = ImageTk.PhotoImage(student_img_2)

# Common Functions
def login_option(option):
    if option == 'admin':
        login = open('login', 'w+')
        login.write('admin')
        login.close()
        launch_main = sp.Popen(['python', 'main_gui.pyw'], shell=True, creationflags = sp.CREATE_NEW_CONSOLE)

    elif option == 'student':
        login = open('login', 'w+')
        login.write('student')
        login.close()
        launch_main = sp.Popen(['python', 'main_gui.pyw'], shell=True, creationflags = sp.CREATE_NEW_CONSOLE)

# Main Frame Widget5
main_bg = tk.Label(mainFrame, image=frame_img_load, width=560, height=320, highlightcolor='#282828', borderwidth=0, highlightthickness=0, bg='white')
main_bg.grid(row=0, column=0, padx=(0,0), pady=(0,0))

def admin_click(clicked):
    admin_btn['image'] = admin_img_2_load
    Thread(target=login_option, args=['admin']).start()

def admin_rel(released):
    admin_btn['image'] = admin_img_1_load
    root.destroy()

admin_btn = tk.Button(mainFrame, image=admin_img_1_load, text='', width=78, height=95, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0, background='white', activebackground='white')
admin_btn.grid(row=0, padx=(0,137), pady=(182,0))
admin_btn.bind('<Button-1>', admin_click)
admin_btn.bind('<ButtonRelease>', admin_rel)

def student_click(clicked):
    student_btn['image'] = student_img_2_load
    Thread(target=login_option, args=['student']).start()
    
def student_rel(released):
    student_btn['image'] = student_img_1_load
    root.destroy()

student_btn = tk.Button(mainFrame, image=student_img_1_load, text='', width=79, height=95, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0, background='white', activebackground='white')
student_btn.grid(row=0, padx=(137,0), pady=(182, 0))
student_btn.bind('<Button-1>', student_click)
student_btn.bind('<ButtonRelease>', student_rel)

root.mainloop()
