from tkinter import*
from tkinter import messagebox
from datetime import datetime

root=Tk()
root.title("Alarm")
root.geometry("300x200")
root.config(bg="black")

def alarmm():
    """this function gets hour and minute and if 
    the computer time == your time it sed a message to you
    """
    entr=ent.get()
    entr2=ent_2.get()
    hours=entr
    minutes=entr2
    # 
    if int(entr)> 23 or int(entr2) > 59 or int(entr)<00 or int(entr2) <00:
        mess=messagebox.showerror("invalid time",
        "you entered a wrong time \n Hour should between 00 to 23 \n Minute shold between 00 to 59 ")
        
    else:
        while 1:
            now=datetime.now()    
            c_h=now.strftime("%H")
            c_m=now.strftime("%M")
            if hours==c_h and minutes==c_m:
                mess_w=messagebox.showinfo("Alarm",f"wake up \n it's  {entr} : {entr2}")
                break



lbl_h=Label(root, text="Hour", bg="black", fg="white")
lbl_h.place(x=65, y=10)
lbl_m=Label(root, text="Minute", bg="black", fg="white")
lbl_m.place(x=110, y=10)
# getting time
ent=Entry(root, width= 5)
ent.place(x=70 , y=40)
ent_2=Entry(root , width=5)
ent_2.place(x=110 , y=40)
# creating button for starting alarm
btn=Button(root , text="start", command=alarmm)
btn.place(x=90, y=80)

root.mainloop()