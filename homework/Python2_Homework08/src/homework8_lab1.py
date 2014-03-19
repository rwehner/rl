from tkinter import *

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=E+W+N+S)
        
        # Left-hand frames
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=1)
        self.frame1 = Label(self, bg='gray35')
        self.frame1.bind("<Button-1>", self.frame1clicked)
        self.frame1.grid(row=0, column=0, rowspan=6, columnspan=2, sticky=E+W+S+N)
        
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)
        self.frame2 = Label(self, bg='gray50')
        self.frame2.bind("<Button-1>", self.frame2clicked)
        self.frame2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=E+W+S+N)
        
        # Right-hand frame
        self.columnconfigure(2, weight=1)
        self.frame3 = Frame(self, bg='gray75')
        self.frame3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=E+W+S+N)
                
        self.frame3entry = Entry(self.frame3)
        self.frame3entry.pack(side=TOP, expand=False, fill=X)  
        
        self.frame3textarea = Text(self.frame3, bg='gray75')
        self.frame3textarea.pack(side=TOP, expand=True, fill=BOTH)
                
        # Bottom row buttons
        self.columnconfigure(0, weight=1)
        self.redbutton = Button(self, text="Red", command=self.turn_red)
        self.redbutton.grid(row=2, column=0, sticky=E+W)
        
        self.columnconfigure(1, weight=1)
        self.bluebutton = Button(self, text="Blue", command=self.turn_blue)
        self.bluebutton.grid(row=2, column=1, sticky=E+W)
        
        self.columnconfigure(2, weight=1)
        self.greenbutton = Button(self, text="Green", command=self.turn_green)
        self.greenbutton.grid(row=2, column=2, sticky=E+W)
        
        self.columnconfigure(3, weight=1)
        self.blackbutton = Button(self, text="Black", command=self.turn_black)
        self.blackbutton.grid(row=2, column=3, sticky=E+W)
         
        self.columnconfigure(4, weight=1)
        self.openbutton = Button(self, text="Open", command=self.open_file)
        self.openbutton.grid(row=2, column=4, sticky=E+W)
    
    def change_fg_color(self, textwidget, color='black'):
        textwidget.config(fg=color)    
    def turn_red(self):
        self.change_fg_color(self.frame3textarea, 'red')
    def turn_blue(self):
        self.change_fg_color(self.frame3textarea, 'blue')
    def turn_green(self):
        self.change_fg_color(self.frame3textarea, 'green')
    def turn_black(self):
        self.change_fg_color(self.frame3textarea, 'black')

    def open_file(self):
        newfile = self.frame3entry.get().strip()
        if not newfile:
            newtext = "Please enter valid file name above."
        else:
            try:
                newtext = open(newfile).read()
            except(IOError):
                newtext = "Failed to open {}".format(newfile)
        self.changetext(self.frame3textarea, newtext)     
    def changetext(self, textArea, newtext):
        textArea.delete(1.0, END)
        textArea.insert(END, newtext)

    def frameclicked(self, event, frame=None):
        print('You clicked {0} at x={1}, y={2}'.format(frame, event.x, event.y))
    def frame1clicked(self, event):
        self.frameclicked(event, frame="Frame 1")
    def frame2clicked(self, event):
        self.frameclicked(event, frame="Frame 2")
   
root = Tk()
app = Application(master=root)
app.mainloop()