def phone(inp):
    """this is a function that you give it a number and it tells
    you how long it will take for the phone charge to reach that number
    Args:
        inp (int): number of charge you want to know
    Returns:
        int:how many minutes does it take to charge phone to that number
    """
    s=0
    for i in range(inp):
        sharg=i+1
        s+=sharg
    return s
# getting input and  calling function
inp = int(input())
print(phone(inp))