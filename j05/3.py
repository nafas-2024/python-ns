n1=0
n2=0                                               
print("when you enter 0 we show you average . ")
while 1:                                          
    i=int(input("enter a number : "))
    if i==0 :                                            #اگر عدد وارد شده برابر با 0 بود تکرار واردکردن عدد را قطع کن
        break
    n1+=i                                                # را بعلاوه ی مقدار وارد شده کنn1مقدار درون 
    n2+=1                                                #را بعلاوه ی یک کن n2 مقدار درون 
print("variable: ", n1/n2)

