from tkinter import*
from tkinter import ttk
root=Tk()
root.title("mobadel pool")
root.geometry("450x200")

def tabdil():
    """This is the function that does your conversions
    """
    texts=""
    entr=ent.get()
    c=combo.get()
    
    if c=="c_f":
        f=int(entr)*1.8+32
        texts=f , "f"
    if c=="f_c":
        c=(int(entr)-32)/1.8
        texts=c, "c"
    if c=="c_kel":
        kel=int(entr)+273.15
        texts=kel, "kel"
    if c=="kel_c":
        c=int(entr)-273.15
        texts=c , "c"
    
        
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" select the conversion typ : ")
lbl.place(x=0, y=0)
combo=ttk.Combobox(root, values=["c_f", "f_c", "kel_c", "c_kel"])
combo.pack()

# getting entry
lbl=Label(root, text=" your amount : ")
lbl.pack()
ent=Entry(root, width=10)
ent.pack()
# creating button
btn=Button(root, text="change ", command=tabdil)
btn.pack()

root.mainloop()