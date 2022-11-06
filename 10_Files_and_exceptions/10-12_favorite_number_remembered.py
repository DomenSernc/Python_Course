import json

filename = "favorite_number.json"

try: 
    with open (filename, "r") as f:
        fav_number = json.load(f)

except (json.decoder.JSONDecodeError, FileNotFoundError): 
    fav_number = input ("What is your favourite number? ")
    print("The program will remember your favorite number, try to run it again!")
    with open (filename, "w") as f:
        json.dump(fav_number, f)

else: 
    print(f"I know your favorite number, it's {fav_number}!")