from tkinter import*

class calcu(Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry("300x350")
        # create an entry 
        self.result=Entry(self, width=15, font=("Arial", 20))
        self.result.grid(row=0, column=0, columnspan=2, padx=5, pady=5, ipadx=20, ipady=10, sticky=W+E)
        # create a from for claculator buttons
        btn_frame=Frame(self)
        btn_frame.grid(row=1 , column=0, columnspan=4 , padx=10, pady=10)
        # create buttons for calculator
        self.creat_button("1", btn_frame, 0,0,lambda: self.add_number(1))
        self.creat_button("2", btn_frame, 0,1,lambda: self.add_number(2))
        self.creat_button("3", btn_frame, 0,2,lambda: self.add_number(3))
        self.creat_button("4", btn_frame, 1,0,lambda: self.add_number(4))
        self.creat_button("5", btn_frame, 1,1,lambda: self.add_number(5))
        self.creat_button("6", btn_frame, 1,2,lambda: self.add_number(6))
        self.creat_button("7", btn_frame, 2,0,lambda: self.add_number(7))
        self.creat_button("8", btn_frame, 2,1,lambda: self.add_number(8))
        self.creat_button("9", btn_frame, 2,2,lambda: self.add_number(9))
        self.creat_button("0", btn_frame, 3,1,lambda: self.add_number(0))
        self.creat_button("+", btn_frame, 0,3,lambda: self.add_operation("+"))
        self.creat_button("-", btn_frame, 1,3,lambda: self.add_operation("-"))
        self.creat_button("*", btn_frame, 2,3,lambda: self.add_operation("*"))
        self.creat_button("/", btn_frame, 3,3,lambda: self.add_operation("/"))
        self.creat_button("=", btn_frame, 3,2,lambda: self.calculate())
        self.creat_button("c", btn_frame, 3,0,lambda: self.clear("c"))
        
    def creat_button(self, text, frame, r, c, command):
        """this is a function for create calculator buttons
        Args:
            text (str): button's name
            frame ((frame)variable): 
            r (int): 
            c (int): 
            command (method): what should this function do
        """
        btn= Button(frame, text=text, command=command , font=("Arial", 10), width=3, height=2)    
        btn.grid(row=r , column=c, padx=10, pady=10)
            
    def add_number(self, kind):
        current = self.result.get()
        current += str(kind)
        self.result.delete(0 ,END)
        self.result.insert(0, current)
    def add_operation(self, op):
        current = self.result.get()
        current += str(op)
        self.result.delete(0 ,END)
        self.result.insert(0, current)
    def calculate(self):
        current= self.result.get()
        self.result.delete(0,END)
        self.result.insert(0, eval(current))
    def clear(self):
        self.result.delete(0, END)

calculate=calcu()
calculate.mainloop()