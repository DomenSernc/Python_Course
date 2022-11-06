question = ("What kind of toppings would you like on your pizza? ")
question += ("\n Enter 'quit' to end the program: ")

while active:
    
    topping = input(question)

    if topping == "quit":
    
        active = False

    else:
        print(f"Adding {topping} to your pizza!")