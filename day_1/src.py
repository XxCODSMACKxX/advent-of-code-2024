import os

# Identify path to puzzle input and read in data
src_dir = os.path.dirname(os.path.realpath(__file__))
input_data = open(os.path.join(src_dir, 'puzzle_input.txt'), 'r').readlines()

# Parse input data into two separate lists
list_0 = []
list_1 = []

for line in input_data:
    elements = line.split()
    list_0.append(int(elements[0]))
    list_1.append(int(elements[1]))

# Sort lists
list_0.sort()
list_1.sort()

# Calculate difference between each element in both lists
differences = []
for index, _ in enumerate(list_0):
    differences.append(abs(list_0[index] - list_1[index]))

# Calculate total distance
total_distance = sum(differences)

print(total_distance)