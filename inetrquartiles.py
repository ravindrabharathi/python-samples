import math
import sys
#content = sys.stdin.readlines()
fname="D:\\hackerrank\\inetrquartiles.txt"
with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content]
elem_len=int(content[0])
elements=content[1].split()
freq=content[2].split()
list1=[]
for i in range(elem_len):
    print(i,int(freq[i]),elements[i])
    for j in range(int(freq[i])):
        list1.append(int(elements[i]))
    print(list1)

print(list1)
print(len(list1))
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
print(mid, Q2)
list1_1=list1[0:math.floor(mid)]
if (is_even(elem_len)):
    list1_2=list1[round(mid):]
else:
    list1_2 = list1[round(mid)+1:]
print(list1_1)
print(len(list1_1))
print(len(list1_2))
print(list1_2)

mid1,Q1=get_mid_median(list1_1)
mid2,Q3=get_mid_median(list1_2)
print(mid1,Q1)
print(mid2,Q3)
print(round(float(Q3)-float(Q1),1))
