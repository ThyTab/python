import numpy as np

# attention
Z = np.zeros(10)
Z.flags.writeable = False
print(Z)