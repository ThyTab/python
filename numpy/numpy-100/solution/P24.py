import numpy as np

np.random.seed(0)
a = np.random.randint(0,10,(5,3))
b = np.random.randint(0,10,(3,2))
print(a@b)