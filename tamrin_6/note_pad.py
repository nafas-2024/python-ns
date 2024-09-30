from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("All Files", "*.*")])
    
    if not filepath:
        return
    
    txt_edit.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(filetypes=[("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

# GUI window
root = Tk()
root.title("Note_pad")
# create a menu
menu =Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)

menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_cascade(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

txt_edit = Text(root, width=30, height=20)
txt_edit.place(x=14, y=23)


root.mainloop()
