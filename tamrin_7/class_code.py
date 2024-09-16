def class_code(k):
    """it's a function that you entr number (k)
    and it shows you k'th digit from 1 to the number that you entered
    Args:
        k (int):
    """
    show = ""
    # insert 1 to (k) in "show"
    for i in range(1, k + 1):
        show += str(i)
    
    return(show[k - 1])
# calling the function
k = int(input())
print(class_code(k))

