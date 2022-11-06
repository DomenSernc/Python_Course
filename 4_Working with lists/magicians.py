magicians = ["Alice", "David", "Carolina"]
for magician in magicians:
    #here we define the for loop and tell our computer to pull a name from the list magicians and assign it to a variable magician
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")
#this line of code is not intended and is therefore only printed once! because it is not intended it doesn't belong to the for loop