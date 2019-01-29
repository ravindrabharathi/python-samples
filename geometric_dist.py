# solution for https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
p=1/3
n1=5
g_n_p= sum(((1-p)**(n-1))*p for n in range(1,n1+1))
print(round(g_n_p,3))