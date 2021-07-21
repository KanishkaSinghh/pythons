class employee:
    no_of_leave=8
    #constructor
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole



    def printdetail(self):
        return f"the name is {self.name}. the salary is {self.salary}. role os{self.role}. "
    @classmethod
    def change_leave(cls,new_Leaves):
        cls.no_of_leave=new_Leaves
    @classmethod
    def from_str(cls,string):
         return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is "+string)
        return("yeah")

harry= employee("harry",455,"instuctor")
rohan=employee("rohan",255,"student")
karan=employee.from_str("karan-480-student")
print(karan.printgood("karan "))

