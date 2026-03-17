import numpy as np

a = np.zeros((5,5))
a += np.arange(5)   #广播机制

print(a)