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

user = User("Domen", "Sernc", 28, "domenemail.gmail.com")
user.describe_user()
user.greet_user()

user_1 = User("Jan", "Sernc", 23, "janemail@gmail.com")
user_1.describe_user()
user_1.greet_user()

class Admin(User):
    """A class admin which inheritets user traits"""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can edit profile", "Can play games"]

    def show_privileges(self):
        print(self.privileges)

admin_1 = Admin("Domen", "Sernc", "28", "domen@mail.com")
admin_1.show_privileges()