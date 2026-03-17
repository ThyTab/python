import numpy as np

today = np.datetime64('today')
yesterday = np.datetime64('today') - np.timedelta64(1, 'D')
tomorrow = np.datetime64('today') + np.timedelta64(1, 'D')

print(yesterday)
print(today)
print(tomorrow)