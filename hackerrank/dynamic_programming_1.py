#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def abbreviation(a, b, index_a = 0, index_b = 0, memory = {}):
    # Write your code here
    # print(memory)
    if (index_a, index_b) in memory:
        # print("memory hit", index_a, index_b)
        return memory[(index_a, index_b)]
    
    if len(a) - index_a < len(b) - index_b:
        memory[(index_a, index_b)] = False
        # print("A is shorter than B")
        return False
    if index_b == len(b):
        memory[(index_a, index_b)] = all([c.islower() for c in a[index_a:]])
        # print("B is empty")
        return memory[(index_a, index_b)]
    if index_a == len(a):
        memory[(index_a, index_b)] = False
        # print("A is empty")
        return False
    if a[index_a].islower():
        # print(a[index_a].upper(), b[index_b])
        if a[index_a].upper() == b[index_b]:
            memory[(index_a, index_b)] = abbreviation(a, b, index_a + 1, index_b + 1, memory) or abbreviation(a, b, index_a + 1, index_b, memory)
            # print("A is lower 1")
            return memory[(index_a, index_b)]
        else:
            memory[(index_a, index_b)] = abbreviation(a, b, index_a + 1, index_b, memory)
            # print("A is lower 2")
            return memory[(index_a, index_b)]
    else:
        if a[index_a] == b[index_b]:
            memory[(index_a, index_b)] = abbreviation(a, b, index_a + 1, index_b + 1, memory)
            # print("A is upper")
            return memory[(index_a, index_b)]
        else:
            memory[(index_a, index_b)] = False
            # print("A is upper")
            return False


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b, 0, 0, {})

        print("YES" if result else "NO")