#amusement_park.py
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#V2 只有一个输出口，易于维护。

age = 12
if age < 4:
    price = 0
elif age < 17:
    price = 5
else :
    price = 10

print("Your admission cost is $"+str(price)+".")

#V3 多个elif
age = 12
if age < 4:
    price = 0
elif age < 17:
    price = 5
elif age < 65:
    print = 10
else :
    price = 5

print("Your admission cost is $"+str(price)+".")

#V4 改写else 避免无效和恶意的数据
age = 12
if age < 4:
    price = 0
elif age < 17:
    price = 5
elif age < 65:
    print = 10
elif age >= 65 :
    price = 5

print("Your admission cost is $"+str(price)+".")
