from tkinter import *

def colorgen():
    while True:
        yield 'gray35'
        yield 'gray50'
        yield 'gray75'

class Application(Frame):
    
    def __init__(self, master=None):
        colors = colorgen()
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=E+W+N+S)
        
        cnt = 1
        for r in (0, 6):
            self.rowconfigure(r, weight=1)
            self.columnconfigure(0, weight=1)
            Label(self, text="Frame {0}".format(cnt), bg=next(colors)).grid(row=r, column=0, rowspan=6, columnspan=2, sticky=E+W+S+N)
            cnt += 1
        
        self.columnconfigure(2, weight=1)
        Label(self, text="Frame 3", bg=next(colors)).grid(row=0, column=2, rowspan=12, columnspan=3, sticky=E+W+S+N)    
        
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c +1)).grid(row=13, column=c, sticky=E+W)
        
root = Tk()
app = Application(master=root)
app.mainloop()