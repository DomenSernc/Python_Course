bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
#[] in the () represents an index of an element in the list

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
#python considers the first item in the list to have an index of 0, the second has an index of 1 etc.

print(bicycles[-1])
#By asking for the item at index -1, Python always returns the last item in the list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)