import math

'''
算术运算符:
+   -   *   /   **   %   //
除法总是返回浮点数
取模一定是正的   eg: -10%3 = 2
'''

'''
关系(比较)运算符:
==   !=   >   <   >=   <=
链式比较(python特有)   eg: 3<=x<=10
注意浮点数的比较(精度问题)
'''

'''
赋值运算:
=   +=   -=   *=   /=   %=   **=   //=
字符串可+=
赋值操作对可变对象的引用传递:不是拷贝,是别名
'''

'''
逻辑运算:
and   or   not
逻辑与:   X and Y   如果X为0则返回0(不执行后续语句),否则返回Y
逻辑或：  X or Y    如果X为非0则返回X(不执行后续语句),否则返回Y
逻辑非:   not X     如果X为0则返回1,否则返回0
'''

'''
其他运算符: 位运算   成员运算   身份运算

位运算: &   |   ^   ~   <<   >>
异或^: 不同为1,相同为0
取反~: 0变1,1变0

成员运算: in   not in   可用于字符串,列表,元组,字典,集合   字典检查键(非值)
in不会递归搜索

身份运算: is   is not    is比较对象ID(内存地址)
'''

print(math.sqrt(16))
#浮点数比较
a = 0.1 + 0.2
print(a==0.3)   #false
print(math.isclose(a,0.3))   #true
#列表赋值操作
list1 = [1,2,3]
list2 = list1   #不是拷贝,是别名
list2.append(4)
print(list1)   #[1,2,3,4]
#逻辑运算符
print(1 and 20)   #20
print(0 or 20)   #20
#成员运算in不做递归搜索
lst = [1,2,[3,4]]
print(3 in lst)   #False
#身份运算符
X = [3,4]
Y = [3,4]
Z = X
print(X is Y)   #False
print(X is Z)   #True
print(X==Y)   #True
print(X==Z)   #True
print('-'*100)

#分支结构   if-elif-else
a=-10
x=a if a>0 else -a   #三元运算符
print(x)

#循环结构   for   while
square = [x**2 for x in range(10)]
print(square)
