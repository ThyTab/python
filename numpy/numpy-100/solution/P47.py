import numpy as np

x = np.array([1,3,5,7,9,11,13,15])
y = x + 0.5
z = np.zeros((x.size,y.size),dtype=np.float32)
z = 1/(z + x.reshape(-1,1) - y)
print(z)