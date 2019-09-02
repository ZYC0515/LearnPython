class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("It's cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant_1 = Restaurant('KFC', 'Fried chicken')
restaurant_2 = Restaurant('McDonald', 'Hamburger')
restaurant_3 = Restaurant('Subway', 'Sandwiches')



restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
