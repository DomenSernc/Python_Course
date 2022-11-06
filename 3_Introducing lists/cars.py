cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#the order of the lists is permanently changed; meaning that the ORIGINAL order of the list cannot be retrieved!

cars.sort(reverse=True)
print(cars)
#same as the above; permanently changed

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
#sorted function displays lists in an alphabetical order

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

len(cars)