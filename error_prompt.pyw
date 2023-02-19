####################
## Import Modules ##
####################

import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
import sys
import Scripts.config_functions as cf

###################
## Get Arguments ##
###################

args = sys.argv[1:]
        
def error(file_name):
    root = tk.Tk()
    root.title('Error')
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

    # Frames
    mainFrame = tk.Frame(root, width=225, height=120, bg='#083414')
    mainFrame.grid()
    mainFrame.grid_propagate(False)

    # Images
    bg_loc = file_name
    bg = Image.open(bg_loc)
    bg_load = ImageTk.PhotoImage(bg)
    error_img_okay_1 = Image.open('Images/e_okay_btn_1.png')
    error_img_okay_1_load = ImageTk.PhotoImage(error_img_okay_1)
    error_img_okay_2 = Image.open('Images/e_okay_btn_2.png')
    error_img_okay_2_load = ImageTk.PhotoImage(error_img_okay_2)
    error_img_try_1 = Image.open('Images/e_try_again_btn_1.png')
    error_img_try_1_load = ImageTk.PhotoImage(error_img_try_1)
    error_img_try_2 = Image.open('Images/e_try_again_btn_2.png')
    error_img_try_2_load = ImageTk.PhotoImage(error_img_try_2)


    # Background
    main_bg = tk.Label(mainFrame, image=bg_load, width=225, height=120)
    main_bg.grid(row=0)

    #Widgets
    def ok_b_click(clicked):
        okay_btn['image'] = error_img_okay_2_load
        
    def ok_b_rel(released):
        okay_btn['image'] = error_img_okay_1_load
        sys.exit()
            
    okay_btn = tk.Button(mainFrame, image=error_img_okay_1_load, text='OKAY', width=68, height=22, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
    okay_btn.grid(row=0, padx=(0,85), pady=(78,0))
    okay_btn.bind('<Button-1>', ok_b_click)
    okay_btn.bind('<ButtonRelease>', ok_b_rel)

    def tr_b_click(clicked): 
        try_btn['image'] = error_img_try_2_load
        
        if args[1] == 'Error sending servo axis data!':
            Thread(target=cf.servo_x_y_send, args=(args[2], args[3])).start()

    def tr_b_rel(released):
        try_btn['image'] = error_img_try_1_load
        sys.exit()

    try_btn = tk.Button(mainFrame, image=error_img_try_1_load, text='SET', width=68, height=22, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
    try_btn.grid(row=0, padx=(85,0), pady=(76,0))
    try_btn.bind('<Button-1>', tr_b_click)
    try_btn.bind('<ButtonRelease>', tr_b_rel)

    root.mainloop()

error('Images/e_sending_servo.png')

