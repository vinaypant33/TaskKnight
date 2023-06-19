import tkinter as tk 
from tkinter import ttk 
import customtkinter as ctk 
from PIL import Image , ImageTk

import fonts
import colors
from ctypes import windll


# Files for the styles : 
import styles

main_dashboard  = tk.Tk()

# Constant Variables : 
height  = 650
width  = 1120
maximized  = False
minimized  = False
main_x = 0 
main_y = 0



screen_width  = main_dashboard.winfo_screenwidth()
screen_height  = main_dashboard.winfo_screenheight()


x_loc  = (screen_width //2 ) - ( width //2 )
y_loc   = (screen_height //2 ) - (height // 2 )

main_dashboard.geometry(f"{width}x{height}+{x_loc}+{y_loc}") # Setting the app in the center location. 
main_dashboard.overrideredirect(True) # Titlebar removed



# General Functions for the app : 
def Close_app():
    main_dashboard.destroy()

def max():
    global maximized
    if maximized == False : 
        main_dashboard.state('zoomed')
        maximized = True
        max_button.configure(text=u"\U0001F5D7")
    else: 
        maximized  = False
        main_dashboard.state('normal')
        max_button.configure(text=u"\U0001F5D6")


def set_appwindow(root):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.wm_withdraw()
        root.after(10, lambda: root.wm_deiconify())


def min():
    main_dashboard.overrideredirect(False)
    main_dashboard.wm_iconify()
    main_dashboard.bind('<FocusIn>' , on_deiconify)

def on_deiconify(event):
        if main_dashboard.wm_state() =='normal' and main_dashboard.overrideredirect() != True:
            main_dashboard.overrideredirect(True)
            set_appwindow(main_dashboard)


def mouse_click(event):
    # print(event)
    global main_x
    global main_y
    main_x  = event.x
    main_y = event.y

def mouse_move(event):
    # print(event)
    global main_x 
    global main_y 
    main_x = main_x
    main_y = main_y
    deltax = event.x - main_x
    deltay = event.y - main_y
    x_location = main_dashboard.winfo_x() + deltax
    y_location  = main_dashboard.winfo_y() + deltay
    main_dashboard.geometry(f"{width}x{height}+{x_location}+{y_location}")


# Setting up the general controls : Fix type controls : 

# Titlebar and Control Buttons
titlebar  = tk.Frame(main_dashboard ,  height=15 , background=colors.sidebar_base)
exit_button  = tk.Button(titlebar , text='\u2716' , command=Close_app)
max_button  = tk.Button(titlebar , text=u"\U0001F5D6", command=max)
min_button  =tk.Button(titlebar , text=u'\u2014' , command=min)

# Sidebar / Controls and Buttons :  
sidebar  = tk.Frame(main_dashboard , width=75, background=colors.sidebar_base)
sidebar.pack_propagate(0)

sidebar_upper_icon_frame  = tk.Frame(sidebar , height = 30 ,  width=50 , background = 'red')


# Configuring the controls : 
main_dashboard.configure(background=colors.app_base)
exit_button.configure(styles.button_styles(exit_button , None , None , colors.sidebar_base , colors.text_foreground , colors.app_base , colors.red , 0))
min_button.configure(styles.button_styles(min_button , None , None , colors.sidebar_base , colors.text_foreground , colors.app_base , colors.red , 0))
max_button.configure(styles.button_styles(max_button , None , None , colors.sidebar_base , colors.text_foreground , colors.app_base , colors.red , 0))



# Binding the controls :
titlebar.bind("<ButtonPress-1>" , mouse_click)
titlebar.bind("<B1-Motion>" , mouse_move)

exit_button.bind("<Enter>" , lambda event : exit_button.configure(background=colors.red))
max_button.bind("<Enter>" , lambda event : max_button.configure(background=colors.app_base))
min_button.bind("<Enter>" , lambda event : min_button.configure(background=colors.app_base))

exit_button.bind("<Leave>" , lambda event : exit_button.configure(background=colors.sidebar_base))
max_button.bind("<Leave>" , lambda event : max_button.configure(background=colors.sidebar_base))
min_button.bind("<Leave>" , lambda event : min_button.configure(background=colors.sidebar_base))


# Placing the general Controls :
# Titlebar and Buttons
titlebar.pack(side="top" , padx=(0,0) , fill='x')
exit_button.pack(side="right" , padx=(0, 0))
max_button.pack(side="right" , padx=(0,0))
min_button.pack(side='right' , padx=(0 , 0))
# Sidebar and Fix Controls : 
sidebar.pack(side='left'  , fill = 'y')
sidebar_upper_icon_frame.pack(side="top" , pady=(10 , 0) , padx=(10,10))



# runnung the main application : 
main_dashboard.after(10, lambda: set_appwindow(main_dashboard))
main_dashboard.mainloop()
