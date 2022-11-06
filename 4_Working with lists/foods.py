my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#We make a copy of my_foods by asking for a slice of my_foods without specifying any indices and store the copy in friend_foods

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)