u1_won=0          # meghdar emtiaz user 1
u2_won=0          # meghdar emtiaz user 2

for a in range (5) :
    u1=input("user1 enter ( rock,paper,scissors ): ")
    u2=input("user2 enter ( rock,paper,scissors ): ")

    if u1==u2 :
     print("equal")
    elif u1=="rock" and u2=="paper":
     print("u2 won")
     u2_won+=1
    elif u1=="paper" and u2=="rock":
     print("u1 won")
     u1_won+=1
    elif u1=="rock" and u2=="scissors":
     print("u1 won")
     u1_won+=1
    elif u1=="scissors" and u2=="rock":
      d=print("u2 won")
      u2_won+=1
    elif u1=="scissors" and u2=="paper":
     print("u1 won")
     u1_won+=1
    elif  u1=="paper" and u2=="scissors":
     print("u2 won")
     u2_won+=1
    else :                          #dar gheir in sorat 
     print("not correct")       
     
print(f"user1 is :{u1_won} and user2 is : {u2_won} ")

