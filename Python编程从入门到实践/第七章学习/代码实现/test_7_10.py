#test_7_10.py

#调查问卷开始
print("------Polling-----")
active = True

responses = {}
while active:
    name = input("\nWhat's your name?")
    place = input("If you could visit one place in the world,where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (Y/N)")
    if repeat == 'N':
        active = False

print("\n-----Poll Result-----")
for name,place in responses.items():
    print(name + " would like to travel to " + place + ".")

    
