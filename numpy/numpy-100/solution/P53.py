import numpy as np

# attention
Z = (np.random.rand(10)*100).astype(np.float32)
Y = Z.view(np.int32)
Y[:] = Z
print(Y)
# 若不是 in place，可直接用astype进行类型转换