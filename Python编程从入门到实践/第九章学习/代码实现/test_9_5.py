class User():
    def __init__(self,first_name,last_name,birth_year):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.birth_year = birth_year
        self.full_name = first_name.title() + " " + last_name.title()
        self.login_attempts = 0

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1


    def describe_user(self):
        print("Fist-Name: " + self.first_name + ".")
        print("Last-Name: " + self.last_name + ".")
        print("Birth-Year: " + str(self.birth_year) + ".")

    def greet_user(self):
        print("Hello, " + self.full_name + ".")

user_1 = User("eason","zhu",1999)
print('You have ' + str(user_1.login_attempts) + " login attempts.")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print('You have ' + str(user_1.login_attempts) + " login attempts.")

user_1.reset_login_attempts()
print('You have ' + str(user_1.login_attempts) + " login attempts.")
