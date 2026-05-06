import numpy as np

def distance(a1,a2):
    return np.sqrt((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2)


a = np.random.randint(0,10,(100,2))
print(a)
i, j = 1, 2
print(f'第{i+1}个点和第{j+1}个点之间的距离:{distance(a[i],a[j])}')