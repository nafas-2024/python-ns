m=input("enter : ")
print(eval(m))


n1=int(input("enter a number : "))
op=input("enter an op (+ or - or * or /) : ")
n2=int(input("enter another number : "))      
if op=="+" :
   print(n1+n2)
elif op=="-" :
    print(n1-n2)
elif op=="*" :
    print(n1*n2)
elif op=="/" :
        if n2==0 :
            print("can not divid by zero!")               
else :
    print(n1/n2)  
