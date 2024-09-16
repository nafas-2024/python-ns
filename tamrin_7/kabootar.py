def looneh(spl):
    """this is a functon that takes the number of pigeons
    and nests and tells you "Yes" if pigeons should be
    grouped together in the same nest and "No" otherwise
    Args:
        spl (lst(split)): number of pigeons and nests
    """
    if spl[0]> spl[1]:
        print("Yes")
    elif spl[1]> spl[0] or spl[0]==spl[1]:
        print("No")
        
# getting the number of pigeons and nests in a list
inp=input().split()
# calling function
looneh(inp)