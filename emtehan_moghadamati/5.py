def wow (num) :
    """with each number you enter , th number of "wow! o's" increases.

    Args:
        num (int): the number you want is the number of "o"
    """
    
    print("w" , end="")
    # how many print o in wow!
    for i in range (num):
        print("o" , end= "")
    print ("w!")
    
n=int(input())
# call th function
wow(n)
