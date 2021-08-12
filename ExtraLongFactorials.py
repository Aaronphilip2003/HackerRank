#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    f=1
    list_numbers=[]
    for i in range(1,n+1):
        f*=i
        list_numbers.append(f)
    print(list_numbers[len(list_numbers)-1])

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
