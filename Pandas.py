import numpy as np

X = []

for line in open('C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/data_2d.csv'):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)
'''
print(X)
X=np.array(X)
print(X)
'''
# Now we load the data using pandas

import pandas as pd

k=pd.read_csv('C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/data_2d.csv', header=None)
#print(type(X))
#print(X.info())
print(k.head(3))

#print(k[3][2])

M3=k.as_matrix()
print(type(M3))
#print(k.iloc[0])
#print(k.ix[0])
#print(k[[0,2]]) To get multiple columns
#L=k[[0,2]]
#print(L)
#print(type(L))
type(X[0]<5)
#print(X[X[0] < 5]) # Some problem in it not working as expected