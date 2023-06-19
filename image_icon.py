import tkinter as tk 
from PIL import Image , ImageTk



# Importing Images : 
tasker  =Image.open(r'assets\tasker.png')
tasker_resize  = tasker.resize((50,50))
tasker_icon = ImageTk.PhotoImage(tasker_resize)


