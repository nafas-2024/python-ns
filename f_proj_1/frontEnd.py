from tkinter import *
from tkinter import ttk, messagebox
from backEnd import Back_End

backend=Back_End()

def selecting(passi):
    global g
    global selected_c
    # selecting an item and get it 
    selected_c = commodity_box.curselection()
    g=commodity_box.get(selected_c)
    # delete every things in entries whit selecting
    name_ent.delete(0, END)
    p_price_ent.delete(0, END)
    s_price_ent.delete(0, END)
    number_ent.delete(0, END)
    # add infos in entries with selecting
    name_ent.insert(END, g[1])
    p_price_ent.insert(END, g[2])
    s_price_ent.insert(END, g[3])
    number_ent.insert(END, g[4])

def loading():
    # delete every things from commodity list
    commodity_box.delete(0, END)
    # add every infos from database to commodity box
    for row in backend.cursor.execute("SELECT * FROM commodities"):
        commodity_box.insert(END, row)

def add_c():   
    """This is a function that takes four entry for commodity's name , 
    its purchase price , its selling price and the number of commodity.
    The it add them to the list box of commodities and
    save them to the database.
    """ 
    # getting entries
    n=name_ent.get()
    p=p_price_ent.get()
    s=s_price_ent.get()
    num=number_ent.get()
    # save entries in a list
    all_info=[n, p, s, num]
    # if all the entries were fill
    if len(n)>0 and len(p)>0 and len(s)>0 and len(num)>0:
        # add infos to database
        backend.add_commodity(n, p, s, num,)
        # add infos to list of commodities
        commodity_box.delete(0, END)
        commodity_box.insert(END, all_info)
        name_ent.delete(0,END)
        p_price_ent.delete(0, END)
        s_price_ent.delete(0, END)
        number_ent.delete(0, END)
        loading()
    # if at least one of the entries was empty , show "Empty error"
    else:
        messagebox.showerror("Empty error", "Entries are empty")
        
def searching():
    """This is a function that you fill ina at least one of the entries 
    and click the "search" button and it will show you 
    any item whith that name or value.
    """
    # delet every thigs in list box and ready for searching 
    commodity_box.delete(0, END)
    # getting entries
    n=name_ent.get()
    p=p_price_ent.get()
    s=s_price_ent.get()
    num=number_ent.get()
    
    for row in backend.search_c(n, p, s, num):
        # insert your search result at the list box
        commodity_box.insert(END, row)

def edit():
    selected = commodity_box.curselection()
    # if an item was select
    if selected:
        backend.edit(g[0],name_ent.get(), p_price_ent.get(), s_price_ent.get(), number_ent.get())
    
        loading()
    else: 
        messagebox.showerror("Not select", 
        "you can't edit an item without selecting. \n Please select an item from commodity list")
    
    
def deleteing():
    # select from commodity box
    selected = commodity_box.curselection()
    # if an item was select
    if selected:
        # delete that item from database
        backend.clear(g[0])
        # than delete all in entries
        name_ent.delete(0,END)
        p_price_ent.delete(0, END)
        s_price_ent.delete(0, END)
        number_ent.delete(0, END)
        loading()
    # if not selecting
    else:
        messagebox.showerror("Not select", 
        "you can't delete an item without selecting. \n Please select an item from commodity list")
    
# create GUI window
root =Tk()
root.title("Super_Management")
root.geometry("500x300")
root.config(bg="#800000")
# getting the name of commodity
name_lbl=Label(root , text="نام کالا", bg="#800000", fg="white")
name_lbl.place(x=25, y=10)
n_var=StringVar()
name_ent=Entry(root , textvariable=n_var, width=20, bg="#cb8777")
name_ent.place(x=100, y=10)
# getting purchsase price
p_price_lbl=Label(root , text="قیمت خرید", bg="#800000", fg="white")
p_price_lbl.place(x=250, y=10)
p_var=StringVar()
p_price_ent=Entry(root , textvariable=p_var, width=20, bg="#cb8777")
p_price_ent.place(x=325, y=10)
# getting selling price
s_price_lbl=Label(root , text="قیمت فروش", bg="#800000", fg="white")
s_price_lbl.place(x=10, y=35)
s_var=StringVar()
s_price_ent=Entry(root , textvariable=s_var, width=20, bg="#cb8777")
s_price_ent.place(x=100, y=35)
# getting the number of commodity
number_lbl=Label(root , text="تعداد", bg="#800000", fg="white")
number_lbl.place(x=265, y=35)
num_var=StringVar()
number_ent=Entry(root , textvariable=num_var, width=20, bg="#cb8777")
number_ent.place(x=325, y=35)
# button for add commodity
add_btn=Button(root , text="اضافه کردن", width=15, command=add_c, bg="#9b3228")
add_btn.place(x=328, y=70)
# button to selch commodities
search_btn=Button(root , text="جستجوی کالا", width=15, command=searching, bg="#b4604e")
search_btn.place(x=328, y=100)
# button to delete a commodity
add_btn=Button(root , text="حذف کالا", width=15, command=deleteing, bg="#cb8777")
add_btn.place(x=328, y=130)
# button to edit datas
add_btn=Button(root , text="ویرایش", width=15, command=edit, bg="#dfaea3")
add_btn.place(x=328, y=160)
# button to close the program
add_btn=Button(root , text="بستن", width=15, command=exit, bg="#f0b6b0")
add_btn.place(x=328, y=190)
# create a list box
commodity_box=Listbox(root , width=40, height=10, bg="#cb8777")
commodity_box.place(x=20, y=70)
# selecting an item of commodity_box
commodity_box.bind("<<ListboxSelect>>", selecting)

scrollbar=ttk.Scrollbar(root, command=commodity_box.yview )
scrollbar.place(x=280, y=120)


loading()

root.mainloop()
backend.conn.close()