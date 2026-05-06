'''
2. 【数学】积分计算：使⽤ numpy、math 库等⼯具独⽴实现⼆重积分的计算,
并与 scipy.integrate ⽐较⼆重积分计算效率
提示：统计连续计算 10000 次的耗时
'''

import numpy as np
import math
import scipy.integrate
import time

# 定义被积函数
def f(y, x):
    return math.sqrt(x + y**2)

# 独立实现
def manual_double_integral():
    total = 0.0
    x_start, x_end = 0, 1
    nx = 1000
    x = np.linspace(x_start, x_end, nx, endpoint=True)
    dx = (x_end - x_start) / nx

    for xi in x:
        y_start, y_end = -xi, xi
        ny = int(2000 * (xi - x_start) / (x_end - x_start) + 1)
        y = np.linspace(y_start, y_end, ny)
        dy = (y_end - y_start) / ny
        for yj in y:
            total += f(yj + dy/2, xi + dx/2) * dx * dy
    return total

# scipy.integrate
def scipy_double_integral():
    result, _ = scipy.integrate.dblquad(f, 0, 1, lambda x: -x, lambda x: x)
    return result

# 性能比较
times = 100
# 统计手动实现耗时
start = time.time()
for i in range(times):
    result1 = manual_double_integral()
manual_time = time.time() - start
# 统计 scipy 耗时
start = time.time()
for i in range(times):
    result2 = scipy_double_integral()
scipy_time = time.time() - start

print(f'独立实现（{times}次）：{result1:.4f}')
print(f'耗时：{manual_time:.4f}秒')
print()
print(f'scipy.integrate（{times}次）：{result2:.4f}')
print(f'耗时：{scipy_time:.4f}秒')

