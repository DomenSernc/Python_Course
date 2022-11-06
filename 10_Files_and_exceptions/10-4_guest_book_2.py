filename = "guest_book.txt"

while True:
    name = input("What is your name?")
    if name == "quit":
        break
    else:
        with open (filename, "a") as file_object:
            file_object.write(f"{name}\n")

        print(f"Hello {name}, we hope you'll enjoy your stay!")

