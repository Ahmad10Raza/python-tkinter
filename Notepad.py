from tkinter import *
import tkinter
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfile
import os

def newFile():
    global file 
    root.title("Untitled - Root Scrawl")
    file=None
    TextArea.delete(1.0,END)
    
    
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All file","*.txt"),("Text Document","*.txt")])
    if file=="":
       file=None
    else:
        root.title(os.path.basename(file)+"-Root Scrawl")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        
        
def saveFile():
    global fileif 
    if file==None:
        file=askopenfilename(initialfile="untitled.txt",defaultextension="*.txt",filetypes=[("All file","*.*")("Text Documents","*.txt")])
        if file=="":
            file=None
            
        else:
            #save the new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+ "-Root Scrawl")
            print("File Saved")
            
    else:
        #save file
        f=open(file ,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        
        
        
def quitApp():
    root.destroy()
    
def cut():
    TextArea.event_generate(("<>"))            
                    
def copy():
    TextArea.event_generate(("<>"))            

def paste():
    TextArea.event_generate(("<>"))            
        
        
def about():
    showinfo("Root Scrawl","Root Scrawl Editor By Ahmad Raza") 
    
    
    
if __name__=='__main__':
    
    root=Tk()
    # root = tkinter.Tk()
    # root.config(background='black')
    root.title("Untitled - Root Scrawl")
    # root.wm_iconbitmap("logo.ico")
    root.geometry("700x800")
    root.config(bg="red")
    # root.configure(background="grey")

    
    #Add Text Area
    TextArea=Text(root,font="lucida 15")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    
    #Creating Menu bar           
    MenuBar=Menu(root)
    
    FileMneu=Menu(MenuBar,tearoff=0)
    #to open new file
    FileMneu.add_command(label="new",command=newFile)
    
    #to open already exits file
    FileMneu.add_command(label="open",command=openFile)
    
    #to save current file
    FileMneu.add_command(label="save",command=saveFile)
    FileMneu.add_separator()
    FileMneu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMneu)
    #filemenu end 
    
    #Edits menu start here
    EditMenu=Menu(MenuBar,tearoff=0)
    
    #to give feature of cut copy  and paste
    
    EditMenu.add_command(label="cut",command=cut)        
    EditMenu.add_command(label="copy",command=copy)        
    EditMenu.add_command(label="paste",command=paste)
    
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    
    #edit menu end here
    
    
    #help menu start here
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Root Scrawl",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    #help menu end here
    
    root.config(menu=MenuBar)
    
    
    #Addint scrool bar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    
    root.mainloop()     

            