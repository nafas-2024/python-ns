from random import randint as r

n1=int(input("enter a number for start range : "))
n2=int(input("enter a number for stop range : "))

rand=r (n1,n2)

for _ in range(5):
    
    num=int(input("enter the number you guess :")) 
    if num==rand :                                            #if num equal the number that camputer choose, print this
        print("your guess was true")
        break
    elif num<rand :                                           #if num smaler than the number that camputer choose, print this
        print("your guess wos smaler than the number!")
    elif num>rand :                                           #if num bigger than the number that camputer choose, print this
        print("your guess was bigger than the number!")

print ("done...")

print (f"the number was \"{rand}\"")