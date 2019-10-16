from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
'''
print(norm.pdf(0))

r=np.random.randn(10)
print(norm.pdf(r))
print(norm.cdf(r))

r2=np.random.randn(1000000)

plt.hist(r,bins=100)
plt.show()
'''

r=np.random.randn(10000,2)
plt.scatter(r[:,0], r[:,1])
plt.show()


