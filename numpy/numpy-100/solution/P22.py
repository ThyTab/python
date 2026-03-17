import numpy as np

# attention
np.random.seed(0)
a = np.random.random((5,5))
print(a)

mean = a.mean()
std = a.std()
print((a-mean)/std)