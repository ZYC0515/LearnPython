#test_7_3.py
number = input("Please tell me a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of 10.")
else:
    print("The number " + str(number) + " isn't a multiple of 10.")
