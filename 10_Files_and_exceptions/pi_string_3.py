filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#We create a loop that adds each line of digits to pi_string and removes the newline character from each line

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
#we prompt for the user's birthday and then we check if that string is in pi_string
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")