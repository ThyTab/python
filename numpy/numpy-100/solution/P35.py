import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=np.float64)
b = np.array([6, 7, 8, 9, 10], dtype=np.float64)
print(a)
print(b)

np.add(a,b,out=b)
np.divide(a,2,out=a)
np.negative(a,out=a)
np.multiply(a,b,out=a)
print(a)