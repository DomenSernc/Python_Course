filename = "alice.txt"

try:
    with open(filename, encoding="uff-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")