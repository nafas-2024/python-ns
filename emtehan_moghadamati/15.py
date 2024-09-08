# lambda function
reverse_1=lambda num : "yes" if num==num[::-1] else "no" 

# calling the function
n=(input())
print(reverse_1(n))

