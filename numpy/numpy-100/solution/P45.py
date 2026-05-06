import numpy as np

a = np.random.randint(10,100,10)
print(a)
a[np.argmax(a)] = 0
print(a)