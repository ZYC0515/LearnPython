#test_6_10.py

favorite_numbers = {'Eason':[3,4,6,7],
                    'John' :[5],
                    'Nancy':[4,6],
                    'Brown':[3,9,32],
                    'Jack':[55,1],
                    }

for name,numbers in favorite_numbers.items():
    print(name + "'s favorite numbers are:")
    print(numbers)
