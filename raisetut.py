a= input("what is your name")
b= input("your salary")
if int(b)==0:
    raise ZeroDivisionError("you do you earn so low.quit now")
if a.isnumeric():
    raise Exception("numbers afre not allowed")
print(f"hello {a}")