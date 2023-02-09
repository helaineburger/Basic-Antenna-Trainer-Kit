import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from threading import Thread
import os
import Scripts.config_functions as cf
import signal

try:
    pid_log = cf.get_pid('Scripts/process/about_pid')
    check_run = cf.check_pid_status(pid_log)

except:
    print('No log data')
    check_run = False

if check_run == True:
    print('Process is already running!') # Error prompt
    os.kill(pid_log, signal.SIGTERM)
    pid = os.getpid()
    log_id = open('Scripts/process/about_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

elif check_run == False:
    pid = os.getpid()
    log_id = open('Scripts/process/about_pid', 'w+')
    log_id.write(str(pid))
    log_id.close()

root = tk.Tk()
root.title('About Us')
root.iconbitmap('Images/icon.ico')

# Window Position
win_width, win_height = 225,120
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
pos_y = int((screen_height/2) - (win_height/2))
pos_x = int((screen_width/2) - (win_width/2))
root.geometry(f'+{pos_x}+{pos_y}')

# Canvas Size
root.minsize(225,120)
root.resizable(height = False, width = False)
#root.maxsize(225,120)

# Frames
mainFrame = tk.LabelFrame(root, width=225, height=120, bg='white', borderwidth=0, highlightthickness=0)
mainFrame.grid(row=0)
mainFrame.grid_propagate(True)

# Images
bg_img = Image.open('Images/about.png')
bg_img_load = ImageTk.PhotoImage(bg_img)

# Common Functions
def browser(link):
    webbrowser.open(link)
    
# Background
main_bg = tk.Label(mainFrame, image=bg_img_load, width=225, height=120)
main_bg.grid(row=0, column=0, padx=(0,0), pady=(0,0))

#Widgets
github_lbl = tk.Label(mainFrame, text='GitHub', background='white', fg='#083414', font=('arial bold', 9))
github_lbl.grid(row=0, padx=(0,0), pady=(0,20))

def github_click(clicked):
    Thread(target=browser, args=['https://github.com/helaineburger']).start()
    
github_link = tk.Label(mainFrame, text='https://github.com/helaineburger', fg='#083414', background='white', font=('arial', 9, 'underline'))
github_link.grid(row=0, padx=(0,0), pady=(20,0))
github_link.bind('<Button-1>', github_click)


root.mainloop()
