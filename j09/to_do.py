lst=[]
def to_do_list(works):
    while 1:
        print("options :",
            "enter \"add\"to add a task",
            "enter \"view\"to view task",
            "enter \"done\"to mark a task as done",
            "enter \"remove\"to remove a task",
            "enter \"exit\"to exit the program",sep="\n")
        work=input("input : ")   #داده ای را از کاربر میگیرد
        
        if work=="add":
            adds=input("enter a new task : ")
            lst.append(adds)               #  را تبدیل به لیست کن adds بود  add اگر داده برابر با    
        if work=="view":
            print(lst)
        if work=="done":
            dones=int(input("enter the number of your program you done and start by 0 : "))
            
            lst.insert(dones,"*")
            print(lst)                           #  بود به پشت شماره ی عدد وارد شده * اضافه کن done اگر داده برابر با 
        if work=="remove":
            n=int(input("enter the number do you want to delete and start by 0 : "))
            lst.pop(n)
            print(lst)                       # بود به ازای عددی که کاربر وارد می کند ان را حذف کن remove  اگر داده برابر با 
        if work=="exit":
            print("end")
            break                          # بود حلقه را بشکن exit اگر دهده برابر با 
        
        
works=""
to_do_list(works)
