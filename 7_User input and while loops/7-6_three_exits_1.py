question = ("What kind of toppings would you like on your pizza? ")
question += ("\n Enter 'quit' to end the program: ")

topping = " "
while topping != "quit":
    topping = input(question)
    print(f"Adding {topping} to your pizza!")