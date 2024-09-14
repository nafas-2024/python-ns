def printer(inp):
    """this is a function that takes an intiger 
    and prints each digit in range of that digit
    """
    for i in inp:
        print(i ,":", i * int(i))
    exit()
inp=input()
print(printer(inp))