
from tkinter import *
from tkinter import ttk
import tkinter
# import sys,os
root = Tk()
root = tkinter.Tk()
root.configure(background='black')
# style configuration
style = ttk.Style(root)
style.configure('TLabel', background='black', foreground='white')
style.configure('TFrame', background='black')
root.geometry("655x444")
root.title("CodeWithHarry - Title Of My GUI")
# root.wm_iconbitmap("@logo.xbm")
# LOGO_PATH="logo.ico"
# LOGO_LINUX_PATH="@logo.xbm"  #do not forget "@" symbol and .xbm format for Ubuntu 
root = Tk()
# if "nt" == os.name:
#     root.wm_iconbitmap(bitmap = "notepad.ico")
# else:
#     root.wm_iconbitmap(bitmap = "@notepad.xbm")
# root.configure(bg='blue')

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()
