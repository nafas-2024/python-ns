from tkinter import *

root = Tk()

root.title("Paint")
root.geometry("500x500")

color_win= "white"

def paint(window):
    global color_win
    x1, y1 = (window.x-3), (window.y-3)
    x2, y2 = (window.x+5), (window.y+5)
    wn.create_oval(x1, y1, x2, y2, fill=color_win, outline=color_win)
            
wn = Canvas(root, width=500, height=350)
wn.bind('<B1-Motion>', paint)
wn.pack()


def color_w():
    
    v=var.get()
    if v==1:
        wn.config(bg="black")
    elif v==2:
        wn.config(bg="white")
    elif v==3:
        wn.config(bg="blue")
        
def color_p():
    global color_win
    v=var2.get()
    if v==4:
        color_win="black"
    elif v==5:
        color_win="white"
    elif v==6:
        color_win="red"
  
        
def create_l():
    global color_win
    v=var.get()
    
    wn.create_line(100, 100, 10, 10, fill=color_win )

def create_c():
    global color_win
    v=var.get()
    
    wn.create_oval(175, 100, 100, 175, width = 3, fill=color_win, outline=color_win)

def create_r():
    global color_win
    v=var.get()
    
    wn.create_rectangle(100, 15, 200, 65, fill=color_win, outline=color_win)
   
var=IntVar()
r1=Radiobutton(root, text="black", variable=var, value=1 , command=color_w)
r1.place(x=20, y=363)
r2=Radiobutton(root, text="white", variable=var, value=2 , command=color_w)
r2.place(x=20, y=383)
r3=Radiobutton(root, text="blue", variable=var, value=3, command=color_w)
r3.place(x=20, y=403)

btn1=Button(root, text="line", command=create_l, width=15)
btn1.place (x=120 , y=383)
btn2=Button(root, text="circle", command=create_c, width=15)
btn2.place (x=120 , y=413)
btn2=Button(root, text="rectangle", command=create_r, width=15)
btn2.place (x=120 , y=443)

var2=IntVar()
rp1=Radiobutton(root, text="black", variable=var2 , value=4, command=color_p)
rp1.place(x=250 , y=383)
rp2=Radiobutton(root, text="white", variable=var2 , value=5 , command=color_p)
rp2.place(x=250 , y=413)
rp3=Radiobutton(root, text="red", variable=var2 , value=6 , command=color_p)
rp3.place(x=250 , y=443)


root.mainloop()