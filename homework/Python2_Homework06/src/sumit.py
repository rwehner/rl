from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        main_frame = Frame()
        
        self.num1 = Entry(main_frame)
        self.num1.pack()
        
        self.num2 = Entry(main_frame)
        self.num2.pack()
        
        self.result = Label(main_frame, text="Result")
        self.result.pack()
        
        main_frame.pack(side=TOP)
        
        bottom_frame = Frame()
                
        self.SUM = Button(bottom_frame, text="Sum the numbers", command=self.handle_sum)
        self.SUM.pack(side=LEFT)
        
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=RIGHT)
        
        bottom_frame.pack(side=TOP)
        
    def handle_sum(self):
        result = None
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
        except ValueError:
            result = "***ERROR***"
            
        if not result:
            result = num1 + num2
            
        self.result.config(text=result)
        
root = Tk()
app = Application(master=root)
app.mainloop()