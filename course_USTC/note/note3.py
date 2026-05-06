import pandas as pd

a = [['张三',18],['李四',20],['王五',22],['赵六',24]]
b = pd.DataFrame(a, columns=['姓名','年龄'])
print(a)
print(b)

data1 = {'姓名':['张三','李四','王五','赵六'],'年龄':[18,20,22,24]}
c = pd.DataFrame(data1)
print(c)

# 列表嵌套字典： 某行中某数据缺失(Nan)
data2 = [{'张三':'M','李四':'F'},{'张三':'18','李四':'20','王五':'22'}]
d = pd.DataFrame(data2, index=['性别','年龄'])
print(d)

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['A','B','C'], index=['X','Y','Z'])
print(df)
e = df.to_numpy()   # 将 DataFrame 转换为 NumPy 数组
print(e)

df1 = pd.DataFrame({'A':[1,2,3]}, index=[1,2,3])
df2 = pd.DataFrame({'A':[1,2,3]}, index=[3,1,2])
print(df1-df2)   # 结果是一个新的 DataFrame，索引对齐后进行元素级的减法运算

# 通过series创建DataFrame: 某列中某个数据缺失(Nan)
f = {'Name' : pd.Series(['张三','李四','王五'], index=['1st','2nd','3rd']), 
     'Age' : pd.Series([18,20,22,24], index=['1st','2nd','3rd','4th'])}
df3 = pd.DataFrame(f)
print(df3)