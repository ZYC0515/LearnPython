#motorcycles.py

#对列表元素的修改
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print("\n")


#对列表元素的增添
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')#append()是添加到列表末尾
print(motorcycles)
print("\n")


#对列表元素的指定位置插入
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')#insert()可在任意位置插入新元素
print(motorcycles)
print("\n")


#对列表元素的删除
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]#第一个元素删除
print(motorcycles)
print("\n")

#用del 来删除列表元素后，被删除的列表元素将无法再被访问到

#对列表元素的删除（pop()出最末尾的元素，仍然可以被访问到。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
print(motorcycles.pop())#最末端元素的删除
print("\n")

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycles I foud owned was a "+last_owned.title()+".")
print("\n")

#根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("\n")





motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too birthay for me")


















print("\n")













