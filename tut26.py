# f = open("kanishka.txt")
# content = f.read()
# print(content)
# f.close

#kind of indexing of the txt file
f = open("kanishka.txt")
content = f.read(5)
print(content)
content = f.read(3)
print(content)
f.close  