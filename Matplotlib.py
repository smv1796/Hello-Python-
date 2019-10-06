import matplotlib.pyplot as plt
import numpy as np

#Line Chart
x=np.linspace(0,10,10000000)
y=np.sin(x)
#plt.show()
#plt.plot(x,y)
#plt.show()

#plt.xlabel("Time")
#plt.ylabel("Sine value")
#plt.title("My sine function wrt time")
#plt.show()

# Scatterplot

import pandas as pd

A=pd.read_csv("C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/data_1d.csv", header=None)
A=A.as_matrix()
x=A[:,0]
y=A[:,1]
#plt.scatter(x,y)
#plt.show()

x_line=np.linspace(0,100,100000)
y_line=2*x_line+1

#plt.plot(x_line,y_line)
#plt.show()

# HISTOGRAM

#plt.hist(x)
#plt.show()

R=np.random.rand(1000)
#print(len(R))
#plt.hist(R,bins=20)
#plt.show()