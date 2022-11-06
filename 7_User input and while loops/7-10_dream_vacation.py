answers = []

polling_active = True

while polling_active:

    prompt = input("If you could visit one place in the world, where would you go? ")
    answers.append(prompt)

    repeat = input("Would you like to visit any other places? (Yes/No) ")
    if repeat == "no":
        polling_active = False
    
print("--- Poll Results ---")
print(f" You would like to visit the following countries: {answers}")

