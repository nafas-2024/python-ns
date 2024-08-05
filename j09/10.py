def difit(a,b=0):
    if a<10:
        return a+b
    else:
        return difit(a//10,a%10+b)

n=int(input())
print(difit(difit(difit(n))))