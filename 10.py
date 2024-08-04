def difit(a:int,b:int=0):
    if a<10:
        return a+b
    
    return difit(a//10,a%10+b)

n=int(input())
print((difit(difit(difit(n)))))