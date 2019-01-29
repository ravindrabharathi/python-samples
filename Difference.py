class Difference:
    def __init__(self,a):
        self.__elements=a
        #self.__maximumDifference=0
    def computeDifference(self):
        a=self.__elements
        a.sort()
        n=len(a)


        setattr(self, 'maximumDifference',a[n-1]-a[0] )
        #return self.__elements





_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)


#print(d.maximumDifference)