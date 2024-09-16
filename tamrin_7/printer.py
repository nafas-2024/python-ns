def print_number(number):
    """this ia a function that you give a number to it 
    and itprints the digits of that number in the range of that digit 
    Args:
        number (str): number you want to see its digits
    """
    for i in number:
        ini=int(i)
        print(i+":", i * ini)

# getting input and calling the function

number= input()
print_number(number)
