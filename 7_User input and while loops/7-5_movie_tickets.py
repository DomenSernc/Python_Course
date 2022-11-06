user_age = input("How old are you?: ")

user_age = int(user_age)

if user_age < 3:
    price = 0

elif user_age < 12:
    price = 10

else:
    price = 15

print(f"Your tickets cost {price}$")
