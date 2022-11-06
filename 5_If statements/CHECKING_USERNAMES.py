current_users = ["Domen", "jacob", "unbroken", "player_10", "geek"]

new_users = ["sara", "benjamin", "unbroken", "klara", "DOMEN"]

for user in new_users:
    if user in current_users:
        print("The username is already taken! Please enter another username to proceed.")
    else:
        print("The username is available!")

#i didn't solve this problem - page 89: "Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#current_users containing the lowercase versions of all existing users.)"