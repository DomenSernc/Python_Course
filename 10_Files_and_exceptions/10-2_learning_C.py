filename = "learning_python.txt"
with open (filename) as objekt:
    list = objekt.readlines()

for line in list:
    print(line.replace("Python", "C"))



