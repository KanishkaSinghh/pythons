def next_palindrome(n):
    #if n itself is a palindrome we want to pront the next palindrome.hence n=n+1
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n


def is_palindrome(n):
    return str(n)==str(n)[::-1]



if __name__ == '__main__':
    n = int(input("enter the no of strings you wish to test\n"))
    numbers = []
    for i in range(n):
        number = int(input("enter the numbers\n"))
        numbers.append(number)
    for i in range(n):
        print(f"the palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
