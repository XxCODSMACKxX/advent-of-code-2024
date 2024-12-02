import os

# Part 1

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
print(f'Result for part 1: {total_distance}')


# Part Two
list_1_counts = {}

# Create a count of each element in the second list
for element in list_1:
    if element not in list_1_counts:
        list_1_counts[element] = 1
    else:
        list_1_counts[element] += 1

# Calculate the element similarity scores between the two lists by multiplying the element in the first list by the count of the second list
element_similarity_scores = [element * list_1_counts[element] if element in list_1_counts else 0 for element in list_0]

# Calculate list similarity score by summing all element similarity scores
list_similarity_score = sum(element_similarity_scores)
print(f'Result for part 2: {list_similarity_score}')