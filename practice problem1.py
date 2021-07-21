#your age in 2090
yearage =int(input("enter your age: "))
isage= False
isyear = False
if len(str(yearage))==4:
    isyear=True
else:
    isage= True
if  yearage > 2019:
    print("you are not born yet")
    exit()
if (yearage < 1900 and isyear):
    print("you seem to be the oldest over here")
    exit()
if isage:
    yearage=2019-yearage
print(f"you will be 100 in {yearage+100}")
interestedyear=int(input("enter the year you want to know your age"))
print(f"you will be { interestedyear-yearage} in {interestedyear}")
