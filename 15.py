def reverse_1 (num) :
    
    n1=num%10
    n2=num//10
    pr=n1,n2
    
    
    if pr==num:
        print("yes")
    else:
        print("no")
        
num=int(input())
reverse_1(num)