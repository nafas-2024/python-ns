def calculate_floor(string):
    """it is a function that by entering "U" or "D" 4 times in a line 
    , you tell the elevator to go up or down.
    Args:
        string (str): just "U" or "D"
    Returns:
        int: the floor you're on it
    """
    c=0
    # if "string" has 4 letters
    if len(string)==4:
        for i in string:
            if "U"in i:
                c+=1
            elif  "D" in i:
                c-=1
        return c
    else :
        return "Invalid input"

# getting input and calling function
inp=input()
print(calculate_floor(inp))
