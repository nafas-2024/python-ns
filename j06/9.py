n1=int(input("enter a number for start : "))
n2=int(input("enter a number for stop : "))
l1=[]

for i in range (n1,n2+1) :                       
    if i % 15 == 0:                     #هست بر 15 بخش پذیر بود i اگر مقداری که در 
        l1.append(i)                     #را به آخر لیست 1 اضافه کن i مقدار درون 
print("numbers that are divisile by 15 in this range : ",l1 , sep="\n" , end="\n\n")
print("count of numbers divisible by 15 : " , len(l1) )