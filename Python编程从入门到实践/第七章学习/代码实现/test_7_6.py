#test_7_6.py
print("\n#1")
prompt = "\nTell me what do you want to add ? "
prompt += "\n(Enter 'quit' to end the program.)"
topping = ""

while topping != 'quit':
    topping = input(prompt)
    print("We will add " + topping + ".")



        
print("\n#2")
prompt = "\nTell me what do you want to add ? "
prompt += "\n(Enter 'quit' to end the program.)"



while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("We will add " + topping + ".")

print("\n#3")
prompt = "\nTell me what do you want to add ? "
prompt += "\n(Enter 'quit' to end the program.)"
active = True


while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("We will add " + topping + ".")
