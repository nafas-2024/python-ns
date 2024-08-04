l=[]
l2=[]
def separator(ls):
    if ls%2==0:
        l.append(ls)       # اضافه کن l اگر  عدد وارد شده بر 2 بخش پذیر بود به لیست 
    else:
        l2.append(ls)      

while 1:
    num=input()            #عددی را می گیرد
    if num=='':
        break               #زد حلقه را بشکن enter اگر کاربر 
    else:
        n=int(num)
        separator(n) 


l3=[]
l3.append(l)
l3.append(l2)
a=tuple(l3)
print(a)