import numpy as np
a = np.array([6,2,3,5,4,8,5,2,9,1])
a[(a>=3)&(a<=8)] *= -1
print(a)