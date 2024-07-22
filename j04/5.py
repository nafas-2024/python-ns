n=int(input("enter anumber :"))                 #عددی را که رابطه ی فیبوناچی آن را می خاهید وارد کنید

fib1=0                                          
fib2=1
fib=0
    
if n<1:                                        #اگر عدد وارد شده از 1 کوچک تر بود جمله ی زیر را چاپ کن
    print("your number is not true ! try again...")


print(fib1,fib2,sep="\n")                          # در ابتدا 0 و 1 راچاپ کن
while fib<n :                                      #از عدد وارد شده کمتر باشد عملیات زیر را اجرا کن fib تا زمانی که  
    fib=fib1+fib2                                 
    fib1=fib2
    fib2=fib
    
    print(fib)                                  
        
