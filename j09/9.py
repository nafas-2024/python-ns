def rhombus(x):
    for i in range(x+1):            #برای یک چیزی در بازه ی عدد وارد شده +1
        print(" "*(x-i+1)+"*" *(2*i+1))         
    for i in range(x,0,-1):         #برای یک چیزی در بازه ی عدد وارد شده تا 0 تا -1با همان ویژگی های قبلی
        print(" "+" "*(x-i+1)+"*"*(2*i-1))
        
n=int(input())
rhombus(n)