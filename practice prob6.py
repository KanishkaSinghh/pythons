import random
player1=input("Enter the name of player 1")
player2=input("Enter the name of player 2")
a=int(input(" enter value of a"))
b=int(input(" enter value of b"))
c1=0
c2=0
mylist=[]
#creating a list of possible numbrs
for i in range(a,b+1):
    mylist.append(i)
print(mylist)
ran_number=random.choice(mylist)
#for player one
print(f"{player1} enter the choice of number ranging between {a} to {b}")
while True:
    c1=c1+1
    p1=int(input("enter the number"))
    if p1==ran_number:
        print(f"you took {c1} trails guess correct\n")
    elif p1<ran_number:
        print("wrong! . guess a larger number.\n")
    else:
        print("wrong! . guess a smaller number.\n")
#for player 2
print(f"{player2} enter the choice of number ranging between {a} to {b}")
while True:
    c2=c2+1
    p2=int(input("enter the number"))
    if p2==ran_number:
        print(f"you took {c2} trails guess correct\n")
    elif p2<ran_number:
        print("wrong! . guess a larger number.\n")
    else :
        print("wrong! . guess a smaller number.\n")
#comparing
if c1==c2:
    print("the game has end to a draw")
elif c1<c2:
    print(f"{player1} has won over with {c1-c2}")
elif c1<c2:
    print(f"{player2} has won over {c2-c1}")