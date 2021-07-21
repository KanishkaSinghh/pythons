# def funargs(*args):
#     print(args[0])
# har = ["harry", "rohan","skill","s"]
# funargs(*har)

def funargs(n,*args):
    for item in args:
        print(item)
har = ["harry", "rohan","skill","s","argghhh"]
funargs(*har)