import numpy as np

# attention
a = np.array([1.1,2.2,5.7,-1.3,0,-1.7],dtype=np.float32)
print(np.copysign(np.ceil(np.abs(a)),a))

# np.copysign(x1, x2) 返回一个数组，其元素是 x1 的绝对值，但符号与 x2 中的对应元素相同。
# np.ceil(x) 返回大于或等于 x 的最小整数。
# np.abs(x) 返回 x 的绝对值。

# print(np.where(Z>0, np.ceil(Z), np.floor(Z)))