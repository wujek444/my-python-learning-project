list_of_many_things = [21212, 'some string', help]
print(type(list_of_many_things[0]))
print(type(list_of_many_things[1]))
print(type(list_of_many_things[2]))

list = [1, 2, 3, 4, 5]
print(list[-1])#last element

print(list[0:2]) # <0; 2)
print(list[:2]) # <0; 2)
print(list[1:]) # <1; 4)


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# All the planets except the first and last
print(planets[1:-1])

# The last 3 planets
print(planets[-3:])

print("Sorted", sorted(planets))

#print("Sum string", sum(planets)) #error (cannot sum strings)

print("Sum", "=", sum(list))

print("Max =", max(list), "Min =", min(list))

planets.append('Pluto')

print(planets)

planets.pop()

print(planets)

print("Is Earth in planets?", "Answer:", "Earth" in planets)
print("Is Kallisto in planets?", "Answer:", "Kallisto" in planets)

