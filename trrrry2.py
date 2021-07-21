
f1 = open("harryfood.txt")

try:
    f = open("does2.txt")

except Exception as e:

    print(e)
    print("ys")

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
