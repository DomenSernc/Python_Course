filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    #tt u the readlines() method takes each line from the file and stores it in a list to work with it later

for line in lines:
    #here we use a simple for loop to print each line from lines
    print(line.rstrip())