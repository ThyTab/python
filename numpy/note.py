import numpy as np

#数组内各元素的数据类型必须相同，与列表不一样
#利用array()函数创建数组，传入参数为列表
list = [10,20,30,40]
array1 = np.array(list)
array2 = np.array([1,2,3,4])
print(array1 + array2)

#维度与形状
array_0d = np.array(100)
array_1d = array1 + array2
array_2d = np.array([[1,2,3,4],[2,4,6,8],[3,4,5,6]])
array_3d = np.array([[[1,2,3],[2,3,4]],[[4,3,2],[1,8,9]]])
print(array_0d)
print(array_1d)
print(array_2d)
print(array_3d)
#直接打印维度   注意：ndim适应没有小括号()
print(array_0d.ndim)
print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)
#查看数组形状  利用数组的shape属性
print(array_0d.shape)
print(array_1d.shape)
print(array_2d.shape)
print(array_3d.shape)

#利用arange()函数创建数组 
arr1 = np.arange(100)   #从零开始，不包括100
arr2 = np.arange(0,100,2)
arr3 = np.arange(0,100,2.5)   #python中步长不能是浮点数，numpy可以
print(arr3)
#利用dtype属性查看数组内元素的数据结构
print(arr2.dtype)
print(arr3.dtype)
#利用size属性查看元素数量
print(arr1.size)
#重塑数组（将一维数组变为多维数组），首先要知道数组的元素数量
arr1_2d = arr1.reshape(10,10)
arr1_3d = arr1.reshape(2,5,10)
print(arr1_2d)
print(arr1_3d)

#设置默认值
zero = np.zeros(8)   #元素均为0的一维8个元素的数组
one = np.ones((2,3))   #元素均为1的二维且两行三列的数组
nine = np.full((2,3,4),9)   #元素均为9的三维且2*3*4数组
print(zero)
print(one)
print(nine)

#定义数组是设置数据类型
arr_set = np.array([1,2,3],dtype=np.float64)
print(arr_set)
print(arr_set.dtype)

#创建随机数数组
random_arr1 = np.random.random((3,4))   #从0.0到1的浮点数，不包括1
random_arr2 = np.random.randn(3,4)   #有负数，标准正态分布  注意：此函数不要多加一层括号
random_arr3 = np.random.randint(2,34,size=(3,4))   #2到33的整数随机
print(random_arr1)
print(random_arr2)
print(random_arr3)

#索引 先行后列   [...,...]或[...][...] (后者对单个索引)  从0开始
students = [1,2,3,4,5,6]
Math = [99,56,22,56,88,23]
English = [28,46,96,20,47,86]
Sport = [95,57,29,58,33,48]
score = np.array([students,Math,English,Sport])
print(score)
print(score[1][2])
print(score[1,2])
print(score[1:4,2])
print(score[1:,2])
print(score[:,::2])   #此处2为步长
#可直接对数组进行加减乘除与条件判断，得到的依旧是一个数组，此数组各元素即为各元素对应的计算
a = np.array([[1,2,3],[-1,-2,-3]])
b = np.array([[2,4,6],[1,3,5]])
print(a)
print(b)
print(a+b)
print(a*b)
print(a>1)   #返回的数组的个元素为布尔值
print((b>1)&(b<5))   #只能用&，且两个条件都要用小括号括起来
mask = (b>1)&(b<5)
print(b[mask])   #将布尔数组作为索引码，可输出满足条件的元素，不过均在一维数组中
#使用where函数，传入三个参数用于对数组元素进行挑选,此函数返回数组
#参数：筛选条件，操作数组，不满足条件的调换为的数字
c = np.where(mask,b,0)
d = np.where(mask,b,np.nan)   #nan也是一种数据类型，表示not a number
print(c)
print(d)
print(np.argwhere(mask))   #此函数自动输出所有满足条件的索引 注意：不用传入b,因为mask本身就对应b

#赋值
print(a)
a[0,0]=2   #单个赋值
a[1,:] = [8,8,8]   #切片赋值，注意格式匹配
print(a)
a[a>7] = 10   #条件赋值
print(a)
a[1,:] = 8   #将所有指定元素赋值为同一个数，注意不能是[8]
print(a)

#广播   将形状不同的数组进行运算
'''
能使用广播机制进行运算的维度不一致数组的规则：
(1)将较小维度的数组用“1x”表示
(2)从后往前对比维度
(3)如果维度不一致，其中一个为1，则可拓展，否则报错
'''
eye = np.eye(5)   #自动创建5*5的单位阵
print(eye)
print(eye + np.array([1,2,3,4,5]))   # 5*5与1*5进行计算
x = np.array([[1,2,3],
              [3,4,5]])
y = np.array([[[1,2,3],[2,3,4]],[[4,5,6],[5,6,7]]])
print(x+y)   #2*2*3与2*3进行计算

#数学函数
print(np.sum([1,2,3]))   #求和
print(np.mean([1,2,3]))   #平均值
print(np.std([1,2,3]))   #标准差
print(np.max([1,2,3]))   #最大值
print(np.min([1,2,3]))   #最小值
print(np.exp([1,2,3]))   #指数  对每个元素运算e的次方
print(np.log([1,2,3]))   #对数  对每个元素计算ln对数
print(np.sqrt([1,2,3]))   #平方根
print(np.abs([-1,2,3]))   #绝对值

z = np.array([1.5,2.3,3.7])
print(np.round(z))   #四舍五入
print(np.floor(z))   #向下取整
print(np.ceil(z))   #向上取整
print(np.clip(z,2,3.5))   #裁剪，小于2变成2，大于3.5变成3.5

#线性代数基础
u = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
print(np.dot(u,v))   #矩阵乘法(只要两个参数矩阵满足结构符合矩阵乘法要求即可)
print(u@v)   #矩阵乘法等价写法
m = np.array([1,2])
n = np.array([0.3,0.5])
print(np.dot(m,n))   #向量点乘
print(np.linalg.norm(m))   #向量模长
print(np.linalg.norm(m-n))   #计算距离

l1 = np.linalg.solve(u,m)   #求解线性方程组 ux=m
print(l1)
invu = np.linalg.inv(u)   #求逆矩阵
l2 = np.dot(invu,m)
print(l2)   #通过矩阵运算求解线性方程组

print(u.T)   #转置矩阵
print(np.diag([1,2,3]))   #对角矩阵

#特征值分解与奇异值分解
A = np.array([[1,2],[3,4]])
B = np.array([[1,2,3],[4,5,6]])
#特征值分解：针对方阵
eigenvalues,eigenvectors = np.linalg.eig(A)   #第一个参数返回由特征值组成的一维数组，第二个是二维数组，每一列是特征向量
print(eigenvalues)
print(eigenvectors)
#奇异值分解：非方阵同样适用
U,S,VT = np.linalg.svd(B)   #分别返回左奇异矩阵、奇异值组成的一维数组、右奇异矩阵的转置
print(U)
print(S)
print(VT)

#常用工具函数
#数组合并与拆分
#排序与去重
#描述性统计
#随机数控制