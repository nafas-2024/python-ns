def sums(a,b):
    return a+b
# taking inputs
inp=input()
spl=inp.split()
# calling function
if len(spl)==2:
    print(sums(int(spl[0]), int(spl[1])))