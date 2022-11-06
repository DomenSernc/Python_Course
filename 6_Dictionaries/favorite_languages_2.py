favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
#method items returns a list of key-value pairs
    print(f"{name.title()}'s favorite language is {language.title()}.")
