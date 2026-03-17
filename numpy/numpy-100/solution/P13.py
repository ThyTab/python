import numpy as np

np.random.seed(23)
a = np.random.randint(-100,101,(10,10))
min = a.min()
max = a.max()

print(a)
print(f"min:{min},max:{max}")