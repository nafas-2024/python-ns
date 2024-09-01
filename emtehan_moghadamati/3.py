def facto () :
    """ This is a factorial function that takes a number from you and 
    shows you the product of the numbers 1 to that number itself.  """   
   
    n=int(input())                    #عددی را از کاربر بگیر
    m=1

    for i in range(1,n+1) :                  #برای هر چیزی که بین 1 تا عدد گرفته شده هست
        m*=i                                #به هر عددی که رسیدی آن را تا عدد گرفته شده ضرب کن                        
    print(f"{n}! = {m}")
        
facto()