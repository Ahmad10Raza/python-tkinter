from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("800x600")

#by using tkinter
# phtot=PhotoImage(file="name.png") #only png formal support in tkinter

image=Image.open("IMAGES/Bugatti-Chiron.jpg")
photo=ImageTk.PhotoImage(image)

# image = image.resize((700, 700))
# image.show()


label=Label(image=photo)
label.pack()

root.mainloop()