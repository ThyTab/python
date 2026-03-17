import pizza   #导入整个模块
from pizza import make_pizza   #从指定模块导入指定函数，此时在调用函数时无需指明模块的名字
from pizza import make_pizza as mp   #使用as给函数指定别名
import pizza as p   #为模块指定别名
from pizza import *   #导入模块中的所有函数，此时调用函数时无需使用点号

message = "Hello World!"
print(message)
print("Hello Python World!")

name1 = "ada lovelace"
name2 = "Ada Lovelace"
print(name1.title()) #title()方法以首字母大写的方式显示每个单词
print(name2.upper()) #upper()全大写
print(name2.lower()) #lower()全小写

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #python将花括号里的变量替换为其值 
#f字符串（在左引号前加字母f）：在字符串中插入变量的值
print(full_name)
print(f"Hello,{full_name}!")
print(f"Hello,{full_name.title()}!")
#换行符：\n   制表符：\t
print("Language:\n\tPyhton\n\tC\n\tJavaScript")
#删除空白：.lstrip()  .rstrip()   会保持原本字符串不变
favorite_language1 = "python "
favorite_language2 = " python"
print(favorite_language1.rstrip()) #删除右边空白
print(favorite_language2.lstrip()) #删除左边空白
#删除前缀： .removeprefix('...')
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))

x,y,z=0,0,0 #同时给多个变量赋值
print(3**2) # **表示乘方

#列表
languages = ['Python','C','JavaScript']
print(languages) #直接打印列表将带有中括号
print(languages[0]) #访问列表元素
print(languages[0].upper())
print(languages[-1]) #特殊的访问列表最后一个元素的方法  -2表示倒数第二个，以此类推
languages[1] = 'C++' #修改列表元素
print(languages)
languages.append('Latex') #在列表末尾插入元素   append()方法
print(languages)
languages.insert(1,'Matlab') #插入元素，此元素插入后的位置由数字表示   insert()方法
print(languages)
#删除元素
#del语句
del languages[0] #利用索引删除任意位置的元素
print(languages)
#pop()方法
popped_languages1 = languages.pop() #删除末尾元素并接着使用它的值  （弹出）
print(languages)
print(popped_languages1)
popped_languages2 = languages.pop(1) #删除任意位置元素并接着使用它的值  （弹出）
print(languages)
print(popped_languages2)
#remove方法   只删除第一个指定的值。若要删除的值在列表中出现多次，则需使用循环
languages.remove('Matlab') #根据值删除元素
print(languages)

#管理列表
#sort()方法   永久排序   所有值均为小写时按字母顺序排列
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print('排序后的列表：')
print(cars)
#sorted()函数   保留原列表
cars = ['bmw','audi','toyota','subaru']
print('sorted列表:')
print(sorted(cars))
#反向列表   reverse()方法
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
#确定列表的长度   len()函数
print(len(cars))
#列表相加（拼接）
list1 = [1,2,3,4]
list2 = [11,22,33,44]
print(list1 + list2)

#操作列表
#遍历列表
students = ['Peter','Alice','Tom','Thomas','David']
#相当于为for后的变量赋值
for student in students:     #名字可以任取，但student有具体含义
    print(f"{student.title()},you are really clever.")
    print(f"KEEP QUIET,{student.upper()}!\n")
print("Thank you, everyone!")

#创建数值列表
#range函数
for value in range(1,6):
    print(value)   #会打印1~5
#使用list()函数将range()的结果直接转换为列表
numbers = list(range(1,11))
print(numbers)
even_numbers = list(range(2,11,2))   #range函数可以指定步长
print(even_numbers)
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)   #打印1~10的平方
#对数值列表的简单统计计算
scores = [11,39,98,27,0,84,79]
print(max(scores))
print(min(scores))
print(sum(scores))
#列表推导式   （更简洁）
cubes = [value**3 for value in range(1,11)]
print(cubes)

#切片   列表的切片本质还是一个列表
players = ['charles','martina','michael','florence','eli']
print(players[0:3])   #只打印一部分,0,1,2
print(players[1:4])
print(players[:3])   #没有前索引自动从头开始
print(players[1:])   #没有后索引自动到末尾开始
print(players[-3:])  #打印后三个
#遍历切片
for player in players[0:3]:
    print(player.title())
#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
#friend_foods = my_foods是不行的，这样会使两个变量指向同一个列表，后续的修改会使两个变量同步修改
print(my_foods)
print(friend_foods)

#元组：不可变的列表，试图修改会报错
dimensions = (200,50)   #用小括号
for dimension in dimensions:
    print(dimension)
