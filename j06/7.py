l1=[ "nafas", "zahra","raha",12, 13, 14]
l2=[]
l3=[]

for i in range(0,len(l1)):        #برای مقداری در بازه ی 0 تا تعداد کاراکتر لیست 1
    if i % 2 == 0 :             
        l2.append(l1[i])         #بر2 بخش پذیر بود در لیست 2 بذار i اگر 
    else :
        l3.append(l1[i])          #در غیر این صورت در لیست 3 بذار
print(l2)
print(l3)