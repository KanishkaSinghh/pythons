# def function1():
#     print("plese subscribe")
# func2 = function1
# del function1
# func2()


def dec1(func1):
    ()    def nowexec():
        print("excecuteing now")
        func1()
        print("executed")
    return nowexec()

@dec1
def who_is_harry():
    print("harry styles")
# who_is_harry=dec1(who_is_harry

