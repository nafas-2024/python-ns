def haft_sin(x):
    """this is a function that you enter a number and it shows you
     haft sin members to that number you write

    Args:
        x (int): the number you want to see members of haft sin by it

    Returns:
        str: members of haft sin
    """
    
    sin_ha=["sib", "samanoo", "senjed" , "somagh" , "serke" , "sabze" , "sir"]
    s=""
    # show members of haft sin 
    for i in range(x):
        s=s+sin_ha[i]+"\n"
        return s
    
num=int(input())
if num <=0 or num>7 :
    print("invalid input")
# call the function
else:
    
    print(haft_sin(num))