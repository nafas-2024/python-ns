def maxim():
    """this is a function that you first give it a number and 
    then enter some numbers in the range of that number and 
    the function will show you the maximum of numbers that you given
    """
    x=input()
    y=input()
    m=y.split()
    if len(m)==int(x):
        print(max(m))
    else :
        print("invalid inputs")
# calling thi function
maxim()