number_1 = input("Pick the first random number:")
number_2 = input("Pick the second random number:")

try:
    number_x = int(number_1) + int(number_2)
    print(number_x)

except ValueError:
    print("Please provide a numerical input!")
