import numpy as np

a = np.array([1,2,0,0,4,0])
print(np.argwhere(a!=0).reshape(-1))
print(np.nonzero(a))