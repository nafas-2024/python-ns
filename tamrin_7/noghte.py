def noghte(inp):
    """it is a function that you give it for numbers in one line 
    and if you and your boss are in a same row it shows you "Horizental" 
    , if you and your boss are in a same column it shows you "Vectical"
    and  other wise it will show you "Try again".
    Args:
        inp (str): the coordinates of you and your boss
    """
    if inp[0] == inp[1] == inp[2] == inp[3] or inp[0]==inp[2]and inp[1]==inp[3]:
        print("invalid input")
    elif inp[1] == inp[3]:
        print("Horizontal")
    elif inp[0] == inp[2]:
        print("Vertical")
    else:
        print("Try again")

# getting input and calling the function
inp = input()
inp=inp.split()
noghte(inp)