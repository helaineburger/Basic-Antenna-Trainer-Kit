import tkinter as tk
from PIL import Image, ImageTk

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
#root.maxsize(800,540)

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

set_img_1 = Image.open('Images/set_btn_1.png')
set_img_1_load = ImageTk.PhotoImage(set_img_1)
set_img_2 = Image.open('Images/set_btn_2.png').convert('RGBA')
set_img_2_load = ImageTk.PhotoImage(set_img_2)

leftframe_img = Image.open('Images/leftframe.png')
leftframe_img_load = ImageTk.PhotoImage(leftframe_img)

rightframe_img = Image.open('Images/rightframe.png')
rightframe_img_load = ImageTk.PhotoImage(rightframe_img)

# Left Frame Widget
left_main_bg = tk.Label(left_frame, image=leftframe_img_load, width=569, height=514)
left_main_bg.grid(row=0)

def cm_b_click(clicked):
    
    classroom_btn['image'] = classroom_img_2_load
def cm_b_rel(released):
    classroom_btn['image'] = classroom_img_1_load

classroom_btn = tk.Button(left_frame, image=classroom_img_1_load, text='CLASSROOM', width=154, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
classroom_btn.grid(row=0, padx=(0,275), pady=(360,0))
classroom_btn.bind('<Button-1>', cm_b_click)
classroom_btn.bind('<ButtonRelease>', cm_b_rel)

def lb_b_click(clicked):
    laboratory_btn['image'] = laboratory_img_2_load
def lb_b_rel(released):
    laboratory_btn['image'] = laboratory_img_1_load

laboratory_btn = tk.Button(left_frame, image=laboratory_img_1_load, text='LABORATORY', width=142, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
laboratory_btn.grid(row=0, padx=(25,0), pady=(360,0))
laboratory_btn.bind('<Button-1>', lb_b_click)
laboratory_btn.bind('<ButtonRelease>', lb_b_rel)

def cr_b_click(clicked):
    courses_btn['image'] = courses_img_2_load
def cr_b_rel(released):
    courses_btn['image'] = courses_img_1_load

courses_btn = tk.Button(left_frame, image=courses_img_1_load, text='COURSES', width=127, height=46, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
courses_btn.grid(row=0, padx=(299,0), pady=(360,0))
courses_btn.bind('<Button-1>', cr_b_click)
courses_btn.bind('<ButtonRelease>', cr_b_rel)

# Right Frame Widgets
right_main_bg = tk.Label(right_frame, image=rightframe_img_load, width=191, height=514)
right_main_bg.grid(row=0)

def ok_b_click(clicked): 
    set_btn['image'] = set_img_2_load
def ok_b_rel(released):
    set_btn['image'] = set_img_1_load

set_btn = tk.Button(right_frame, image=set_img_1_load, text='SET', width=125, height=32, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
set_btn.grid(row=0, padx=(0,0), pady=(330,0))
set_btn.bind('<Button-1>', ok_b_click)
set_btn.bind('<ButtonRelease>', ok_b_rel)

root.mainloop()
