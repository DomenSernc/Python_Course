height = input("How tall are you, in inches? ")

height = int(height)
#here we tell that the input under variable height is an integer, so we can compare it to integer in the code below

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")