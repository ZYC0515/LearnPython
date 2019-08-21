#test_7_9.py
sandwich_orders = ['sandwich_A','pastrami','sandwich_B',
                   'pastrami','sandwich_C','pastrami']

print("'pastrami'has been sold out !")

while 'pastrami' in sandwich_orders :
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
