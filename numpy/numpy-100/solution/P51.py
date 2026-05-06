import numpy as np

type = np.dtype([('x',np.float64),('y',np.float64),('r',np.int32),('g',np.int32),('b',np.int32)])
a = np.zeros(10,dtype=type)
print(a)