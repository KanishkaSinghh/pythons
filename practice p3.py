#take the size of lis
print("enter the list one by one\n")
size=int(input("enter size of list:"))
mylist=[]
#take input from user one by one
for i in range(size):
    mylist.append(int(input("enter the element\n")))

print(f"your list is {mylist}")
#reverse methods:
reverse1=mylist[:]
reverse1.reverse()
reverse2= mylist[::-1]
print(f"my first reverse of {mylist} is {reverse1}")
print(f"my second reverse of {mylist} is {reverse2}")
reverse3=mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"my third reverse {mylist} is {reverse3}")
if (reverse3 == reverse1 and reverse2==reverse1):
    print("all three give same resutls")

