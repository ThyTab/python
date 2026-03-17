import numpy as np

# attention
Z = np.array([1, 2, 3, 4, 5])

# 使用 np.add.reduce（对于小数组更快）
result = np.add.reduce(Z)
print(result)  # 15