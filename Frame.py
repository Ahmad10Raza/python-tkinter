from tkinter import *
root=Tk()
root.geometry("700x500")

f1=Frame(root,bg="black",borderwidth=8,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,borderwidth=8,bg="black",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Dil ne ye kha hai dil se...",fg="white")
l.pack(pady=140)

l=Label(f2,text="Mohabbat ho gyi hai tumse",font="Helvetica 16 bold",fg="white",pady=22)
l.pack()

root.mainloop()