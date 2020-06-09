from tkinter import *
import tkinter.messagebox  as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
 
def newfile():
    global file
    root.title("Untitled-notepad")
    file=NONE
    TextArea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(filetypes[("All Files","*.*"),
          ("Text Documents","*.txt")],defaultextension=".txt")
    if file=="":
        file=NONE
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(filetypes[("All Files","*.*"),("Text Documents","*.txt")],
              initialfile="Untitled-Notepad",defaultextension=".txt")
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.pathh.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
    
def quitapp():
    root.destroy()
    
def cut():
    TextArea.event_generate(("<<Cut>>"))
    
def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    
def about():
    tmsg.showinfo("Notepad","Notepad with karishma")

if __name__=='__main__':
    root=Tk()
    root.geometry("733x600")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("notepad1.ico")
    
    #add text area
    TextArea=Text(root,font="lucida 13")
    file=NONE
    TextArea.pack(expand=True,fill=BOTH)
    
    #menubar
    Menubar=Menu(root)
    FileMenu=Menu(Menubar,tearoff=0)
    FileMenu.add_command(label="New",command=newfile)
    FileMenu.add_command(label="Open",command=openfile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Save",command=savefile)
    FileMenu.add_command(label="Exit",command=quitapp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    
    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)
    
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    
    root.config(menu=Menubar)
    
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    
    root.mainloop()