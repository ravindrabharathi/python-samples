N = input()

# Get the input
numArray = map(int, input().split())
# Get L and R from the input
L, R = map(int, input().split())


numArray=list(numArray)
print(numArray,type(numArray))
sum_integer = 0
# Write the logic to add these numbers here
for i in range(int(N)):
    sum_integer +=numArray[i]**2



# Print the sum
print(sum_integer)

# Write here the logic to print all integers between L and R
s=''
for i in range(L,R):
   s +=str(i)+' '
s +=str(R)
print(s)

l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
sem=l1+l2
print(sem)