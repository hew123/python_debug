#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'analyzeInvestments' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#

def analyzeInvestments(s):
    num = 0
    for index ,char in enumerate(s):
        counter = 0
        while(counter < len(s) - index - 1):
            counter += 1
            char = char + s[index+counter]
            if 'A' in char and 'B' in char and 'C' in char:
                num +=1

    
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = analyzeInvestments(s)

    fptr.write(str(result) + '\n')

    fptr.close()
