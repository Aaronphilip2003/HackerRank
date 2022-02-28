#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    pages=p//2
    total=n//2
    
    from_front=pages
    from_back=total-pages
    
    res=min(from_back,from_front)
    
    return  res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())
    
    
    
    result = pageCount(n,p)
    fptr.write(str(result) + '\n')

    fptr.close()
