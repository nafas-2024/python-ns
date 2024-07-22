for _ in range(3):
    
    num=int(input("enter the number >10 and <100 you guess :")) 
    if num==50 :                                            #if num equal 50 print this
        print("your guess was true")
        break
    elif num<50 :                                           #if num smaler than 50 print this
        print("your guess wos smaler than the number!")
    elif num>50 :                                           #if num bigger than 50 print this
        print("your guess was bigger than the number!")

print ("done...")