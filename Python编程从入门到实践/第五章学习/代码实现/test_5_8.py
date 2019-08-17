#test_5_8.py

user_names = ['Eason','Mike','Donald','Micky','John','admin']

for user_name in user_names:
    if user_name == 'admin':
        print(user_name+",would you like to see a status report?")
    else:
        print(user_name+",welcome back!")
    

#5_9
user_names = ['Eason','Mike','Donald','Micky','John','admin']
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(user_name+",would you like to see a status report?")
        else:
            print(user_name+",welcome back!")
else:
    print("We need to find some users!")

#5_10
current_users = ['Eason','Mike','Donald','Micky','John']
new_users = ["Eason","Zhu","Andy","miKE","Kris"]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
         print(new_user+",you have to type in another name.")
    else:
         print(new_user+",your name is uique!")

#5_11
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")
