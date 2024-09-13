def mashgh(z1,z2,z3):
    """it is a function that takes three angles and tells you 
    if you can make a triangle with these three angles or not 
    Args:
        z1 (int): angel_1
        z2 (int): angle_2
        z3 (int): angle_3
    Returns:
        str: can you make a triangle or not
    """
    if z1 <=0 or z1 >360 or z2 <=0 or z2 >360 or z3<=0 or z3>360:
        return "No"
    if z1+z2+z3==180:
        return"Yes"
    else :
        return "No"
# taking three angles in one line
inp=input()
spl=inp.split()
if len(spl)==3:
    print(mashgh(int(spl[0]), int(spl[1]), int(spl[2])))
