def pilgrimage():
    """it is a function that the firs thing you enter is whether you 
    have gone on a pilgrimage to mecca , karbala , or mashhad , and 
    if you haven't gone on either of these trips, it show you "agha" .
    """
    
    z=input()
    if z=="yyy" or z=="yyn" or z=="ynn" or z=="yny":
        print("haji")                    # if "z" has these conditions , print "haji"
    elif z=="nyy" or z=="nyy" or z=="nyn":
        print("karbalaee")              # if "z" has these conditions , print "karbalaee"    
    elif z=="nny":
        print("mashti")                 # if "z" has these conditions , print "mashti"
    else :
        print("agha")    
    
pilgrimage()