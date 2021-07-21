# snake water gun
#import random
import random


print("Welcome to the game of snake water and gun")
attempt=1
c=0
user=0

while(attempt<=10):


    list=["snake","gun","water"]
    ran=random.choice(list)

    inp= input("enter your input(snake/water/gun: )")
    inp=inp.lower()

    if inp==ran:
         print("Tie")
         print(f"The computer chose {ran} and you choose was {inp}")

    elif ran=="snake" and inp=="water":
         c=c+1
         print(f"The computer chose {ran} and you choose was {inp}")
         print("the snake drank the water")
         print("you lost this round")
         print("computer gets one point \n")

    elif ran == "water" and inp == "snake":
         user=user+1

         print(f"The computer chose {ran} and you choose was {inp}")
         print("the snake drank the water")
         print("you won this round")
         print("you get one point \n")


    elif ran == "gun"and inp == "snake":
         c=c+1
         print(f"The computer chose {ran} and your choose was {inp}")
         print("the snake got killed by the gun")
         print("you lost this round")
         print("computer gets one point \n")

    elif ran == "snake" and inp == "gun":
         user=user+1
         print(f"The computer chose {ran} and your choose was {inp}")
         print("the snake got killed by the gun")
         print("you won this round")
         print("you get one point \n")

    elif ran == "water" and inp == "gun":
         c=c+1
         print(f"The computer chose {ran} and your choose was {inp}")
         print("the gun drowned in the water")
         print("you lost this round")
         print("computer gets one point \n")

    elif ran == "water" and inp == "gun":
         print(f"The computer chose {ran} and your choose was {inp}")
         user+=1
         print("the gun drowned in the water")
         print("you won this round")
         print("you get one point \n")

    else:
         print("invalid input")
         continue
    print("no. of guesses left: {}".format(10-attempt))
    attempt=attempt+1

    if attempt>10:
         print("game over")


print(f"your score {user} \ncomputers score {c}")

if c>user:
        print("you lost and computer won")

elif c<user:

            print("you won and computer lost")
else:
            print("tie it is")
print(10-attempt," no. of attempts left")
attempt= attempt+1
if attempt>10:
       print("game over")
