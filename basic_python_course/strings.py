multiline_string = """
test1
test2
test3 test4
"""

print(multiline_string)

#strings are immutable sequences of chars (cannot be modified as lists can be):
# Indexing
planet = 'Pluto'
print(planet[0])
# Slicing
print(planet[-3:])
# How long is this string?
print(len(planet))
# Yes, we can even loop over them
print([char + '! ' for char in planet])

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())

# all lowercase
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))

print(claim.startswith('Pluto'))
# false because of missing exclamation mark
print(claim.endswith('planet'))
print(claim.endswith('planet!'))

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)

print("/".join([day, month, year]))

print(' 👏 '.join([word.upper() for word in words]))

position = 9
print("{}, you'll always be the {}th planet to me.".format(planet, position))

###################

pluto_mass = 1.313 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.3} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))



# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

