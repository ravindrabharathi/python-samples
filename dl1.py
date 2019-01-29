from sklearn import tree
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.neighbors import KNeighborsClassifier


X=[[181,80,44],[177,70,43],[160,60,38],
   [154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],
   [171,75,42],[181,85,43]]

Y=['male','female','female','female','female','male',
   'male','male','female','male']

clf= tree.DecisionTreeClassifier()

eclf=tree.ExtraTreeClassifier()

nbclf= GaussianNB()

bclf= BernoulliNB()

mclf= MultinomialNB()

clf=clf.fit(X,Y)

eclf=eclf.fit(X,Y)

nbclf=nbclf.fit(X,Y)

bclf=bclf.fit(X,Y)

mclf=mclf.fit(X,Y)

nnclf=KNeighborsClassifier()

nnclf=nnclf.fit(X,Y)



prediction = clf.predict([[177,90,44]])

prediction2 = nbclf.predict([[177,90,44]])

prediction3=eclf.predict([[177,90,44]])

prediction4=bclf.predict([[177,90,44]])

prediction5=mclf.predict([[177,90,44]])

prediction6=nnclf.predict([[177,90,44]])

print(prediction)

print(prediction2)

print(prediction3)

print(prediction4)

print(prediction5)

print(prediction6)