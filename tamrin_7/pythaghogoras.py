def pythagoras():
    """this is a function that takes three numbers from you and 
    checks if it is possible to create a right triangle with those three number 

    Returns:
        str:can make a right triangle or not
    """
    # taking inputs
    n1=int(input())
    n2=int(input())
    n3=int(input())
    if n1**2+n2**2==n3**2 or n2**2+n3**2==n1**2 or n3**2+n1**2==n2**2:
        return "Yes"
    else:
        return "No"
# calling the function
print (pythagoras())