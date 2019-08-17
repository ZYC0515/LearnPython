#cars.py
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car=='bmw')
        print(car.upper())
    else:
        print(car=='bmw')
        print(car.title())
# 在Python中检查相等时是区分大小写的，若要实现不区分大小写，可以将要识别的变量值转化为小写，在做比较
#car.lower() = 'audi'

