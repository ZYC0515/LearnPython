#test_7_5.py

while True :
    age = input("Please enter your age : ")
    age = int(age)

    if age > 12:
        price = 15
        print("Your price is $" + str(price) + ".")
    elif 3 <= age <=12:
        price = 10
        print("Your price is $" + str(price) + ".")
    elif age < 3:
        price = 0
        print("Your price is $" + str(price) + ".")


