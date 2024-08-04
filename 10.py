def difit(a,b=0):
    if a<10:               #را بر گردان a اگر عدد اول از 10 کوچک تر بود 
        return a+b
    
    return difit(a//10,a%10+b)

n=int(input())
print((difit(difit(difit(n)))))
