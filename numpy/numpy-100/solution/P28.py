import numpy as np

print(np.array(0) / np.array(0), np.array(0) // np.array(0), np.array([np.nan]).astype(int).astype(float))