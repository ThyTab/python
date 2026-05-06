# number string list tuple dict set

# number: int float bool complex
a, b, c, d = 1, 2.2, True, 2+1j
print(a, b, c, d)
print(type(a), type(b), type(c), type(d)) 
# int无限精度   bool类型是int类型的子类型,可直接与整形进行计算
print(d.real,d.imag)
print('-'*100)

# string: 字符串是不可变的
a = 'hello'
b = "world"
c = '''
hello
world
'''   # 三引号可以换行
print(a, b, c)
print(type(a), type(b), type(c))
print(a*2)   # 两个a拼接
print(a+' '+b)   # 字符串拼接
print(f'we say {a} when we come to this {b}.')
print('-'*100)

# list: list中的元素可以是不同数据类型的
list = ['abcd', 1, 2.2, False, 2+1j, 'python']
print(list)
print(list*2)
print(list + ['hello', 4.3])
list.append(10)
print(list)
print('-'*100)

# tuple: 不可变、小括号

# set(集合): 无序、不重复   集合可变、集合中的元素不可变   元素可以是任意数据类型
setA = {1,2,3,4,5}
print(type(setA))
setB = set([4.3, 1, "hello world"])
print(setB)
print(setA&setB)   #交集
print(setA|setB)   #并集
print(setA-setB)   #差集
print(setA^setB)   #对称差集
print('-'*100)

# dictionary: key-value
person = {'name':'tom', 'age':20, 'gender':'male'}
print(person['name'])
print(person.keys())
print(person.values())
print(person.items())
person['height'] = 180
print(person)
del person['age']
print(person)
person.clear()
print(person)
del person   # 销毁释放哈希空间

