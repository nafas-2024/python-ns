def prime_2(x) :

    n=0
    for i in range(2,x):         #برای یک چیزی در بازه ی 2 تا عدد وارد شده
        if x%i==0:
            n=1
            break                # اگر عدد وارد شده بر اعداد بین 2 تا خود آن عدد بخش پذیر بود 0 را برابر با 1 کن و آنها را از حلقه خارج کن
    
    return n

n1=int(input())
n2=int(input())

for i in range(n1,n2+1):           
   
    if prime_2(i)==0:        
        print(i,end="\t")        #آنها بابر با 0 بود آنها را چاپ کن prime_2 برای یک چیزی در بازه ی عدد اول تا عدد دوم اگر 
