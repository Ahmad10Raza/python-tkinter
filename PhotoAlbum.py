import tkinter as Tk
from PIL import Image, ImageTk
import random
import glob

class gui:
    def __init__(self, mainwin):
        self.counter = 0
        self.mainwin = mainwin
        self.mainwin.title("Our Photos")
        self.colour()
        self.mainwin.configure(bg = "black")
        self.Frame = Tk.Frame(mainwin)
        self.img = Tk.Label(self.Frame)
        self.Frame.place(relheight = 0.85, relwidth = 0.9, relx = 0.05, rely = 0.05 )
        self.img.pack()
        self.pic()
    def colour(self):
        self.colours  =['gray47','gray48']

        c = random.choice(self.colours)
        self.mainwin.configure(bg = c)
        root.after(2000, self.colour)

    def pic(self):
        for name in glob.glob(r"/home/blackheart/Pictures/*"):
            self.pic_list = []
            val = name
            self.pic_list.append(val)
        
        if self.counter == len(self.pic_list) - 1:
            self.counter = 0
        else:
            self.counter == self.counter + 1
        
        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)
        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]
        self.real_aspect = self.pic_width/self.pic_height
        self.calc_width = int(self.real_aspect * 800)  
        self.load2 = self.load.resize((self.calc_width, 800))
        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image = self.render)
        self.img.image = self.render
        root.after(2000, self.pic) 
  


root = Tk.Tk()
myprog = gui(root)
root.geometry("800x600")
root.mainloop()