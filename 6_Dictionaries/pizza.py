# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.

print(f"You ordered a {pizza['crust']}-crust pizza "
#callin the "crust" in square brackets returns key crust's value; "thick"
    "with the following toppings:")
    #these double paranthases above is used to break the line of the string - Python then combines it in the output.

for topping in pizza['toppings']:
    print("\t" + topping)
