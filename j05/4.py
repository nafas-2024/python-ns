while 1 :                           #حلقه را تا زمانی که درست است ادانه بده

    n1=int(input("enter a number : "))
    op=input("enter an op (+ or - or * or /) : ")
    n2=int(input("enter another number : "))               #عدد اول  ، عمل ریاضی و عدد دوم را وارد کنید تا عملیات زیر صورت گیرد

    if op=="+" :
        print(n1+n2)
    elif op=="-" :
        print(n1-n2)
    elif op=="*" :
        print(n1*n2)
    elif op=="/" :
        if n2==0 :
            print("can not divid by zero!")               #اگر عدد دوم برابر با 0 بود عبارت روبرو را چاپ کن 
    else :
        print(n1/n2)                                      # در غیر این صورت عدد اول و دوم را چاپ کن
    
    d=input("enter *finish* for break ' if you do not want to break click enter' :") 
    if d=="finish":
        print("break.")
        break