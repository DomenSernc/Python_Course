magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
#this first print call is executed once for each value in the list
print(f"I can't wait to see your next trick, {magician.title()}.\n")
#the last print call only prints "Carolina" statement because the print call is not intended. since Carolina is the last value associated
#with the variable magician it gets printed.