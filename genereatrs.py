# def gen(n):
#     for i in range (n):
#         yield i
# g= gen(94152)
# print(g)
# Factorial
# def factorial(number):
#     result=1
#     i=1
#     while(i<=number):
#         result=result*i
#         i+=1
#         yield result
#
# if __name__ == "__main__":
#     fac=factorial(5)
#     for item in fac:
#         print(item)
# fibonacci
# def Fibonaachi(Number):
#     i = 0
#     a = 0
#     b = 1
#     temp = 0
#     while i < Number:
#         yield a
#         temp = a
#         a = b
#         b = temp + a
#         i = i + 1
#
# if __name__ == "__main__":
#     Fib = Fibonaachi(10)
#     for item in Fib:
#         print(item)

"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)