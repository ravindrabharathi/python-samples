def array_left_rotation(a, n, k):
    for i in range(k):
        a=rotate_left(a)
    return a
rotate =lambda x: (x[1:]).append(x[0])
def rotate_left(x):
    y=x[1:]
    #print(type(y))
    print(x[0])
    y.append(x[0])
    #y[len(y)]=x[0]
    return y
#n, k = map(int, input().strip().split(' '))
#a = list(map(int, input().strip().split(' ')))
a=[1,2,3,4,5]
n,k=5,4
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')