available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
    #the if falls under for loop
        print(f"Adding {requested_topping}.")
        #the print falls under if
    else:
    #the else goes under for
        print(f"Sorry, we don't have {requested_topping}.")
        #the print falls under else

print("\nFinished making your pizza!")