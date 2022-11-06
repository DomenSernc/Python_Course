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


class Privileges:
    def __init__(self):
        self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can edit profile", "Can play games"]
        
        #the self only means it that the variable is accessible to all class objects/instances and methods

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    """A class admin which inheritets user traits"""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email,)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)