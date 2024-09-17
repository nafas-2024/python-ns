from tkinter import*
from datetime import datetime

root=Tk()
root.title("Alarm")
root.geometry("450x200")

def alarmm():
    entr=ent.get()
    hours=entr[0:2]
    minutes=entr[3:5]
    while 1:
        now=datetime.now()    
        c_h=now.strftime("%H")
        c_m=now.strftime("%M")
        if hours==c_h and minutes==c_m:
            lbl=Label(root, text="pashoooo")
            lbl.pack()    
            break
ent=Entry(root, width= 10)
ent.pack()
btn=Button(root , text="start", command=alarmm)
btn.pack()
root.mainloop()