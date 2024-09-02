def kamel (x):
    """this is a function that tells you if the sum of the divisors of 
    the number you enterd is equal to the number itself

    Args:
        x (int): _description_
    """
    # counter
    m=0
    for i in range(1,x):
        #if the number that user entered is divisible by 1 untill that number add the counter
        if x%i==0:          
            m+=i
    if m==x:
        print("yes") , exit()
    else:
        print("no") , exit()
#call the function    
num=int(input())
print(kamel(num))