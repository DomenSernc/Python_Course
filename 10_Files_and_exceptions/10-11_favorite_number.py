import json

filename = "favorite_number.json"
fav_number = input ("What is your favourite number? ")

with open (filename, "w") as f:
    json.dump(fav_number, f)


