filename = "programming_poll.txt"

while True:
    reason = input("Why do you like programing?")
    if reason == "quit":
        break
    else:
        with open (filename, "a") as file_object:
            file_object.write(f"{reason}\n")