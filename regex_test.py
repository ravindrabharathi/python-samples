#solution for https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re
import sys
data=sys.stdin.readlines()
data=''.join(data[1:])
#print(data)
data=re.sub("(?<= )\&\&(?= )","and",data)
data=re.sub("(?<= )\|\|(?= )","or",data)
print(data)




