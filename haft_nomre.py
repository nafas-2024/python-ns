lst=[10, 20, 20, 25, 30, 40]
# most in lst
print(max(set(lst)), key=lst.count)
# average of lst
c=0
for i in lst :
    c+=i
    j=c/len(lst)
print (j)

