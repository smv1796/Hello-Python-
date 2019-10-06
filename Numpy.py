import numpy as np
from datetime import datetime
#Starting of function definitions
'''
def magnitude(a):
    mag=0
    for e in a:
        mag+=e**2
    mag=np.sqrt(mag)
    return mag

def dotProduct(A,B):
    dotP=0
    for e,f in zip(A,B):
        dotP+=e*f
    return dotP

def diffinmethods(A,B):
    T=1000

    tb=datetime.now()
    for r in range(T):
        dotProduct(A,B)
    te=datetime.now()

    duration1=te-tb

    tb=datetime.now()
    for r in range(T):
        np.dot(A,B)
    te=datetime.now()

    duration2=te-tb

    print("Predefined dot is", duration1/duration2,'times faster than our method for calculating dot product')



#

L=[1,2,3]
A=np.array(L)

for ele in L:
    print(ele)


for ele in A:
   print(ele)

L.append(17)

print(L)
L=L+L
#print(L)

A=A+A
#print(A)


a=np.array([1,2])
b=np.array([2,1])
result=0;
for e1,e2 in zip(a,b):
    result+=e1*e2

print("result is:",result)

r=a*b;
dotP=0
for e in r:
    dotP+=e

print(dotP)

# numpy has predefined function to calculate dot product

print(np.dot(a,b))

#Finding the angle b/w two vectors

maga=np.linalg.norm(a)
maga1=magnitude(a)

if maga==maga1:
        print("Both the methods produce same result")
else:
    print("Methods prodeuce different result")

magb=np.linalg.norm(b)

costheta=(np.dot(a,b))/(maga*magb)
print("The cosine of the angle b/w two vectors is",costheta)

#Example problem
A=np.array([[1.5,4.0],[1,1]])
B=np.array([5050,2200])
X=np.linalg.solve(A,B)
print(X[0])

# Comparing dot product methods

a = np.random.randn(100)
b = np.random.randn(100)
#diffinmethods(a,b)

#Matrix multiplication
'''
m1=np.array([[1,2,3],[1,2,3],[1,2,3]])
m2=np.array([[2,13],[9,0,1]])

#print(np.dot(m1,m2))
#print(np.outer(m1,m2))
#print(np.trace(m1)
print(np.linalg.inv(m1))

