import math
#----------
#for reading from system input
#import sys
#data = sys.stdin.readlines()
#------------------------------
fname="D:\\hackerrank\\values2.txt"
with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content]
list1_len=int(content[0])
maths=[]
physics=[]
chemistry=[]
def ave(x):
    assert len(x)>0 , 'size of sample should be >0'
    return float(sum(x))/len(x)
def pearson_r_coeff(x,y):
    assert (len(x)==len(y)) , 'size of the two samples must be the same'
    assert len(x) > 0, 'size of sample should be >0'
    ave_x=ave(x)
    ave_y=ave(y)
    s1=0
    s2=0
    s3=0

    for i in range(len(x)):
       s1 +=(x[i] - ave_x) * (y[i] - ave_y)
       s2 +=((x[i] -ave_x)**2)
       s3 +=((y[i] -ave_y)**2)
    coeff=s1/(math.sqrt(s2)*math.sqrt(s3))

    return coeff
for i in range(1,list1_len+1):
    row=content[i].split()
    maths.append(int(row[0]))
    physics.append(int(row[1]))
    chemistry.append(int(row[2]))
#print((ave(maths)))
#print(ave(physics))
#print(ave(chemistry))
print(round(pearson_r_coeff(maths,physics),2))
print(round(pearson_r_coeff(physics,chemistry),2))
print(round(pearson_r_coeff(chemistry,maths),2))