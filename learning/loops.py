planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file_to_save_to = open("resources/print_to_this.txt", "w")
for planet in planets:
    print(planet, end = ' ', file = file_to_save_to) # print all on same line
file_to_save_to.close()

#######################
#w - overwrites
#a - appends
#r - reads
with open("resources/with_file.txt", "w") as the_file:
    for planet in planets:
        the_file.write(planet + " ")


tuple = (1, 2, 3, 4)
for element in tuple:
    if element > 2: print(element)

i_counter = 0
phrase = "this is a string"
for character in phrase:
    if character == "i": i_counter += 1
print("phrase", "\"" + phrase + "\"", "contains", i_counter, "\"i\" characters!")

#in range loop
for i in range(10):
    print("current idx:", i)



dot_to_find = "lorem ipsum dolor sit. amet"
current_char = ""
idx = 0
while current_char != ".":
    current_char = dot_to_find[idx]
    print("current character:", current_char)
    idx += 1

