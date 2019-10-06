# In this Mnist data set of hand-written digit is used

import pandas as pd

df=pd.read_csv("C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/train.csv")
print(df.shape)

#Converting it into matrix

M=df.values

#Selecting the first image

im1=M[0,1:]
im1=im1.reshape(28,28)

import matplotlib.pyplot as plt
print(M[0,0])
plt.imshow(im1, cmap='gray')
plt.show()