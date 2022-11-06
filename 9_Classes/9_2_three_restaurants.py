class Restaurant:
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cousine_type):
        """A method describing restaurant_name and cousine_type"""

        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
    
    def describe_restaurant(self):
        print(f"Our restaurant's name is {self.restaurant_name}.")
        print(f"We mainly serve {self.cousine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open.")

restaurant_1 = Restaurant("American", "beef burger & sweet cheese")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Japanese", "sushi & rice")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Kmečka", "krvavica & krompir")
restaurant_3.describe_restaurant()