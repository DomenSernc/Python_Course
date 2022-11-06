banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    #If the value of user is not in the list banned_users, Python returns True and executes the indented line.
    print(f"{user.title()}, you can post a response if you wish.")