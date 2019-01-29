import sys
data = sys.stdin.readlines()
print(data)
list_len=int(data[0].strip())
X=list(map(float, data[1].strip().split(' ')))
Y=list(map(float, data[2].strip().split(' ')))
print(X)
print(Y)