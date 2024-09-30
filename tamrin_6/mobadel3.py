from tkinter import*
from tkinter import ttk, messagebox
root=Tk()
root.title("coverter")
root.geometry("450x200")

def tabdil():
    """This is the function that converts your units
    """
    texts=""
    entr=ent.get()
    c=combo_1.get()
    c2=combo_2.get()
    
    if c=="mm" and c2=="cm":
        cm=int(entr)/100
        texts=cm,"cm"
    elif c=="cm" and c2=="mm":
        m=int(entr)*100
        texts=m,"mm"
    elif c=="mm"and c2=="m":
        m=int(entr)/1000
        texts=m,"m"
    elif c=="m" and c2=="mm":
        mm=int(entr)*1000
        texts=mm,"mm"
    elif c=="m" and c2==cm:
        cm=int(entr)*100
        texts=cm,"cm"
    elif c=="cm" and c2=="m":
        cm=int(entr)/100
        texts=cm,"m"
    else:
        messagebox.showerror("invalid items", "you chose wrong items")
    
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" convert from : ")
lbl.place(x=0, y=0)
combo_1=ttk.Combobox(root, values=["mm", "cm", "m"])
combo_1.place(x=85, y=0)
lbl=Label(root, text=" to : ")
lbl.place(x=250, y=0)
combo_2=ttk.Combobox(root, values=["mm", "cm", "m"])
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