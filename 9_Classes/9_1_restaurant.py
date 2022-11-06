class Restaurant:
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cousine_type):
        """A method describing restaurant_name and cousine_type"""

        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"We mainly serve {self.cousine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open.")

restaurant = Restaurant("American", "beef burger & sweet cheese")
restaurant.describe_restaurant()
restaurant.open_restaurant()

