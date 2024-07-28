t1=[]
for i in range(5):                  #در بازه ی 5 بار iبرای 
    n=int(input("enter : "))
    t1.append(n)                    #اضافه کن t1 را به آخر  n

t1.sort()                             #قرار دارد را به تر تیب بچین t1 هرچه در داخل 
print(t1)
t1.sort(reverse=True)                  #قرار دارد را به تر تیب برعکس بچین t1 هرچه در داخل 
print(t1)