from tkinter import *

class UIpaint:


    def __init__(self):
        self.root = Tk()
        self.root.title("paint")
        self.root.geometry("1920x1080")
        self.create_toolbar()
        self.create_buttons()
        self.create_canvas()
        #self.root.attributes('-fullscreen', True)
        self.root.rowconfigure([1,4], weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.mainloop()
    
    def Save():
        #todo
        pass
    
    def New():
        #todo
        pass
    
    def create_toolbar(self):
        self.toolbar = Menu(self.root)
        self.root.config(menu=self.toolbar)
        filemenu = Menu(self.toolbar)
        filemenu.add_command(label="Save", command=self.Save)
        filemenu.add_command(label="New", command=self.New)
        self.toolbar.add_cascade(label="File", menu=filemenu)

    

    def create_buttons(self):
        self.pennello = Button(self.root, text="pennello", font=("Helvetica bold", 20), bg= "white", width=3)
        self.gomma = Button(self.root, text="gomma", font=("Helvetica bold", 20), bg= "white", width=3)
        self.pennello.grid(row=2, column=0)
        self.gomma.grid(row=3, column=0)


    def create_canvas(self):
        self.canvas = Canvas(self.root, bg="red")
        self.canvas.grid(row = 1, column=1, rowspan=5, columnspan=2,sticky="nsew")
