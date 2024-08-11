def letters(name):
    """this is a function that you give a number and
    write some names as much as numbers
    you give

    Args:
        name (str):input names

    Returns:
        int: how many letters repeated
    """
    count=0
    f={}
    for i in name:
        if i in f:
            f[i]+=1
        else:
            f[i]=0         
    for j in f.values():
        if j>=1:
            count+=j
    return count

chars=0
how_many=int(input())
for i in range(how_many):
    n=input()
    chars+=letters(n)
print(chars)