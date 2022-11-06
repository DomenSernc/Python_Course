pizzas = ["classic", "margharita", "pepperoni"]
friend_pizzas = pizzas[:]
for pizza in pizzas:
    print(f" I like {pizza} pizza.")
print("This statement is outside the loop. Therefore it is written only once since its code is not written intendedly. Pizza rocks.")


pizzas.append("greek")
friend_pizzas.append("detroit")
print(pizzas)
print(friend_pizzas)

print(f"My favourite pizzas are {pizzas}.")
print(f"My friend's favourite pizzas are: {friend_pizzas}")



