from tkinter import*
from tkinter import messagebox
from random import randint as r
rand=r(10,100)

def game ():
    """This is a function that takes the number you guessed, 
    checks if the number you guessed is the same as the number 
    that computer chose, and puts the answer in a message box.
    """
    texts=""
    entr=ent.get()
    
    if int(entr)== rand:
        texts="Your guss was true"
    elif int(entr)< rand:
        texts=f"Your guess was smaller than computer's number . \n Number was :{rand}"
    if int(entr)> rand:
        texts=f"Your guess was bigger than computer's number .\n Number was : {rand}"
    
    m=messagebox.showinfo("result", texts)

root =Tk()
root.title("hads adad")
root.geometry("381x389")
# getting user's guess
lbl=Label(root, text=" Enter that number you guess between  10 and 100 :")
lbl.pack()
ent=Entry(root, width=10)
ent.pack()
# button for show result of game
btn=Button(root, text="Play", command=game)
btn.pack()

root . mainloop()