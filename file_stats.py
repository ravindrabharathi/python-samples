#Hackerrank Basic Statistics Warmup
import numpy as np
from statistics import mode
import math
fname="D:\\hackerrank\\values.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
list1_len=int(content[0])
list1=np.array(content[1].split(),dtype=np.float64)
assert (list1_len>=10 & list1_len <=2500) , "Size of sample should be between 10 and 2500"
assert ((min(list1)>0) & (max(list1) < 100000)) , "Elements must be positive integers between 1 and 100000 "
#mean
list1_mean=np.mean(list1)
print(round(list1_mean,1))
#median
print(round(np.median(list1),1))

#mode
if (len(set(list1)) != list1_len ):
    if (len(set(list1)) - list1_len ==1):
        print(int(mode(list1)))
    else:
        list1_l=list1.tolist()
        dupes=set([x for x in list1_l if list1_l.count(x) > 1])
        #print(dupes)
        print(int(min(dupes)))
else:
    print(int(min(list1)))
#std deviation
list1_std=np.std(list1)
print(round(list1_std,1))
#confidence interval 95%
list1_SE=list1_std/math.sqrt(list1_len)
list1_CI_upper= round(list1_mean+list1_SE*1.96,1)
list1_CI_lower= round(list1_mean-list1_SE*1.96,1)
print(str(list1_CI_lower)+ ' '+str(list1_CI_upper))