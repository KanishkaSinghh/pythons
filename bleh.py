# stone paper scissor
import random
l=["stone","paper","scissor"]

user_score = 0
comp_score = 0
i=0



#stone


def func1():

    y = random.choice(l)
    print("computer:",y)
    global user_score
    global comp_score


    if x=="stone" and y=="scissor":
        print("user wins")
        user_score += 1
    if x=="stone" and y=="paper":
        print("computer wins")
        comp_score += 1
    if x=="stone" and y=="stone":
        print("play again")
    print("Chances left:",5-i)


#paper

def func2():
    global user_score
    global comp_score
    y = random.choice(l)
 #   print("user:{},computer:{}".format(x,y))
    print("computer:",y)
    if x=="paper" and y=="scissor":
        print("computer wins")
        comp_score += 1
    if x=="paper" and y=="stone":
        print("user wins")
        user_score += 1
    if x=="paper" and y=="paper":
        print("play again")
    print("Chances left:",5-i)




#scissor

def func3():
    global user_score
    global comp_score
    y = random.choice(l)
    print("computer:",y)

    if x=="scissor" and y=="paper":
        print("user wins")
        user_score += 1
    if x=="scissor" and y=="stone":
        print("computer wins")
        comp_score += 1
    if x=="scissor" and y=="scissor":
        print("play again")
    print("Chances left:",5-i)


while i<6:
    x = input("user: ")
    if x=="stone":
        func1()
    if x=="paper":
        func2()
    if x=="scissor":
        func3()
    i+=1

print(f"user's score : {user_score}, computer's score : {comp_score}")