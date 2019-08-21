#test_7_8.py
sandwich_orders = ['sandwich_A','sandwich_B','sandwich_C']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order.title() + ".")
    finished_sandwiches.append(sandwich_order)

print("The following sandwiches have been finished: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
