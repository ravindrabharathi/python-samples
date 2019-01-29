#sol for https://www.hackerrank.com/challenges/np-arrays/problem
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr=numpy.array(arr,float)
    return np_arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# sol for  https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy
arr=list(map(int,input().strip().split(' ')))
n_arr=numpy.array(arr)
n_arr.shape=(3,3)
print(n_arr)


#sol for https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

N, M = input().split(' ')
arr = numpy.array([], int)
for i in range(int(N)):
    arr = numpy.append(arr, list(map(int, input().strip().split(' '))))

arr.shape = (int(N), int(M))
print(numpy.transpose(arr))
print(arr.flatten())