from learning.functions_passed_to_functions import squared_call, mult_by_five
from my_functions import read_string_from_file, generic_procedure, least_difference

help(least_difference)
print("least_difference(55, 4, 21)")
print(least_difference(55, 4, 21))

print("\nread_string_from_file(\"test.txt\")")
print(read_string_from_file("resources/test.txt"))

print("type(generic_procedure()): ", str(type(generic_procedure())))

test = squared_call(mult_by_five, 1)
print("squared_call(mult_by_five, 1) = ", test)

max_abs = max(100, -1000, 1, key=abs)
print("max(100, -1000, 1, key=abs) = ", max_abs)

