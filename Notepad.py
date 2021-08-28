from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

if __name__ == '__main__':
    root= Tk()
    root.title("Notpad")
    root.geometry("600x799")

    def newFile():
        global file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0,END)
        

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f= open(file,"r")
            TextArea.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt" , defaultextension=".txt", filetypes=[("All files","*.*"),("Text Documents","*.txt")])
            
            if file == "":
                file = None
            
            else:
                #save as a  anew file
                f = open(file,"w")
                f.write(TextArea.get(1.0 , END))
                f.close()


                root.title(os.path.basename(file) + " - Notepad")
        else:
            # save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            

    def quiteApp():
        root.destroy()
        pass

    def cut():
        TextArea.event_generate(("<<Cut>>"))
        pass

    def copy():
        TextArea.event_generate(("<<Copy>>"))
        pass

    def paste():
        TextArea.event_generate(("<<Paste>>"))
        pass

    def about():
        showinfo("Notepad","Notepad By Ritesh")
        
  
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    #----------------Menubar--------------------------
    MenuBar = Menu(root)

    #filemenu starts
    FileMenu = Menu(MenuBar, tearoff=0)

    # To open new file------
    FileMenu.add_command(label = "New", command=newFile)

    # ------To open already existing file ------
    FileMenu.add_command(label = "Open", command=openFile)

    # To save the current File---

    FileMenu.add_command(label ="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command=quiteApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    #----------file menu ends
        # Edit Menu Starts
    EditMenu = Menu(MenuBar,tearoff=0)
    #To give a feature of cut,copy,paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    # edit menu ends

    #help menu start

    HelpMenu = Menu(MenuBar ,tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu = HelpMenu)


    #help menu ends
    root.config(menu=MenuBar)

    # -------- Adding scroolbar----
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()
