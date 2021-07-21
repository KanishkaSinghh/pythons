def next_palindrome(n):
    #if n itself is a palindrome we want to pront the next palindrome.hence n=n+1
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n


def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    size=int(input("enter the size of list"))
    l1=[]
    for i in range(size):
        l1.append(int(input("enter the elements of list")))
    print(f"you have enter the list {l1}")
    new_list=[]
    for element in l1:
        if element >10:
            n=next_palindrome(element)
            new_list.append(n)
        else:
            new_list.append(element)
    print(f"output list {new_list}")



