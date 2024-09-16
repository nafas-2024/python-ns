from tkinter import*
from tkinter import ttk , messagebox
from random import choice as ch
lst=["rock" , "paper" , "scissors"]
computer_choice=ch(lst)
player_choice="rock"

def game():
    """it is a function for shows messagebox
    """    
    texts=""
    if (
        (player_choice=="rock" and computer_choice=="scissors")
        or( player_choice=="paper" and computer_choice=="rock") 
        or (player_choice=="scissors" and computer_choice=="paper")
        ):
        texts=f"You win ! Computer chose {computer_choice}"
        
    elif player_choice==computer_choice:
        texts=f"Equal ! You and computer chose {computer_choice}"
    else:
        texts=f"You lose ! Computer chose {computer_choice}"
  
    m=messagebox.showinfo("result", texts)

# Creating a window
root=Tk()
root.title("rock_paper_scissors")
root.geometry("381x389")

# Creating Lable
lbl=Label(root, text="Choose your move : ").pack(pady=10)

# Combobox for choose 
choice=["rock", "paper" ,"scissors"]
combo=ttk.Combobox(root , values= choice , state="readonly" ).pack(pady=5)

# Button for Play
btn=Button(root, text="play", command=game).pack(pady=10)

root.mainloop()