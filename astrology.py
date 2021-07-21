# #
# # input = inteager n
# # boolean =
#
# # num =int(input("enter number how many rows you want"))
# # print("chose 0 or  1")
# # boolean = input("1 is for tue or 0 is for false")
# # if boolean==1:
# #     for i in range(0,num+1):
# #         print("*",int(i))
# # if boolean == 0:
# #     for i in range(num,0 -1):
# #         print("*",int(i))
#
#
# try:
#     n=int(input("enter the number of rows"))
#     b= int(input("enter 0 or1 : "))
#     if b is 0:
#         count = 0
#         while(count<=n):
#             print("*"/n )
#             count=count+1
#
#     elif b is 1 :
#         count = n
#         while(count!=0):
#             print("*" * count, end=" ")
#             print("/n",end=" ")
#             count=count-1
#
#
#     else:
#         print("invalid pattern")
# except exception as e:
#     print("invalid input")
#


 n = int(input("enter the number of rows"))
 b = int(input("enter 0 or 1 : "))

 def star(n,b):
     if b is 0:
         c=1
         while(c<=n):
             c=c+1
             print("*"*c)
    else:
         while c>0:
             print("*"*c)
             c=c-1

