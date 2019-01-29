# Enter your code here. Read input from STDIN. Print output to STDOUT
#sol for https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
import sys
data=sys.stdin.readlines()
N=int(data[0]) # not needed for below lines
data=data[1:]
regex_pattern=r'[789]\d{9}$'
for x in data:
    if (re.match(regex_pattern, x)):
        print("YES")
    else:
        print('NO')