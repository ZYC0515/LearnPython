class User():
    def __init__(self,first_name,last_name,birth_year):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.birth_year = birth_year
        self.full_name = first_name.title() + " " + last_name.title()
    def describe_user(self):
        print("Fist-Name: " + self.first_name + ".")
        print("Last-Name: " + self.last_name + ".")
        print("Birth-Year: " + str(self.birth_year) + ".")
    def greet_user(self):
        print("Hello, " + self.full_name + ".")

user_1 = User("eason","zhu",1999)
user_2 = User('kris','wu',1990)
user_3 = User("maggie",'q',1980)

user_1.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()