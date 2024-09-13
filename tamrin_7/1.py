def multi():
    """this is a function that takes a number and print its multiplication table
    """
    n=int(input()) 
    for i in range(1,n+1):
        for j in range(1,n+1):
            print (i *j,end="  ")
        print()
# calling the function   
multi()