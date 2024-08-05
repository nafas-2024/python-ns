def fibonachi(x):
    fib1=0                                         
    fib2=1
    fib=0
    
    print(fib1,fib2,sep="\n")                          # در ابتدا 0 و 1 راچاپ کن
    while fib<x :                                      #از عدد وارد شده کمتر باشد عملیات زیر را اجرا کن fib تا زمانی که  
        fib=fib1+fib2                                 
        fib1=fib2
        fib2=fib
        if fib<x:
            print(fib)
    return (f"they make {x}")
num=int(input("enter :"))
print(fibonachi(num))