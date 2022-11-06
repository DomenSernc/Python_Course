class User:
    """A class representing a user on our website"""
    def __init__ (self, first_name, last_name, age, email):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print (f"Name : {self.first_name}\n surname: {self.last_name} \n age: {self.age} \n email: {self.email} ")

    def greet_user(self):
        print(f"Hey, {self.first_name} {self.last_name}, how are you today?")