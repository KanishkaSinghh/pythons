class A :
    classvar1="i am a class variavle in class a"
    def __init__(self):
        self.var1="i am inside classA's constructor"
        self.classvar1="instance variable a"
class B(A):
     classvar2="i am in class b"
a=A()
b=B()
print(b.classvar1)