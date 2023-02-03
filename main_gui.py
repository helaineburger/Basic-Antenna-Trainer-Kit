import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from threading import Thread

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

go_img_1 = Image.open('Images/go_btn_1.png')
go_img_1_load = ImageTk.PhotoImage(go_img_1)
go_img_2 = Image.open('Images/go_btn_2.png').convert('RGBA')
go_img_2_load = ImageTk.PhotoImage(go_img_2)

leftframe_img = Image.open('Images/leftframe.png')
leftframe_img_load = ImageTk.PhotoImage(leftframe_img)

rightframe_img = Image.open('Images/rightframe.png')
rightframe_img_load = ImageTk.PhotoImage(rightframe_img)

about_img = Image.open('Images/about_btn.png')
about_img_load = ImageTk.PhotoImage(about_img)

contact_img = Image.open('Images/contact_btn.png')
contact_img_load = ImageTk.PhotoImage(contact_img)


# Common Functions
def browser(link):
    webbrowser.open(link)

# Left Frame Widget
left_main_bg = tk.Label(left_frame, image=leftframe_img_load, width=569, height=514)
left_main_bg.grid(row=0)

def cm_b_click(clicked):
    classroom_btn['image'] = classroom_img_2_load
    Thread(target=browser, args=('meet.google.com',)).start()
   # webbrowser.open('meet.google.com')
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
    Thread(target=browser, args=('lsu.instructure.com/courses',)).start()
    #webbrowser.open('lsu.instructure.com/courses')
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
    go_btn['image'] = go_img_2_load
def ok_b_rel(released):
    go_btn['image'] = go_img_1_load

go_btn = tk.Button(right_frame, image=go_img_1_load, text='GO', width=125, height=32, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
go_btn.grid(row=0, padx=(0,0), pady=(330,0))
go_btn.bind('<Button-1>', ok_b_click)
go_btn.bind('<ButtonRelease>', ok_b_rel)

def abt_b_click(clicked): 
    about_btn['image'] = about_img_load

about_btn = tk.Button(right_frame, image=about_img_load, text='ABOUT', width=32, height=6, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
about_btn.grid(row=0, padx=(0,0), pady=(406,0))
about_btn.bind('<Button-1>', ok_b_click)

def cnt_b_click(clicked): 
    contact_btn['image'] = contact_img_load

contact_btn = tk.Button(right_frame, image=contact_img_load, text='CONTACT', width=53, height=8, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
contact_btn.grid(row=0, padx=(0,0), pady=(436,0))
contact_btn.bind('<Button-1>', ok_b_click)

root.mainloop()
