# n,m=map(int,input("enter length").split())
# s1='#'
# for i in range(n):
#     print((s1*((i*1)+1)).center(m))
# for i in range(n-1):
#     print((s1).center(m))
#
#

height = (input("height of tree = "))

height = int(height)

spaces = height - 1
hashes = 1
stump = height - 1

while (height != 0):

    for i in range(spaces):
        print(' ',end="")

    for i in range(hashes):
        print('#', end="")

    print()

    spaces = spaces - 1
    hashes = hashes + 2
    height = height - 1


for i in range(stump):
    print(' ',end="")
print("s")

