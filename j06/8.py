l1=[]
l2=[]

for i in range(1,101):         #در بازه ی 1 تا 100 i برای 
    if i % 2 ==0 :               #اگر اعدادی که از 1 تا 100 زوج بودند
        l1.append(i)             #آنها را به آخر لیست 1 اضافه کن
    elif i % 2 !=0 :             #اگر اعدادی که از 1 تا 100 فرد بودند
        l2.append(i)             # آنها را به آخر لیست 2 اضافه کن
print("Even numbers from 1 to 100 : " , l1 , end="\n\n")
print("Odd numbers from 1 to 100" , l2 , end="\n")
