#!/bin/python3
###
#import sys
#from datetime import date, timedelta

#def solve(year):
    # Complete this function
    #delta=255
    #if (year<=1917) & (year%4 ==0):
        #delta=254
    #dd=date(year,1,1)
    #dd=dd+timedelta(days=delta)
    #return dd.strftime('%d.%m.%Y')
#year = int(input().strip())
#print(year<=1917 & year%4==0)
#print(year%4)
#result = solve(year)
#print(result)
###
#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# !/bin/python3

import sys


def solve(year):
    # Complete this function
    datestr = '13.09'
    if year == 1918:
        return '26.09.1918'
    elif ((year <= 1917) & (year % 4 == 0)) or (
        (year > 1918) & ((year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)))):
        return '12.09.' + str(year)
    else:
        return '13.09.' + str(year)


year = int(input().strip())
result = solve(year)
print(result)