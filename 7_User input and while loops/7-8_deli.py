sandwich_orders = ["vegi", "poli", "tuna"]
finished_sandwiches = []

while sandwich_orders:
    preparation = sandwich_orders.pop()
    finished_sandwiches.append(preparation)

    for sandwich in sandwich_orders:
        print(f" I made you a {sandwich} sandwich.")

print(finished_sandwiches)
print(sandwich_orders)
#here we printed the lists to make sure that we really moved sandwiches from sandwich_orders to finished_sandwiches