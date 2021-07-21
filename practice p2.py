n=int(input("enter no of apples: "))
mn = int(input("enter the min no of range of apples: "))
mx = int(input("enter the max no of range of apples: "))

def apples():
    for i in range(mn,mx+1):
        if n%i==0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")

Apple=apples()
