n=int(input("enter a number:"))                    #عددی را از کاربر بگیر
m=1

for a in range(1,n+1) :                            #اعداد 1 تا عددی که کاربر وارد کرده را نشان بده
    m*=a                                           #1 را در اعداد بین 1 تا عددوارد شده ضرب کن
    print(f"{a}! = {m}")
    
    