u1=input("user1 enter ( rock,paper,scissors ): ")
u2=input("user2 enter ( rock,paper,scissors ): ")

if u1==u2 :
    print("equal")
elif u1=="rock" and u2=="paper":
    print("u2 won")
elif u1=="paper" and u2=="rock":
    print("u1 won")
elif u1=="rock" and u2=="scissors":
    print("u1 won")
elif u1=="scissors" and u2=="rock":
    print("u2 won")
elif u1=="scissors" and u2=="paper":
    print("u1 won")
elif u1=="paper" and u2=="scissors":
    print("u2 won")
else :
    print("not correct")