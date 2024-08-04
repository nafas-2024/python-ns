def prime_number(x):
    if x<2:
        return False              #اگر عدد وارد شده کمتر از 2 بود به صورت غلط برگردان
   
    for i in range(2,int(x**0.5)+1):           
        if x%i==0:
            return False          #برابر با صفر بود به صورت غلط چاپ کن i اگر باقی مانده ی عدد وارد شده بر 
        return True
            
            
n=int(input(" enter a number : "))
if prime_number(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")