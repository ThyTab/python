from car import Car   #导入Car类

class Battery:
    '''关于电池的类'''
    def __init__(self,battery_size=40):   #设置默认值
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
        
class ElectricCar(Car):
    '''创建一个电动汽车类，是汽车类的子类'''
    def __init__(self, make, model, year):   #与父类一致
        super().__init__(make, model, year)   #继承父类的属性和方法
        self.max_speed = 200   #为子类添加新的属性（方法亦可）
        self.battery = Battery(50)   #将实例用作属性 

#my_leaf = ElectricCar("nissan","leaf","2024")
#my_leaf.battery.describe_battery()   #将实例用作属性时的调用


