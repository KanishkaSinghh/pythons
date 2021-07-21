# self-)

# class employee:
#     no_of_leave=8
#     def printdetail(self):
#         return f"the name is {self.name}. the salary is {self.salary}. role os{self.role}. "
# harry= employee()
# rohan=employee()
#
# harry.name="harry"
# harry.salary=455
# harry.role="instructor"
#
# rohan.name="rohan"
# rohan.salary=4555
# rohan.role="student"
# print(harry.printdetail())


# consstructor->
class employee:
    no_of_leave=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole



    def printdetail(self):
        return f"the name is {self.name}. the salary is {self.salary}. role os{self.role}. "
harry= employee("harry",455,"instuctor")
# rohan=employee()

# harry.name="harry"
# harry.salary=455
# harry.role="instructor"
#
# rohan.name="rohan"
# rohan.salary=4555
# rohan.role="student"
print(harry.salary )

