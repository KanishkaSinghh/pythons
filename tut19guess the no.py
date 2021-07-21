# n=18
# input for user
#     inform th user to guess the no by informing that theno is greater or larger

n=18
number_of_guesses=1
print("your guesses are limited to 9")
while (number_of_guesses<=9):
    num=int(input("guess the number"))
    if num<18:
        print("the number is higher than the number you input")
    elif num>18:
        print("the number is lower than the number you input")
    else:
        print("you won")
        print(number_of_guesses,"number of guesses taken to finish")
    break

    print(9-number_of_guesses,"no of guessses left")
    number_of_guesses=number_of_guesses+1
if(number_of_guesses>9):
    print("game over")

