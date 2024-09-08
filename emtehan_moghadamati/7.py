def watermelon_melon (w , m):
    """this is a function that you give it a number of watermelons
    and melons and if you two eat these , will it add to your life equally or not.
    Args:
        h (int): the number of watermelons
        k (int): the number of melons
    """
    # if "k" was odd , print "no"
    if m%2!=0:
        print ("no")
    else:
        print ("yes")
# getting inputs and calling the function
w=int (input())
m=int (input())
watermelon_melon(w , m)