dimensions = (100,200)   #不能修改内部元素，但是可以重新定义元组
for dimension in dimensions:
    print(dimension) 

#if语句
#and or 检查多个条件
#检查特定的值是否在列表里
cars = ['bmw','audi','toyota','subaru']
if 'bmw' in cars:
    print('BMW')
if 'sanlun' not in cars:
    print(f"sanlun is not in cars")
#布尔值直接赋值True 和 False
#在if语句中将列表名作为条件表达式时，列表至少一个元素返回True,否则返回False
requested_toppings = []
if requested_toppings:
    print("something")
else:
    print("nothing")  

#字典：由多个键值对组成
alien_0 = {'color':'green','point':5}
print(alien_0['color'])   #访问字典
alien_0['x_position']=0
alien_0['y_position']=25   #直接添加键值对
print(alien_0)
alien_0['color'] = 'yellow'   #直接修改
print(alien_0)
del alien_0['point']   #使用del语句删除键值对
print(alien_0)
#使用get()来访问值
point_value = alien_0.get('point','No point value assigned')
print(point_value)
#get()中的两个参数：第一个表示要访问的键，若没有此键，则返回第二个参数
#当指定键不一定存在时，应用get()而不是方括号表示法

#遍历字典
for key,value in alien_0.items():
    print(f"{key}:{value}")
#items()方法会返回一个键值对列表，for循环后接两个变量，分别表示键和值
for key in alien_0.keys():
    print(key)
#keys()方法会返回一个键列表
#遍历字典时，默认遍历所有键，所有for key in alien_0.keys():与for key in alien_0:等价
for value in alien_0.values():
    print(value)
#values()方法会返回一个值列表
favorite_language3 = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',   #此逗号有无均可
}
for name in sorted(favorite_language3.keys()):
    print(name.title())   #按特殊顺序遍历字典
#使用集合（set）剔除列表中的重复项
for language in set(favorite_language3.values()):
    print(language)

#嵌套
#字典列表、列表字典、字典字典

#输入
name = input("Please enter your name: ")
print(f"Hello,{name.title()}")
prompt = "Please share your name."
prompt += "\nWhat is your first name: "   #一种创建多行字符串的方式
first_name = input(prompt)
print(f"Hello,{first_name.title()}")
#使用int()来获取数值输入
age = input("How old are you?")   #返回字符型
age = int(age)   #转换为整形
if age>=18:
    print("It's Ok.")

#while循环
prompt2 = "Tell me something, and I will repeat it back to you:"
prompt2 += "\nEnter 'quit' to end this program."
message = input(prompt2)
while message != 'quit':
    message = input(prompt2)
    if message != 'quit':
        print(message)
#break语句可退出循环，continue语句可跳过余下部分重新执行循环  

#无返回值函数
def describe_pet(pet_name,animal_type="dog"):   #可为形参提供初始值，注意指定默认值时等号左右不要有空格
    print(f"You have a {animal_type}")
    print(f"It's name is {pet_name}\n") 

describe_pet('willie')   #未指定实参值时，会使用默认值
describe_pet(pet_name='willie')

describe_pet('harry','hamster')   #位置实参
describe_pet(pet_name='harry',animal_type='hamster')   #关键字实参
describe_pet(animal_type='hamster',pet_name='harry')

#有返回值函数：返回值可以是字典  
def print_fullname(first_name,last_name,middle_name=''):   #此种写法使实参变为可选的
    if middle_name == '':
        fullname = f"{first_name} {last_name}"
    else:
        fullname = f"{first_name} {middle_name} {last_name}"
    return fullname

print(print_fullname('john','hooker','lee'))
print(print_fullname('john','hooker'))

#传递列表
want_to_eat = ['pizza','hamburger','coffee']
have_eaten = []
def eat(want_to_eat,have_eaten):
    while want_to_eat:
        current_eat = want_to_eat.pop()
        have_eaten.append(current_eat)
def show_food(have_eaten):
    print(have_eaten)
eat(want_to_eat,have_eaten)
show_food(have_eaten)    #函数中对列表做的任何修改都是永久的
#若要禁止函数修改列表，可将列表的副本作为实参传入函数（eg:  want_to_eat[:]  ）

#传递任意数量的实参
'''def make_pizza(*toppings):   # *号会使python创建一个名为toppings的元组
    print(toppings)'''
pizza.make_pizza('mushrooms','green peppers','extra cheese')   #module_name.function_name()
#若要使函数接收不同类型的实参，则接受任意数量实参的形参应放于后面

#使用任意数量的关键字实参
def build_profile(first,last,**user_info):   #两个*代表创建一个名为user_info的字典，可传入名值对
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)







