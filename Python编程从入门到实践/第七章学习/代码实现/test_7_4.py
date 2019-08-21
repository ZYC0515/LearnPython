#test_7_4.py

prompt = "\nTell me what do you want to add ? "
prompt += "\n(Enter 'quit' to end the program.)"



while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("We will add " + topping + ".")
