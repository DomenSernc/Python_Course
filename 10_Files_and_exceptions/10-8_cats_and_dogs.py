try:

    with open ("dogs.txt") as filename_1:
        list_1 = filename_1.read()
        #we store the functions we perform in a certain variable (filename_1 in this case) to another variable (list_1). This makes our further
        #usage of variables easier; with calling list_1 variable we actually call the filename_1.read()
    print(list_1)

    with open("cats.txt") as filename_2:
        list_2 = filename_2.read()

    print(list_2)

except FileNotFoundError:
    print("The file is missing!")
