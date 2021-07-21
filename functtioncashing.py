import time
def some_work():
    time.sleep(n)
    return n


if __name__=='__main__':
    print("now running some work")
    some_work(3)
    print("Done .. calling again")
    some_work(3)
    print("Called again")

