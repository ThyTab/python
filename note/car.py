class Car:
    '''此类用于模拟汽车'''

    #以下函数必须含self的形参
    def __init__(self,make,model,year):   #传入参数
        self.make = make
        self.model = model
        self.year = year   #定义实例的属性
        self.odometer_reading = 0   #给属性指定默认值
    #以self.为前缀的变量可供类里所有方法使用
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def increase_odometer(self,miles):
        self.odometer_reading += miles

#my_new_car = Car("audi","a4",2024)   #创建实例
'''print(my_new_car.year)   #访问属性
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(100)
my_new_car.increase_odometer(200)   #改变属性的值
my_new_car.read_odometer()   #访问方法'''


    
        