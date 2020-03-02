#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridGame' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER k
#  3. STRING_ARRAY rules
#

def gridGame(grid, k, rules):
    rule_int = []
    for index, x in enumerate(rules):
        if x == 'alive':
            rule_int.append(index+1)
  
    temp_grid = grid   
    turn = 0

    while turn < k :
        new_grid = temp_grid.copy()
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                num = 0
                if i-1 > -1 and i-1 < len(grid) and j-1 > -1 and j-1 < len(x):
                    if temp_grid[i-1][j-1] ==1:
                        num += 1
                if i > -1 and i < len(grid) and j-1 > -1 and j-1 < len(x):
                    if temp_grid[i][j-1] ==1:
                        num += 1
                if i-1 > -1 and i-1 < len(grid) and j > -1 and j < len(x):
                    if temp_grid[i-1][j] ==1:
                        num += 1
                if i+1 > -1 and i+1 < len(grid) and j-1 > -1 and j-1 < len(x):
                    if temp_grid[i+1][j-1] ==1:
                        num += 1     
                if i-1 > -1 and i-1 < len(grid) and j+1 > -1 and j+1 < len(x):
                    if temp_grid[i-1][j+1] ==1:
                        num += 1
                if i > -1 and i < len(grid) and j+1 > -1 and j+1 < len(x):
                    if temp_grid[i][j+1] ==1:
                        num += 1
                if i+1 > -1 and i+1 < len(grid) and j > -1 and j < len(x):
                    if temp_grid[i+1][j] ==1:
                        num += 1
                if i+1 > -1 and i+1 < len(grid) and j+1 > -1 and j+1 < len(x):
                    if temp_grid[i+1][j+1] ==1:
                        num += 1
                if num in rule_int:
                    new_grid[i][j] == 1
                else:
                    new_grid[i][j] == 0

        temp_grid = new_grid
        turn +=1

    return temp_grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    rules_count = int(input().strip())

    rules = []

    for _ in range(rules_count):
        rules_item = input()
        rules.append(rules_item)

    result = gridGame(grid, k, rules)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
