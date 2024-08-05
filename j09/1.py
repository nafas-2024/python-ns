def sums(x,y) :
    
    return x+y        #عدد اول و دوم را به صورت جمع برگردان

def subs(x,y):
    
    return x-y

def mult(x,y):
    
    return x*y

def divid(x,y):
    if y==0:                    #اگر عدد دوم برار با صفر بود عبارت زیر را چاپ کن
        print("can not divid by zero !")
    else:
        
        return x/y    #در غیر این صورت عدد اول و دوم را بر هم تقسیم کن

n1=int(input("enter a number : "))
op=input("enter an op (+ or - or * or /) : ")
n2=int(input("enter another number : "))      


if op=="+":
    print(sums(n1,n2))
elif op=="-":
    print(subs(n1,n2))
elif op=="*":
    print(mult(n1,n2))
elif op=="/":
    print(divid(n1,n2))