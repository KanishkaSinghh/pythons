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

    def __add__(self, other):
        return self.salary + other.salary


emp1=employee("harry",345,"Programmer")
emp2=employee("rohan",45,"cleaner")
print(emp1+emp2)