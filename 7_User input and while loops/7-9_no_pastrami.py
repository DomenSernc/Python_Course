sandwich_orders = ["vegi", "pastrami", "poli", "pastrami", "tuna", "pastrami"]

print("Our Deli has run out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)