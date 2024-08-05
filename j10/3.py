from random import randint as r

l_name=["nafas","zahra","nadia","raha","anita"]


for i in (l_name):           #هست l_name برای هر چیزی که در لیست 
    rand=r(1,10)             #اعدادی را به صورت شانسی از بین 1 تا 10 انتخاب و در متغیر بریز
    print(i,rand)            