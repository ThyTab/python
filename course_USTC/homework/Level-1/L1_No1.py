'''
1. 【优化问题】 使⽤梯度下降法求解函数 f(x)=x^4−3x^3+2 的最⼩值，并
可视化迭代过程（结合微积分与数值分析）。
'''

import matplotlib.pyplot as plt
import numpy as np

# 设置初始参数
x0 = 2   # 初始点
lr = 0.01   # 学习率
iter = 100   # 迭代次数
list_x = []   # 记录迭代过程中的 x 值

# 定义函数和导函数
def f(x):
    return x**4 - 3*x**3 + 2

def df(x):
    return 4*x**3 - 9*x**2

# 梯度下降法
x = x0
list_x.append(x)
for i in range(iter):
    x = x - lr*df(x)   # 更新参数
    list_x.append(x)   # 记录迭代过程中的x值用于可视化
print(f"最小值点: {x}")
print(f"最小值: {f(x)}")

# 可视化迭代过程
#横坐标为迭代次数，纵坐标为函数值，最终函数值收敛到最小值
plt.figure(1,figsize=(8,8))   
plt.plot(range(i+2), [f(x) for x in list_x], marker='o')
plt.xlabel('Iteration')
plt.ylabel('f(x)')
#绘制函数图像并标记迭代点
plt.figure(2,figsize=(8,8))
plt.plot(np.linspace(0,3,500),f(np.linspace(0,3,500)))
plt.scatter(list_x, [f(x) for x in list_x], color='red')  # 标记迭代点
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function and Iteration Points')
plt.show()