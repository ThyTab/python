import numpy as np

# attention
for dtype in [np.int8, np.int32, np.int64]:
    print(dtype)
    print("min:", np.iinfo(dtype).min)
    print("max:", np.iinfo(dtype).max)
    print()

for dtype in [np.float32, np.float64]:
    print(dtype)
    print("min:", np.finfo(dtype).min)
    print("max:", np.finfo(dtype).max)
    print()


