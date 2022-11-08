requested_toppings = []
if requested_toppings:
    #when the name of a list is used in an if statement, Python returns True if the list contains at least one item while an emtpy
    #list evaluates to False. If Requested_toppings passes the conditional test, we run the same for loop we used in the previous example.
    #if not, else is executed.
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
