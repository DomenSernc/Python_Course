line = "Row, row, row your boat"
print(line.count('row'))
print(line.lower().count('row'))

with open ("alice_in_wonderland.txt", encoding='utf-8') as filename:
#had to add encoding variable to avoid error
    words = filename.read()
    print(words.lower().count("the "))
#added the spacing after "the" to avoid counting "then", "there", etc....
#counting the number of the words in the files

with open ("metamorphosis.txt", encoding='utf-8') as filename:
    words = filename.read()
    print(words.lower().count("the "))

with open ("sherlock_holmes.txt", encoding='utf-8') as filename:
    words = filename.read()
    print(words.lower().count("the "))