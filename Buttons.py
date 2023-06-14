from tkinter import *

root =Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons")

def name():
    print("Name is Sameer Raza")
def age():
     print("Age is :13")
def Hobby():
     print("Hobby is Cricket")

frame = Frame(root, borderwidth=6, bg="black", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Buttons Example", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Age",command=age)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="Hobby",command=Hobby)
b4.pack(side=LEFT, padx=23)
root.mainloop()
