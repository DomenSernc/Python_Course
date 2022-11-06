import json
#here we import the json module

filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f)

print(numbers)