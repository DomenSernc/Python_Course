squares = []
    #squares it the name of the list
for number in range(1,11):
    #for number in range from 1 to 11
    square = number ** 2
    #square number is number from range 1 to 11 squared with number 2
    squares.append(square)
    #add to list "squares" all the results for "square" = meaning 1**2, 2**2, 3**2 etc... until 10**2
print(squares)
    #print the list "squares" which has been transformed with our program. It started as an empty list at the start of the code
    #and resulted in a full list with append function

squares = []
for value in range(1,11):
    squares.append(value**2) #this code does the same as code from line 5 and 7 combined
print(squares)

#Sometimes using a temporary variable makes your code easier to read; other times it makes the code unnecessarily long.

comprehend_squares = [stevilka**2 for stevilka in range (1,11)]
print(comprehend_squares)
