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

class IceCreamStand(Restaurant):
    """An icecream stand using the code from excercise 9-1"""

    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def display_flavors(self):
        print(f"Flavors of available icecream are: {self.flavors}.")

icecreamery = IceCreamStand("Coldy", "all sorts of icecream")
icecreamery.describe_restaurant()
icecreamery.display_flavors()

    



