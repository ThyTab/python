import numpy as np

# 方法1：使用 errstate（推荐，局部禁用）
with np.errstate(all='ignore'):
    result = np.array([1, 0]) / np.array([1, 0])
    print(result)  # [1. inf]

# 方法2：全局设置（不推荐）
np.seterr(all='ignore')

# 恢复默认
np.seterr(all='warn')