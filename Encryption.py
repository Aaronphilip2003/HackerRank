import math
import os
import random
import re
import sys
from math import *
# Complete the encryption function below.
def encryption(s):
	s=s.replace(" ","")
	n = len(s)
	r = floor(sqrt(n))
	c = ceil(sqrt(n))
	result = []
	for i in range(c):
		temp = []
		j=0
		while i+j<n:
			temp.append(s[i+j])
			j+=c
		result.append("".join(temp))
    
	return" ".join(result)

s = input()

result = encryption(s)

print(result)
