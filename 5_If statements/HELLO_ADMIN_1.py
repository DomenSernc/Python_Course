usernames = []

if usernames:
    for name in usernames:
        if name == "admin":
            print("Hello admin, would you like to see a status report?")
    
        else:
            print(f"Hello {name}, welcome!")

else:
    print("We need to find some users!")