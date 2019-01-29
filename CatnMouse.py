#!/bin/python3
#solution for https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    x1 = abs(z - x)
    x2 = abs(z - y)
    result = 'Mouse C'
    if x1 < x2:
        result = 'Cat A'
    elif x2 < x1:
        result = 'Cat B'

    return result


q = int(input())
#print(type(q))
for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)

    print(result + '\n')


