number = input("Write a random number: ")
#make one space after the string for the input function so the program has a neat output
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")