players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#slice function to "slice" specific elements from the list