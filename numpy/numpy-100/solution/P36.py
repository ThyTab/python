import numpy as np

a = np.random.random(10)*10
print(a)

# 1
print(np.floor(a))
# 2
print(np.trunc(a))
# 3
print(np.int16(a))
# 4
print(a.astype(int))
# 5
print(a//1)
# 6
print(a-a%1)
