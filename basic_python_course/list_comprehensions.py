squares = [n**2 for n in range(10)]
print("squares =", squares)

squares_tuple = (n**2 for n in range(10)) #not really working i guess
print("squares tuple =", squares_tuple)


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(planet) < 6]
print("short_planets", short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print("loud_short_planets", loud_short_planets)

mystery_list = [1 for planet in planets]
print("[1 for planet in planets] =", mystery_list)


def count_negatives_long(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives_short(nums):
    return len([num for num in nums if num < 0])

print("count_negatives_short([1, 2, -3, 4, -5]): there are ", count_negatives_short([1, 2, -3, 4, -5]), "negative numbers")