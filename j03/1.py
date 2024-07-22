math=int(input("enter the math score: "))
scienc=int(input("neter the scienc score: "))
art=int(input("enter the art score: "))
music=int(input("enter the music score: "))

GPA=(math+scienc+art+music)/4
if GPA<=20 :
    print(GPA)
elif GPA<10 :
    print("failed")
elif GPA>20 :
    print(" your data is not correct")
elif  GPA>=10 and GPA<12 :
    print("your GPA is ( D )")
elif GPA>=12 and GPA<14:
    print("your GPA is ( C )")
elif  GPA>=14 and GPA<16 :
    print("your GPA is ( B )")
elif  GPA>=16:
    print("your GPA is ( A )")
