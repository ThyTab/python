from electric_car import ElectricCar   #导入电动汽车类
#from electric_car import Battery,ElectricCar   #同时导入多个类
#import electric_car   #直接导入模块，此时使用类时需要用electric_car.前缀
#from electric_car import *   #直接导入模块中的每个类（不推荐）

#python标准库
from random import randint
from random import choice

my_leaf = ElectricCar('nissan','leaf',2024)
my_leaf.battery.describe_battery()

print(randint(1,6))   #打印1~6的随机整数
players = ['Peter','Tom','Alice']
print(choice(players))   #choice()以列表作为参数，并随机返回一个元素



