#!/bin/python3

import sys

def sum_digits(n):
    return n and n % 10 + sum_digits(n // 10)

def superDigit(n, k):
    # Complete this function
    #n1 = n * k
    if len(n) == 1 & k==1:
        s_d = n
        return s_d
    else:
        d_list = [int(char) for char in n]
        s = sum(d_list)
        s= s*k
        #s=sum_digits(int(n))

        #for i in range(len(d_list)):
            #s += float(d_list[i])
        s = str(int(s))
        return superDigit(s, 1)


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = superDigit(n, k)
    #print(int(n)//10)
    print(result)