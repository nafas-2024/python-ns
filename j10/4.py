from random import choice as ch

lst=["account","acid","across","act","addition","adjustment","advertisement","after","again","against","agreement",
     "air","all","almost","among","amount","amusement","and","angle","angry","animal","answer","ant","any"]

choic=ch(lst)          #کامپیوتر از این لیست یکی را انتخاب کرده
lenn=len(choic)        #کلمه ای که کامپیوترانتخاب کرده چند کاراکتر است

print(f"the word you should guess has {lenn} letter")

for i in range (lenn) :
    user_choice=input("enter the word you guess : ")
    
     if user_choice==choic:          #اگر چیزی که کاربر وارد کرده با انتخاب کامپیوتر برابر بود
        print("you won")
        break
     if user_choice != choic:              #اگر هیچ کدام از حدس های کابر درست نبود عبارت زیر را چاپ کن
          print (f"you lose !!! the word was : {choic}")

"""
from random import choice as ch

lst = [
    "account",
    "acid",
    "across",
    "act",
    "addition",
    "adjustment",
    "advertisement",
    "after",
    "again",
    "against",
    "agreement",
    "air",
    "all",
    "almost",
    "among",
    "amount",
    "amusement",
    "and",
    "angle",
    "angry",
    "animal",
    "answer",
    "ant",
    "any",
]

choic = ch(lst)  # کامپیوتر از این لیست یکی را انتخاب کرده
lenn = len(choic)  # کلمه ای که کامپیوترانتخاب کرده چند کاراکتر است

print(f"the word you should guess has {lenn} letter")

for i in range(0, lenn):
    u_choice = input(f"enter choice {lenn - i}: ")
    if lenn == 0:
        break
    if len(u_choice) != len(choic):
        print("invalid input")
    if u_choice == choic:
        print("you win...")
        break
    else:
        if (lenn - i) > 1:
            print("try again")
else:
    print("game over...", f"correct word is {choic}", sep = "\n")
"""
