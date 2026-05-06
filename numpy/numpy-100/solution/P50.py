import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
n = 10*np.random.random(1)
print(f'目标:{n}')
print(f'最接近的数:{a[np.argmin(np.abs(a-n))]}')

