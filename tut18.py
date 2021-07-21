# i=0
#
# while(i<45):
#     print(i,end =" ")
#     i=i+1
# i=0
#
# while(True):
#     print(i,end =" ")
#     if (i==45):
#         break
#     i=i+1

#
while (True):
    imp=int(input("enter a num\n"))
    if imp>100:
        imp=imp+1
        print("congo\n")
        break
    else:
        print("try again\n")
        continue