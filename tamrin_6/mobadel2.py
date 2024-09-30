from tkinter import*
from tkinter import ttk, messagebox
root=Tk()
root.title("money converter")
root.geometry("450x200")

def tabdil():
    """This is the function that does your conversions
    """
    texts=""
    entr=ent.get()
    c=combo_1.get()
    c2=combo_2.get()
    
    if c=="dollar" and c2=="toman":
        toman=int(entr)*60000
        texts=toman, "تومن"
    elif c=="toman"and c2=="dollar":
        dollar=int(entr)/60000
        texts=dollar , "$"
    elif c=="toman" and c2=="rial":
        rial=int(entr)*10
        texts=rial, "ريال"
    elif c=="dollar" and  c2=="rial":
        rial=int(entr)*600000
        texts=rial, "ريال"
    elif c=="rial" and c2=="dollar":
        dollar=int(entr)*10
        texts=dollar, "$"
    elif c=="rial" and c2=="toman":
        toman=int(entr)/600000
        texts=toman, "تومن"
    else:
        messagebox.showerror("invalid items", "you chose wrong items")
        
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" convert from : ")
lbl.place(x=0, y=0)
combo_1=ttk.Combobox(root, values=["dollar", "toman", "rial"])
combo_1.place(x=85, y=0)
lbl=Label(root, text=" to : ")
lbl.place(x=250, y=0)
combo_2=ttk.Combobox(root, values=["dollar", "toman", "rial"])
combo_2.place(x=300, y=0)

# getting entry
lbl=Label(root, text=" your amount : ")
lbl.place(x=0, y=30)
ent=Entry(root, width=10)
ent.place(x=100, y=32)
# creating button
btn=Button(root, text="change ", command=tabdil)
btn.pack(pady=30)

root.mainloop()