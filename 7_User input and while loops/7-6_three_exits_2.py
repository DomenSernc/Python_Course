question = ("What kind of toppings would you like on your pizza? ")
question += ("\n Enter 'quit' to end the program: ")

active = True
    #flag is set to true
while active:
    #while flag is true perform this:
    topping = input(question)
    #variable topping is the input word we input for the question variable. "input" method should always be before the variable in
    #the brackets

    if topping == "quit":
        # == is a comparison operator which compares values of two operands
        active = False

    else:
        print(f"Adding {topping} to your pizza!")