alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#If the key 'points' exists in the dictionary, you’ll get the corresponding value
#If it doesn’t, you get the default value.