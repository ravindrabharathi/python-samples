#sol for https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy
N,M,P= input().split()
n_arr=numpy.array([],int)
for i in range(int(N)+int(M)):
    n_arr=numpy.concatenate([n_arr,list(map(int,input().strip().split(' ')))],axis=0)
n_arr.shape=((int(N)+int(M)),int(P))
print(n_arr)