import json
#here we import the json module

numbers = [2, 3, 5, 7, 11, 13]
#this is the data we're going to >>dump<< = store in the file

filename = 'numbers.json'
with open(filename, 'w') as f:
    #with open filename in write mode = w
    json.dump(numbers, f)
    #here we dump the numbers list in the file numbers.json