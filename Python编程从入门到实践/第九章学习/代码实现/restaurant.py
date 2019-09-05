class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self,number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Are you sure??")

    def increment_number_served(self,incre_number):
        if incre_number >= 0:
            self.number_served += incre_number
        else:
            print("Are you sure??")


    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("It's cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open.")