count=0
b="c"
while b=="c" :                           #حلقه را تا زمانی که درست است ادانه بده
    if count==0 :
       n1=int(input("enter a number : "))
       op=input("enter an op (+ or - or * or /) : ")
       n2=int(input("enter another number : "))               #عدد اول  ، عمل ریاضی و عدد دوم را وارد کنید تا عملیات زیر صورت گیرد
    else :
        op=input("enter an op : ")
        n1=int(input("enter a number : "))
        n2=result
    
    if op=="+" :
        result=n1+n2                          
    elif op=="*" :
        result=n1*n2
    elif op=="-" :
        if count==0:
            result=n1-n2
        else :
            result=n2-n1
    elif op=="/" :
        if count==0 :
            if n2==0 :
                print("can not divid by zero!")#اگر عدد دوم برابر با 0 بود عبارت روبرو را چاپ کن 
                continue
            result=n1/n2
        else :
            if n1==0 :
                print("invalid input")
                continue
            result=n1/n2
    print("answer= " , result)
    count+=1
    b=input("enter *finish* for break ' if you do not want to break click enter :") 
    if b=="finish":
        print("break.")
        break
    