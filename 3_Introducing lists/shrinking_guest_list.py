people = ["Albert Einstein", "Elon Musk", "Bill Gates", "Yuval Noah Harari"]

message = f"Hey, {people[0]}, would you like to come to dinner tonight?"
print(message)

message = f"Hey, {people[1]}, would you like to come to dinner tonight?"
print(message)

message = f"Hey, {people[2]}, would you like to come to dinner tonight?"
print(message)

message = f"Hey, {people[3]}, would you like to come to dinner tonight?"
print(message)

print("I found a bigger dinner table so we'll be inviting more guests tonight!")

people.insert(0, "Domen Sernc")
people.insert(3, "Joe Biden")
people.append("Slavoj Žižek")
#we added people to the list using various methods

print(people)

message = f"Hey, {people[0]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[1]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[2]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[3]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[4]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[5]}, would you like to come to dinner tonight?"
print(message)
message = f"Hey, {people[6]}, would you like to come to dinner tonight?"
print(message)

print(people)

print("I can invite only 2 people to the dinner tonight since we're out of space!")

popped_person = people.pop(0)
print(f"{popped_person}, I'm sorry but I have to cancel your invitation to tonights dinner!")

popped_person = people.pop(0)
print(f"{popped_person}, I'm sorry but I have to cancel your invitation to tonights dinner!")

popped_person = people.pop(0)
print(f"{popped_person}, I'm sorry but I have to cancel your invitation to tonights dinner!")

popped_person = people.pop(0)
print(f"{popped_person}, I'm sorry but I have to cancel your invitation to tonights dinner!")

popped_person = people.pop(0)
print(f"{popped_person}, I'm sorry but I have to cancel your invitation to tonights dinner!")

message = f"{people[0]}, you're still invited to dinner tonight! "
print(message)
message = f"{people[1]}, you're still invited to dinner tonight! "
print(message)

del people[0]
del people[0]


print(people)

