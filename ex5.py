def getdate():
    import datetime
    return datetime.datetime.now()
print("welcome to health management system, click 1 to write 0 to read and 2 to exit")
selector=int(input())
if selector==0:
    print("thank you for entering to read")
    check=int(input())

    print("you have entred the recipeints list: to acess it type the number of repective receipient-\n1 1)harry \n2 rohan \n3 hammad")
    inp=int(input())
    if inp==1:
            print("you have entered the log of harry. please inform what do you wish to check - 1)FOOD /n 2) EXECISE ")
            inp=int(input())
            if inp==1:
                print("HARRY'S FOOD LOG")
                with open("harryfood.txt","r") as h1:
                    for i in h1:
                        print(i)

            elif check==2:
                print("HARRY'S EXERCISE LOG")
                with open("harryexercise.txt") as h2:
                    for i in h2:
                        print(i)
            else:
                print("invalid")

#rohan

    elif inp == 2:
        print("you have entered the log of rohan. please inform what do you wish to check - 1)FOOD /n 2)EXERCISE")
        inp = int(input())
        if inp == 1:
                print("ROHAN'S FOOD LOG")
                with open("rohanfood.txt", "r")as r1:
                    for i in r1:
                                print(i)

        elif check == 2:
                print("ROHAN'S EXERCISE LOG")
                with open("rohanexercise.txt")as r2:
                    for i in r2:
                        print(i)


        else:
            print("invalid")

#hammad

    else:
            print("you have entered the log of hammad. please inform what do you wish to check - 1)FOOD \n 2) EXERCISE ")
            inp = int(input())

            if inp== 1:
                print("HAMMAD'S FOOD LOG")
                with open("hammadfood.txt", "r") as ha1:
                    for i in ha1:
                        print(i)
            elif check == 2:
                print("HAMMAD'S EXERCISE LOG")
                with open("hammadexercise.txt") as ha2:
                    for i in ha2:
                        print(i)
            else:
                print("invalid")

       #for write funtion

elif selector==1:
   print("thank you for entering to write")

print("you have entred the recipeints list: to acess it type the number of repective receipient- /n1 1)harry /n2 rohan /n3 hammad")
inp = int(input())
if inp == 1:
            print("you have entered the log of harry. please inform what do you wish to add data to - 1)FOOD /n 2) EXERCISE ")
            inp = int(input())
            if inp == 1:
                print("HARRY'S FOOD LOG selected , feel free to add")
                with open("harryfood.txt", "a") as h1:
                  for i in h1:
                    print(i)
                inp1=input()
                h1.write("\n")
                h1.write(str(get_time()))
                h1.write("\n")
                h1.write(inp1)
                print("your entry is successful")

            elif inp == 2:
                print("HARRY'S EXERCISE LOG feel free to add on")
                with open("harryfood.txt", "a") as h2:
                  for i in h2:
                    print(i)
                inp1 = input()
                h2.write("\n")
                h2.write(str(get_time()))
                h2.write("\n")
                h2.write(inp1)
                print("your entry is successful")
            else:
                print("invalid")

        # rohan

elif inp == 2:
            print("you have entered the log of rohan. please inform what do you wish to add - 1)FOOD /n 2) EXERCISE ")
            inp = int(input())
            if inp == 1:
                print("ROHAN'S FOOD LOG selected , feel free to add")
                with open("rohanfood.txt", "a") as r1:
                    for i in r1:
                     print(i)
                inp1 = input()
                r1.write("\n")
                r1.write(str(get_time()))
                r1.write("\n")
                r1.write(inp1)
                print("your entry is successful")

            elif check == 2:
                print("ROHAN'S EXERCISE LOG feel free to add on")
                with open("rohanfood.txt", "a") as r2:
                    for i in ha1:
                      print(i)
                inp1 = input()
                r2.write("\n")
                r2.write(str(get_time()))
                r2.write("\n")
                r2.write(inp1)
                print("your entry is successful")
            else:
                print("invalid")

                #hammad
else:
            print("you have entered the log of hammad. please inform what do you wish to add on - 1)FOOD /n 2) EXERCISE ")
            inp = int(input())
            if inp == 1:
                print("HAMMAD'S FOOD LOG selected , feel free to add")
                with open("hammadfood.txt", "a") as ha1:
                    for i in ha1:
                        print(i)
                inp1 = input()
                ha1.write("\n")
                ha1.write(str(get_time()))
                ha1.write("\n")
                ha1.write(inp1)
                print("your entry is successful")

            elif check == 2:

               print("HAMMAD'S EXERCISE LOG feel free to add on")
               with open("hammadfood.txt", "a") as ha2:
                   for i in ha2:
                    print(i)
               inp1 = input()
               ha1.write("\n")
               ha1.write(str(get_time()))
               ha1.write("\n")
               ha1.write(inp1)
               print("your entry is successful")

            else:
                print("invalid")














