from random import choice

stevilke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']


zrebanje = []
for x in range(4):
    rezultat = choice(stevilke)
    zrebanje.append(rezultat)

print(f"Any ticket containing letters and numbers {zrebanje} wins a price!")