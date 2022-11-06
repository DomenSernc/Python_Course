filename = 'programming.txt'

with open(filename, 'a') as file_object:
    #the w argument tells python we want to open the file in write mode
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")