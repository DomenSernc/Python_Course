favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_people = ['jen', 'benjamin', 'edward', 'kaja']

for person in poll_people:
    if person in favorite_languages:
        print("Thank you for taking the poll!")
    else:
        print("You're invited to take the poll!")