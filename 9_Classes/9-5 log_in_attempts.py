class User:
    """A class representing a user on our website"""
    def __init__ (self, first_name, last_name, age, email, login_attempts):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        print (f"Name : {self.first_name}\n surname: {self.last_name} \n age: {self.age} \n email: {self.email} \n login_attempts: {self.login_attempts} ")

    def greet_user(self):
        print(f"Hey, {self.first_name} {self.last_name}, how are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
#if we want to add up we MUST use the += function, only using + will not work!!

    def reset_login_attempts(self):
        self.login_attempts = 0


user_2 = User ("Jacob", "Smith", 32, "smith@mail.com", 10 )
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
#here we

user_2.describe_user()

user_2.reset_login_attempts()
user_2.describe_user()


