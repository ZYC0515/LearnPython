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

class Privileges():
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        print("This admin has these privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name,birth_year):
        super().__init__(first_name,last_name,birth_year)
        self.previleges = Privileges()