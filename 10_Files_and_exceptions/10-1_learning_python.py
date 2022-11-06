with open ("learning_python.txt") as notebook:
#The keyword with closes the file once access to it is no longer needed.
    content = notebook.read()
print(content)

filename = "learning_python.txt"
with open (filename) as objekt:
    for line in objekt:
        print(line.rstrip())

ime_mape = "learning_python.txt"
with open(ime_mape) as file_object:
    lines = file_object.readlines()
#The readlines() method returns a list containing each line in the file as a list item
for linija in lines:
    print(linija.rstrip())