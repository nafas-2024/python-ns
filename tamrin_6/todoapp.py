from tkinter import *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect("todo app.db")
# handing sql
cursor = conn.cursor()
# creating a table for tasks
cursor.execute(
    """CREATE TABLE IF NOT EXISTS tasks (task_id INTEGER PRIMARY KEY, task TEXT)""")

def load_tasks():
    """delete everythings at the 
    listbox and starting operations
    """
    lstbox.delete(0, END)
    for row in cursor.execute("SELECT * FROM tasks"):
        lstbox.insert(END, row[1])
        
def add_task():
    """it is a function that takes task 
        of entry and put it in the list box
    """
    task = task_entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        task_entry.delete(0, END)
        load_tasks()
    else:
        messagebox.showerror("Add error", "Task is empty")

def delete_task():
    """this function delete 
        that option you select it 
    """
    try:
        selected_task = lstbox.get(lstbox.curselection())
        cursor.execute("DELETE FROM tasks WHERE task = ?", (selected_task,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Delete error", "Cannot delet a task without selecting")


root = Tk()
root.title("ToDo APP")
root.geometry("320x350")
# getting tasks
task_entry = Entry(root, width=30)
task_entry.place(x=20, y=10)
# button to adding tasks
btn_add = Button(root, text="Add Task", command=add_task, background="blue", width=10)
btn_add.place(x=150, y=40)
# button to delete the selected task
delete_task_btn = Button(root, text="Delete Task", command=delete_task, bg="crimson", width=10)
delete_task_btn.place(x=50, y=40)

lstbox = Listbox(root, width=45, height=13)
lstbox.place(x=10, y=80)

load_tasks()

root.mainloop()
conn.close()