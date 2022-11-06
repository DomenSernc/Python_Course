filename = "guest_book.txt"

while True:
    name = input("What is your name?")
    with open (filename, "a") as file_object:
        file_object.write(f"{name}\n")

        print(f"Hello {name}, we hope you'll enjoy your stay!")


#this has the right ouput but the program is not concloded - the loop is not finished



