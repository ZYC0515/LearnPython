#test_6_1.py

people = []

eason = {'first_name':'eason',
         'last_name':'zhu',
         'age':20,
         'country':'China'
         }

print(eason['first_name'])
print(eason['last_name'])
print(eason['age'])
print(eason['country'])

kris = {'first_name':'kris',
         'last_name':'wu',
         'age':30,
         'country':'China'
         }

andy = {'first_name':'andy',
         'last_name':'liu',
         'age':45,
         'country':'China'
         }

people.append(eason)
people.append(kris)
people.append(andy)

for person in people:
    print(person)
