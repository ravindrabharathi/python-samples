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

average=lambda x: (sum(x)/len(x))

#def average(x):
#    return sum(x)/len(x)

def sum_least_squares(x):
    ave=average(x)
    s=0
    for i in range(len(x)):
        s += (x[i]-ave)**2
    return s

sigma=math.sqrt(sum_least_squares(list1)/len(list1))
print(round(sigma,1))
a=int()
b=float()
c=str()
print(a,b,c)