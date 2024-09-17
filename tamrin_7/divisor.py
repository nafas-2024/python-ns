def maghsoom(num):
    """it is a function that takes a number and
    prints the number of divisors and their sum
    Args:
        n (int):
    """
    # counter and sum
    count=0
    sum=0
    for i in range(1,num+1):
        for j in range(1,(i+1)//2+2):    
            if i%j==0:
                count+=1
                sum+=j
        # if "i" bigger than 3
        if i>3:
            count+=1
            sum+=i
    print(count, sum)
# getting inputs and calling numbers
num=int(input())
maghsoom(num)
