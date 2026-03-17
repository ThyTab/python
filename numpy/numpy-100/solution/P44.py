import numpy as np

np.random.seed(0)
a = np.random.randint(0,10,(10,2))
print(a)
b = np.zeros((10,2))
b[:,0] = np.sqrt(a[:,0]**2 + a[:,1]**2)
b[:,1] = np.arctan2(a[:,1],a[:,0])
print(b)