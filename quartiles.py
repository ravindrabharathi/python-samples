import math
#----------
#for reading from system input
#import sys
#data = sys.stdin.readlines()
#------------------------------
fname="D:\\hackerrank\\quartile_values2.txt"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]
list1_len=int(content[0])
list1=content[1].split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
print(list1)
list1.sort()
print(list1)
is_even=lambda x: (x%2==0)

def get_mid_median(y):
    mid = len(y) / 2

    if is_even(len(y)):
        median1 = (y[int(mid-1)] + y[int(mid)]) / 2

    else:
        median1 = y[int(mid)]
    return mid, median1

mid, Q2= get_mid_median(list1)

list1_1=list1[0:math.floor(mid)]
if (is_even(list1_len)):
    list1_2=list1[round(mid):]
else:
    list1_2 = list1[round(mid)+1:]


mid1,Q1=get_mid_median(list1_1)
mid2,Q3=get_mid_median(list1_2)
print(Q1)
print(Q2)
print(Q3)
print(list1_1)
print(list1_2)