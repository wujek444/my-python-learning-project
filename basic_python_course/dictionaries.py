#dictionaries ~= key-value maps?
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11 #add value
print(numbers.keys(), numbers.values())
numbers['one'] = 'Pluto' #modify value
print(numbers.keys(), numbers.values())

##########

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
print("'Saturn' in planet_to_initial?", 'Saturn' in planet_to_initial) #search through keys
print("'X' in planet_to_initial?", 'X' in planet_to_initial) #search through keys

#dictionaries {} #like json
#lists []
#tuples ()

numbers2 = [12, 3, 4325, 132, 13, 14, 523427, 312321]
dividable_by_7 = {number: number % 7 == 0 for number in numbers2}
print("dividable_by_7:", dividable_by_7)

numbers3 = {'one':1, 'two':2, 'three':3}
#loop over dictionary's keys:
for number_key in numbers3:
    print("{} : {}".format(number_key, numbers3[number_key]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))

#loop through key-value pairs
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))