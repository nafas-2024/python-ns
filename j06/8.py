l1=[]
l2=[]

for i in range(1,101):
    if i % 2 ==0 :
        l1.append(i)
    elif i % 2 !=0 :
        l2.append(i)
print("Even numbers from 1 to 100 : " , l1 , end="\n\n")
print("Odd numbers from 1 to 100" , l2 , end="\n")
