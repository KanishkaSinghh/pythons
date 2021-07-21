class employee:
    no_of_leave=8
    pass
harry= employee()
rohan=employee()

harry.name="harry"
harry.salary=455
harry.role="instructor"

rohan.name="rohan"
rohan.salary=4555
rohan.role="student"


print(harry.no_of_leave)
print(rohan.__dict__)
rohan.no_of_leave=10
print(rohan.__dict__)
print(employee.no_of_leave)
print(rohan.no_of_leave)