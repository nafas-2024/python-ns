def game (number) :
    """you give a number and get the diffrence of the digits of that two-digit number.

    Args:
        number (int): a number that is entered to subtract its digit from each other

    Returns:
        int: subtracting digits from each other
        
    """
    lst=[]
    # make a list of the number
    for i in str(number):
        lst.append(int(i))
    
    # if two members are missing from the list print "invalid input"
    if len(lst)!=2:
        print("invalid input")
        exit()
    # subtraction of digits
    if lst[0]>lst[1]:
        return lst[0]-lst[1]
    elif lst[0]<lst[1]:
        return lst[1]-lst[0]
    elif lst[0]==lst[1]:
            return 0
   
number=int(input())
print(game(number))
