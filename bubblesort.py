#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
#solution for https://www.hackerrank.com/challenges/30-sorting/problem
def bubbleSort(a):
    numSwaps=0
    if (len(a)<=1):
        return a, 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (a[i]>a[j]):
                print(a[i],a[j])
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                numSwaps +=1
    return a, numSwaps

sorted_list, numSwaps=bubbleSort(a)

print('Array is sorted in '+str(numSwaps)+' swaps.')
print('First Element: '+str(sorted_list[0]))
print('Last Element: '+str(sorted_list[n-1]))