import numpy as np

x=np.array([7,15])
y=np.array([18,19])

print(x<7)
print(y>17)

x1=x<7
y1=y>17

print(np.logical_or(x1,y1))

int_list=[1,2,3]
dd= (p+1 for p in int_list)

#for i in dd:
#    print(i)

print(dd.__next__())
print("-----")
for i in dd:
    print(i)

yy=[1,2,3]

y2=[k**2 for k in yy]

print(y2)

kk=zip(yy,y2,yy)

for l in kk:
    print(type(l))

print(type(range(100)))

#for i in range(100):
    #print(i)

n=["n1","n2"]
m=["m1","m2"]

z= zip(n,m)
for i in iter(z):
    print("kkk")
    print(type(i))

p = [9, 13, 8, 14, 7, 2]
print(sorted(p, reverse=False))

y="Mercury"
print((y).lower())



print(*z)
print(z)

