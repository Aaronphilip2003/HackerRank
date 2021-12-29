#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    current_pos=0
    jumps=0
    last_pos=len(c)-1
    second_last_pos=len(c)-2
    
    while current_pos<second_last_pos:
        if c[current_pos+2]==0:
            current_pos+=2
        else:
            current_pos+=1
        jumps+=1
    
    if current_pos!=last_pos:
        jumps+=1
        
    return jumps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
