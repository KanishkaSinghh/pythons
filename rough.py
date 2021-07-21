import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    i,j=0,0
    c1=0
    c2=0
    m=len(arr)
    while(i<m and j<m):
        if arr[i] <= arr[j]:
            c1 += 1
        else:
            c2 += 1
        while i < m:
            c1 += 1
        while j < m:
            c2 += 1
        print(c1)
        print(c2)
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input().strip())

        for t_itr in range(t):
            n = int(input().strip())

            arr = list(map(int, input().rstrip().split()))

            result = countInversions(arr)

            fptr.write(str(result) + '\n')


