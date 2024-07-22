a=int(input("1_enter the two digit number you guess :"))
b=int(input("2_enter the two digit number you guess :"))
c=int(input("3_enter the two digit number you guess :"))

if a and b and c %10 :
    while a==50 :                      #ta zamani ke a=50
     print("your first guess is true") #if a = 50 print this
     break 
    while b==50 :                      #ta zamani ke b=50
     print("your secend guess is true")#if b = 50 print this
     break 
    while c==50 :                     #ta zamani ke c=50
     print("your third guess is true")#if c = 50 print this
     break
    
    

elif a or b or c !=50 :
     print("your guesses are not true")

print("done")