import numpy as np

# attention
 
# 创建自定义dtype
color = np.dtype([('R',np.uint8),('G',np.uint8),('B',np.uint8),('A',np.uint8)])
# 创建一个颜色数组
colors = np.array([(255,0,0,255),(0,255,0,255)],dtype=color)
print(colors)