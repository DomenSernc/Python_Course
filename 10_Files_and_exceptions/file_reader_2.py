with open("learning_python.txt") as file_object:
#Here, open('pi_digits.txt') returns an object representing pi_digits.txt. Python assigns this object to
#file_object, which we’ll work with later in the program.
    for line in file_object:
        line.replace("Python", "C")