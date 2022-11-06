def make_shirt(message, size="L"):
    print(f"The shirt's size is '{size}' and it has a text '{message}' printed on it.")

make_shirt("I love Python")
make_shirt(message = "I love Python")

def make_shirt_2(size, message = "Python rocks!"):
    print(f"The shirt's size is '{size}' and it has a text '{message}' printed on it.")

make_shirt_2("L")
make_shirt_2("M")

def make_shirt_3(size, message):
    print(f"The shirt's size is '{size}' and it has a text '{message}' printed on it.")

make_shirt_3("S", "Programing for everybody")
make_shirt_3("XL", "Daniel Kahneman FTW")