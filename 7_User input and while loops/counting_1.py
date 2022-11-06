current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        #the continue statement tells the program to return to the beginning of the loop
    
    print(current_number)