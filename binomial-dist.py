# solution for https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
from math import factorial as f
p=0.12
n=10
def comb(n,x):
    return f(n)/(f(n-x) *f(x) )
#b(x1,n,p)
prob1=sum(p**x1 * (1-p)**(n-x1) * comb(n,x1) for x1 in range(0, 3))
prob2=sum(p**x1 * (1-p)**(n-x1) * comb(n,x1) for x1 in range(2, n+1))

print(round(prob1,3))
print(round(prob2,3))