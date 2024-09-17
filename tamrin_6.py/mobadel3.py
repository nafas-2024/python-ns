from tkinter import*
from tkinter import ttk
root=Tk()
root.title("mobadel vahed")
root.geometry("450x200")

def tabdil():
    """This is the function that converts your units
    """
    texts=""
    entr=ent.get()
    c=combo.get()
    
    if c=="mm_cm":
        cm=int(entr)/100
        texts=cm,"cm"
    if c=="cm_mm":
        m=int(entr)*100
        texts=m,"mm"
    if c=="mm_m":
        m=int(entr)/1000
        texts=m,"m"
    if c=="m_mm":
        mm=int(entr)*1000
        texts=mm,"mm"
    if c=="m_cm":
        cm=int(entr)*100
        texts=cm,"cm"
    if c=="cm_m":
        cm=int(entr)/100
        texts=cm,"m"
    
    label=Label(root, text=texts)
    label.pack()

# creating combo box
lbl=Label(root, text=" select the conversion typ : ")
lbl.place(x=0, y=0)
combo=ttk.Combobox(root, values=["mm_cm", "cm_mm", "cm_m", "m_cm", "mm_m", "m_mm"])
combo.pack()

# getting entry
lbl=Label(root, text=" your number for change : ")
lbl.pack()
ent=Entry(root, width=10)
ent.pack()
# creating button
btn=Button(root, text="change ", command=tabdil)
btn.pack()

root.mainloop()