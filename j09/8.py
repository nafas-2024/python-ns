def pythagoras(n,s,h):         #تابعی که سه تا ورودی می گیرد
    no="No"
    if n**2+s**2==h**2 or h**2+s**2==n**2 or h**2+n**2==s**2:              #Yes اگر جمع مجذور دو عدد با مجذور عدد سوم مساوی باشد بگو
        no="Yes"
    return no

n1=int(input())
n2=int(input())
n3=int(input())

print(pythagoras(n1,n2,n3))            #سه تا ورودی دریافت کن و در تابع جایگذاری کن