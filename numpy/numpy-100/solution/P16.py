import numpy as np

np.random.seed(0)
a = np.random.randint(1,100,(10,8))
print(a)

z = np.zeros((a.shape[0]+2,a.shape[1]+2))
z[1:-1,1:-1] = a
print(z)

x = np.pad(a,1,mode='constant',constant_values=0)
print(x)