def sandwich_type(*ingridients):
    #ingridients is a parameter
    """Summarizing the ordered sandwich type"""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingridients:
        print(f"- {ingredient}")

#the strings in the brackets are called arguments
sandwich_type("tuna")
sandwich_type("salami", "cheese", "tomato")
sandwich_type("cheese", "radish")

