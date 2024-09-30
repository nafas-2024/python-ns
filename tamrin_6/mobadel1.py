from tkinter import*
from tkinter import ttk , messagebox
root=Tk()
root.title("degree converter")
root.geometry("450x200")

def tabdil():
    """This is the function that does your conversions
    """
    texts=""
    entr=ent.get()
    c=combo_1.get()
    c2=combo_2.get()
    
    if c=="cant"and c2=="far":
        f=int(entr)*1.8+32
        texts=f , "f"
    elif c=="far" and c2=="cant":
        c=(int(entr)-32)/1.8
        texts=c, "c"
    elif c=="cant" and c2=="kel":
        kel=int(entr)+273.15
        texts=kel, "kel"
    elif c=="kel" and c2=="cant":
        c=int(entr)-273.15
        texts=c , "c"
    else:
        messagebox.showerror("invalid items", "you chose wrong items")
        
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" convert from : ")
lbl.place(x=0, y=0)
combo_1=ttk.Combobox(root, values=["far", "cant", "kel"])
combo_1.place(x=85, y=0)
lbl=Label(root, text=" to : ")
lbl.place(x=250, y=0)
combo_2=ttk.Combobox(root, values=["far", "cant", "kel"])
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