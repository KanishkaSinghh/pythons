# design a calculator which will solve all the calculations except the following


print("enter first number")
num1=int(input())
print("enter second number")
num2=int(input())
print("enter operator")
operator=input()
float=0


if num1==45 and num2==3 and operator=='*':
    print("0")
elif num1==56 and num2==9 and operator=='+':
    print("10")
elif num1==56 and num2==6 and operator=='/':
    print("13")
elif(operator == '+') :
    plus=num1+num2
    print(plus)
elif operator == '-' :
    minus = num1-num2
    print(minus)
elif operator == '*' :
    pro = num1*num2
    print(pro)
elif (operator == '/'):
    float=num1/num2
    print(float)
else:
    print("not possible")
