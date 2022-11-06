def build_profile(first, last, **user_info):
    #The double asterisks before the parameter **user_info cause Python to create 
    #an empty dictionary called user_info and pack whatever name-value pairs
    #it receives into this dictionary.

    """Build a dictionary about yourself."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Domen', 'Sernc',
                            location='Šenčur',
                            age = 28,
                            field='Computer Science',)
print(user_profile)