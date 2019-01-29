import math
#lambda
L=2.5
k=5
p=L**k * math.exp(-1*L)/math.factorial(k)
print(round(p,3))

#solution for https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

l_a=0.88
l_b=1.55
X2=l_a**2+l_a
Y2=l_b**2+l_b
CA=160+40*X2
CB=128+40*Y2

print(round(CA,3))
print(round(CB,3))


#import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))


mu=20
s=2
X2=19.5
Xu=22
Xl=20
fx=lambda x: 1/2*(1+ math.erf((x-mu)/(s*math.sqrt(2))))

p1=fx(X2)
p2=fx(Xu)-fx(Xl)

print(round(p1,3))
print(round(p2,3))

#solution for https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

mu=70
s=10
p1=(1-fx(80))*100
p2=(1-fx(60))*100
p3=fx(60)*100

print(round(p1,2))
print(round(p2,2))
print(round(p3,2))

#test format
print('{:.3f}'.format(100222.0))