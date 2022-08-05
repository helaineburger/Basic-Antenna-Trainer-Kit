import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Assistant Robot')
'''root.iconbitmap('')'''

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
logo_img = tk.PhotoImage(file='Images/logo.png')

classroom_img_1 = Image.open('Images/classroom_btn_1.png')
classroom_img_1_load = ImageTk.PhotoImage(classroom_img_1)
classroom_img_2 = Image.open('Images/classroom_btn_2.png').convert('RGBA')
classroom_img_2_load = ImageTk.PhotoImage(classroom_img_2)

msg_img_1 = Image.open('Images/msg_img_1.png').convert('RGBA')
msg_img_1_load = ImageTk.PhotoImage(msg_img_1)
msg_img_2 = Image.open('Images/msg_img_2.png').convert('RGBA')
msg_img_2_load = ImageTk.PhotoImage(msg_img_2)

call_img_1 = Image.open('Images/call_img_1.png').convert('RGBA')
call_img_1_load = ImageTk.PhotoImage(call_img_1)
call_img_2 = Image.open('Images/call_img_2.png').convert('RGBA')
call_img_2_load = ImageTk.PhotoImage(call_img_2)

contacts_img_1 = Image.open('Images/contacts_img_1.png')
contacts_img_1_load = ImageTk.PhotoImage(contacts_img_1)
contacts_img_2 = Image.open('Images/contacts_img_2.png').convert('RGBA')
contacts_img_2_load = ImageTk.PhotoImage(contacts_img_2)

locate_img_1 = Image.open('Images/locate_img_1.png')
locate_img_1_load = ImageTk.PhotoImage(locate_img_1)
locate_img_2 = Image.open('Images/locate_img_2.png').convert('RGBA')
locate_img_2_load = ImageTk.PhotoImage(locate_img_2)

browser_img_1 = Image.open('Images/browser_img_1.png')
browser_img_1_load = ImageTk.PhotoImage(browser_img_1)
browser_img_2 = Image.open('Images/browser_img_2.png').convert('RGBA')
browser_img_2_load = ImageTk.PhotoImage(browser_img_2)

admin_img_1 = Image.open('Images/admin_img_1.png')
admin_img_1_load = ImageTk.PhotoImage(admin_img_1)
admin_img_2 = Image.open('Images/admin_img_2.png').convert('RGBA')
admin_img_2_load = ImageTk.PhotoImage(admin_img_2)

time_date = tk.PhotoImage(file='Images/time_date.png')

temp_img = Image.open('Images/temperature.png')
temp_img_load = ImageTk.PhotoImage(temp_img)

annc_img = tk.PhotoImage(file='Images/announcements.png')

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
    
classroom_btn = tk.Button(left_frame, image=classroom_img_1_load, text='CLASSROOM', width=154, height=46, borderwidth=0, bg = "White",  relief=tk.SUNKEN, highlightthickness=0)
classroom_btn.grid(row=0, padx=(0,275), pady=(360,0))
classroom_btn.bind('<Button-1>', cm_b_click)
classroom_btn.bind('<ButtonRelease>', cm_b_rel)


'''
def msg_b_click(clicked):
    msg_b['image'] = msg_img_2_load
def msg_b_rel(released):
    msg_b['image'] = msg_img_1_load
   
msg_b = tk.Button(left_frame, image=msg_img_1_load, text='MESSAGE', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
msg_b.grid(row=0, padx=(0,183), pady=(0,158))
msg_b.bind('<Button-1>', msg_b_click)
msg_b.bind('<ButtonRelease>', msg_b_rel)

def call_b_click(clicked):
    call_b['image'] = call_img_2_load
def call_b_rel(released):
    call_b['image'] = call_img_1_load
    
call_b = tk.Button(left_frame, image=call_img_1_load, text='CALL', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
call_b.grid(row=0, padx=(178,0), pady=(0,158))
call_b.bind('<Button-1>', call_b_click)
call_b.bind('<ButtonRelease>', call_b_rel)

def contacts_b_click(clicked):
    contacts_b['image'] = contacts_img_2_load
def contacts_b_rel(released):
    contacts_b['image'] = contacts_img_1_load
    
contacts_b = tk.Button(left_frame, image=contacts_img_1_load, text='CONTACTS', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
contacts_b.grid(row=0, padx=(0,183), pady=(98,0))
contacts_b.bind('<Button-1>', contacts_b_click)
contacts_b.bind('<ButtonRelease>', contacts_b_rel)

def locate_b_click(clicked):
    locate_b['image'] = locate_img_2_load
def locate_b_rel(released):
    locate_b['image'] = locate_img_1_load
    
locate_b = tk.Button(left_frame, image=locate_img_1_load, text='LOCATE', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
locate_b.grid(row=0, padx=(178,0), pady=(98,0))
locate_b.bind('<Button-1>', locate_b_click)
locate_b.bind('<ButtonRelease>', locate_b_rel)

def browser_b_click(clicked):
    browser_b['image'] = browser_img_2_load
def browser_b_rel(released):
    browser_b['image'] = browser_img_1_load
    
browser_b = tk.Button(left_frame, image=browser_img_1_load, text='BROWSER', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
browser_b.grid(row=0, padx=(0,183), pady=(351,0))
browser_b.bind('<Button-1>', browser_b_click)
browser_b.bind('<ButtonRelease>', browser_b_rel)

def admin_b_click(clicked):
    admin_b['image'] = admin_img_2_load
def admin_b_rel(released):
    admin_b['image'] = admin_img_1_load
    
admin_b = tk.Button(left_frame, image=admin_img_1_load, text='ADMIN', width=114, height=113, borderwidth=0, relief=tk.SUNKEN, highlightthickness=0)
admin_b.grid(row=0, padx=(178,0), pady=(351,0))
admin_b.bind('<Button-1>', admin_b_click)
admin_b.bind('<ButtonRelease>', admin_b_rel)
'''

# Right Frame Widgets
right_main_bg = tk.Label(right_frame, image=rightframe_img_load, width=191, height=514)
right_main_bg.grid(row=0)

'''
tm_img = tk.Label(right_frame, image=time_date, width=189, height=90)
tm_img.grid(padx=0)

tm = tk.Label(right_frame, text='12 : 00 : 00 AM', font=('Arial', 8), bg='white') # Time Label
tm.grid(row=0, padx=(45,0), pady=(0,34))

dy = tk.Label(right_frame, text='05 - 03 - 2022', font=('Arial', 8), bg='white') # Day Label
dy.grid(row=0, padx=(45,0), pady=(46,0))

temp_img = tk.Label(right_frame, image=temp_img_load, width=189, height=70)
temp_img.grid(row=1)

temp = tk.Label(right_frame, text=('--'), font=('Arial', 25,'bold'), fg='green', bg='white')
temp.grid(row=1, column=0, padx=(18,0), pady=(0,0))

anncLabel = tk.Label(right_frame, image=annc_img, width=189, height=195)
anncLabel.grid(row=2)

txF = tk.Text(right_frame, height=9, width=21, bg='white', fg='#282828', borderwidth=0, highlightthickness=0.5, wrap=tk.WORD)
txF.grid(row=2, column=0, padx=(0,0), pady=(30, 0))

annc = 'The brown fox jumped over the lazy dog.'
txF.insert(tk.END, annc)
txF.config(state=tk.DISABLED)

lg = tk.Button(right_frame, image=logo_img, text='MAIN LOGO', relief=tk.SUNKEN, width=191, height=149, borderwidth=0)
lg.grid(row=3)
'''


root.mainloop()
