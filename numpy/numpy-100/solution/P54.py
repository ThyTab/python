import numpy as np
from io import StringIO

# attention
# Fake file
s = StringIO('''1, 2, 3, 4, 5

                6,  ,  , 7, 8

                 ,  , 9,10,11
''')
Z = np.genfromtxt(s, delimiter=",", dtype = int, filling_values = 0)
print(Z)