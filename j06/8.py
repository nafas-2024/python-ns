l1=[]
l2=[]

for i in range(1,101):
    if i % 2 ==0 :                 #اگر اعداد بین یک تا 100 زوج بود
        l1.append(i)               #آن را به آخر لیست 1اضافه کن
    else :
        l2.append(i)              #در غیر این صورت به آخر لیست 2 اضافه کن
print("Even numbers from 1 to 100 : " , l1 , end="\n\n")
print("Odd numbers from 1 to 100" , l2 , end="\n")
