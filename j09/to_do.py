lst=[]
def to_do_list(works):
    while 1:
        print("options :",
            "enter \"add\"to add a task",
            "enter \"view\"to view task",
            "enter \"done\"to mark a task as done",
            "enter \"remove\"to remove a task",
            "enter \"exit\"to exit the program",sep="\n")
        work=input("input : ")
        
        if work=="add":
            adds=input("enter a new task : ")
            lst.append(adds)
        if work=="view":
            print(lst)
        if work=="done":
            dones=int(input("enter the number of your program you done and start by 0 : "))
            
            lst.insert(dones,"*")
            print(lst)
        if work=="remove":
            n=int(input("enter the number do you want to delete and start by 0 : "))
            lst.pop(n)
            print(lst)
        if work=="exit":
            print("end")
            break
        
        
works=input()
to_do_list(works)