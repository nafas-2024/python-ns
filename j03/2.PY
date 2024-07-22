n1=int (input("enter yhe first number: "))
n2=int(input("enter the secend number: "))
n3=int(input("enter the third number: "))

if n1==n2==n3 :
    print("Numbers are equal")
elif n1==n2 and n1<n3 :
    print(f"{n1}<{n3}")
elif n1==n2 and n3<n1 :
    print (f"{n3}<{n1}")
elif n1==n3 and n1<n2 :
    print(f"{n1}<{n2}")
elif n1==n3 and n2<n1 :
    print(f"{n2}<{n1}")
elif n2==n3 and n2<n1 :
    print(f"{n2<n1}")
elif n2==n3 and n1<n2 :
    print(f"{n1}<{n2}")
elif n1>n2 :
    print(f"{n3}<{n2}<{n1}")
elif n1>n3 :
    print(f"{n2}<{n3}<{n1}")
elif n2>n1 :
    print(f"{n3}<{n1}<{n2}")
elif n2>n3 :
    print(f"{n1}<{n3}<{n2}")
elif n3>n1 :
    print(f"{n2}<{n1}<{n3}")
elif n3>n2 :
    print(f"{n1}<{n2}<{n3}")
else :
    print("data is not correct")
    