#test_8_12.py
def sandwiches_order(*toppings):
    print("The sandwich will be made up of following toppings:")
    for topping in toppings:
        print(topping)

sandwiches_order('sugar','chocolate')
