#cars.py

#.sort()永久排序
#字母顺序排列sort()
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
print("\n")

#字母逆序排列 添加参数 (reverse = true)
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)
print("\n")

#.sorted()临时排序
cars = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars,reverse = True))
#其中的|,reverse = True|如果去掉就是字母顺序排序

print("\nHere is the original list again:")
print(cars)

print("\n")
#逆序打印列表
#reverse()
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

print("\n")
#确定列表长度
cars = ['bmw','audi','toyota','subaru']
print(len(cars))


