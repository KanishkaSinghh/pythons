# used for finding the execution time

import time
initial =time.time()
k=0
while(k<45):
    print("kay")
    k+=1
print("time taken by while loop",time.time()-initial)
for i in range(45):
    print("kay")