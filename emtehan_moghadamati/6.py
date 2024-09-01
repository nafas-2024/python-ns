def calculate_floor(string):
    """it is a function that by entering "u" or "d" 4 times in a line 
    , you tell the elevator to go up or down.

    Args:
        string (str): just "u" or "d"

    Returns:
        int: the floor you're on it
    """
    
    lst=[]
    # put the arg in a list
    for i in string:
        lst.append(i)
    # if the number of input was not 4 , exit of prigram
    if len(lst)!=4 :
        print("invalid input")
        exit()
    
    if string=="uuuu":
        return 4
    elif string=="uuud" or string=="uduu" or string=="uudu"or string=="duuu":
        return 2
    elif string=="uudd" or string=="dduu" or string=="uddu" or string=="udud"or string=="dudu" or string=="duud":
        return 0
    elif string=="uddd"or string=="dddu" or string=="ddud" or string=="dudd":           
        return -2
    elif string=="dddd" :
        return -4
    else:
        print("invalid input2")
        exit()
#taking input and call the funcyion 
str=input()
print(calculate_floor(str))
