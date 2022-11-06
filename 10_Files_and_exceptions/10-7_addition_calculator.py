print ("Tell me two numbers and i'll add them!")
print ("Enter 'quit' to end the program!")

while True:
    #using while true is a way of running a loop forverer unless we explicitely tell the program to end (by inputing the quit in this case)
    number_1 = input("Pick the first random number:")
    if number_1 == "quit":
        break
    number_2 = input("Pick the second random number:")
    if number_2 == "quit":
        break
    try:
        number_x = int(number_1) + int(number_2)
    except ValueError:
        print("Please provide a numerical input!")
    else:
        print(number_x)