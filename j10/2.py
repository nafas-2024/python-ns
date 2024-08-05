from random import choice as ch

types=("rock","paper","scissors")

user_1=0              #مقدار بازی هایی که کابر برده
camputer=0              #مقدار بازیهایی که کامپیوتر برده
equals=0                #مقدار برابری ها

for i in range(5):
    choice=ch(types)
    user=input("enter a type of \"rock\" or \"paper\" or \"scissors\" :")
    print("camputer choiced : ",choice)
    
    if user==choice :
        print("equal")                             #اگر گزینه ی انتخابی توسط کامپیوتر و کاربر یکی بود به امتاز برابری ها اضافه کن
        equals+=1
    elif user=="rock" and choice=="paper":
        print("camputer won")
        camputer+=1
    elif user=="paper" and choice=="rock":
        print("you won")
        user_1+=1
    elif user=="rock" and choice=="scissors":
     print("you won")
     user_1+=1
    elif user=="scissors" and choice=="rock":
      d=print("camputer won")
      camputer+=1
    elif user=="scissors" and choice=="paper":
     print("you won")
     camputer+=1
    elif  user=="paper" and choice=="scissors":
     print("camputer won")
     camputer+=1
    else :                           
     print("not correct")       
     
print(f"you are :{user_1} and camputer is : {camputer} and you have {equals} time(s) equal ")