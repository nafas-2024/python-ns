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
    
    if c=="dollar_toman":
        toman=int(entr)*60000
        texts=toman
    else:
        dollar=int(entr)/60000
        texts=dollar
        
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" select the conversion typ : ")
lbl.place(x=0, y=0)
combo=ttk.Combobox(root, values=["dollar_toman", "toman _dollar"])
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