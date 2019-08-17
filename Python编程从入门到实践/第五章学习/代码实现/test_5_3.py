#test_5_3.py
alien_color = 'green'

if alien_color == "green":
    print('You get 5 points.')

if alien_color == "red":
    print("You get 10 points.")

#5_4
alien_color = 'green'

if alien_color == "green":
    print('You get 5 points.')
elif alien_color != 'green':
    print("You get 10 points.")

alien_color = 'red'

if alien_color == "green":
    print('You get 5 points.')
elif alien_color != 'green':
    print("You get 10 points.")

#5_5
alien_color = 'green'

if alien_color == "green":
    print('You get 5 points.')
elif alien_color == 'yellow':
    print("You get 10 points.")
elif alien_color == 'red':
    print("You get 15 points.")
    
alien_color = 'yellow'

if alien_color == "green":
    print('You get 5 points.')
elif alien_color == 'yellow':
    print("You get 10 points.")
elif alien_color == 'red':
    print("You get 15 points.")

alien_color = 'red'

if alien_color == "green":
    print('You get 5 points.')
elif alien_color == 'yellow':
    print("You get 10 points.")
elif alien_color == 'red':
    print("You get 15 points.")

#5_6
age = 15

if age < 2:
    print("You are a baby!")
elif age < 4:
    print("Your are learning to walk!")
elif age < 13:
    print("You are a child!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
elif age >= 65:
    print("Your are an old man")

#5_7
favourite_fruits = ['apple','banana','peach','pinapple']
if 'peach' in favourite_fruits:
    print("You really like peach!")
if 'watermelon' in favourite_fruits:
    print("You really like watermelon!")
if 'pear' in favourite_fruits:
    print("You really like pear!")
if 'orange' in favourite_fruits:
    print("You really like orange!")
if 'apple' in favourite_fruits:
    print("You really like apple!")
if 'banana' in favourite_fruits:
    print("You really like banana!")
    
