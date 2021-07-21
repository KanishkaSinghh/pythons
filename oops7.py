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
class programmer(employee):
    def __init__(self,aname,asalary,arole,language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=language
    def printprog(self):
        return f"the name is {self.name}. the salary is {self.salary}. role is {self.role}. the languages are {self.language}. "

harry= programmer("harry",455,"instuctor",["cpp"])
rohan=programmer("rohan",255,"student",["py"])

shubham = programmer("shubahm",555,"programmer",["ijnk"])
karan = programmer("karan",552,"programmer",["python"])
print(karan.printprog())