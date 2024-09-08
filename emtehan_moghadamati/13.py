def corona(sh_1 , sh_2 , n_1 , n_2):
    """

    Args:
        sh_1 (int): how many people has corona in shekarestan
        sh_2 (int): how many people died due  tocorona in shekarestan
        n (int): how many people has corona in namakestan
        n2 (int): how many people died due  tocorona in namakastan
    """
    shekarestan=sh_1-sh_2
    namakestan=n_1-n_2
    
    
    if shekarestan>namakestan:
       return "shekarestan"
    elif namakestan>shekarestan:
        return "namakestan"
    elif namakestan==shekarestan:
        return "equal"
    
#  calling the funcyion
sh_1 , sh_2 = int(input()) , int(input())
n_1 , n_2 = int(input()) , int(input())     

# conditions
if sh_1<1 or sh_2<1 or sh_1<sh_2: 
    print("invalid input") , exit()
if n_2<1 or n_1<1 or n_1<n_2 :
    print("invalid input") , exit()
# calling the function
else:
    print(corona(sh_1 , sh_2 , n_1 , n_2))

