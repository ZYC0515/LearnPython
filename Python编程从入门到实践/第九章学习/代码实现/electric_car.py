class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条关于汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def fill_gas_tank(self):
        print("Now the gas tank is full!")

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self,battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的信息"""
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar("tesla","model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()