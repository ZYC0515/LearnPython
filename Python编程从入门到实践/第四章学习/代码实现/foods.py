#foods.py

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foos are:")
print(my_foods)


print("My friend's favorite foos are:")
print(friend_foods)

#若是使用my_foods  = friend_foods 就是将两个表连接起来了，改变其中一个另一个也会跟着改
