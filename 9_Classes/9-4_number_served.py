class Restaurant:
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cousine_type):
        """A method describing restaurant_name and cousine_type"""

        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"We mainly serve {self.cousine_type}.")
        print(f"We've served {self.number_served} customers today.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open.")

    def set_number_served(self, served_update):
        self.number_served = served_update

    def increment_number_served(self, guests_added):
        self.number_served += guests_added


restaurant = Restaurant("American", "Beef Burger & Sweet Cheese")
restaurant.describe_restaurant()

restaurant.set_number_served(5)
restaurant.describe_restaurant()
#above we've set the number of guests we've served today to 5 because we've write a method this way

restaurant.increment_number_served(2)
restaurant.describe_restaurant()
#the above method adds 2 guests to the total guests because of the += method which is an add up function

