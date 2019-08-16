#test_for_4_10.py
#4_10
players = ['charles','martina','michael','florence','eli']
print('The first three items in the list are: ')
print(players[:3])
print('Three items from the middle of the list are: ')
print(players[1:4])
print('The last three items in the list are: ')
print(players[-3:])

#4_11
pizzas = ['little mac','middle mac','big mac']
friends_pizzas = pizzas[:]
pizzas.append("super big mac")
friends_pizzas.append("super little mac")
print('My favourite pizzas are:')
for pizza in pizzas :
    print(pizza)
print("My friend's favorite pizzas are :")
for pizza in friends_pizzas :
    print(pizza)

#4_12

my_foods = ['pizza','falafel','carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foos are:")
for food in my_foods :
    print(food)


print("My friend's favorite foos are:")
for food in friend_foods :
    print(food)
