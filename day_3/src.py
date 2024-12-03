import re
import os

def main():
    # Part 1
    # Identify path to puzzle input and read in data
    src_dir = os.path.dirname(os.path.realpath(__file__))
    input_data = open(os.path.join(src_dir, 'puzzle_input.txt'), 'r').read()

    # Extract all valid mul statements and pull the numbers being multiplied through regex groups
    valid_mul_params = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', input_data)

    # Cast params to integers and calculate product for each valid mul command
    products = [int(element_0) * int(element_1) for element_0, element_1 in valid_mul_params]

    # Sum products and output result of part 1
    print(f'Result for part 1: {sum(products)}')

    # Part 2
    # Update the memory to account for do() and don't() commands
    # Begin by adding do() and don't() command to beginning and end to simplify regex
    updated_memory = 'do()' + input_data + "don't"

    # Pull all data between a do() and don't() command
    operable_memory = ''.join(re.findall(r"do\(\)(?:(?!don't\(\)).)*", updated_memory, re.DOTALL))
    
    # Extract all valid mul statements and pull the numbers being multiplied through regex groups
    valid_mul_params_part_2 = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', operable_memory)

    # Cast params to integers and calculate product for each valid mul command
    products_part_2 = [int(element_0) * int(element_1) for element_0, element_1 in valid_mul_params_part_2]

    # Sum products and output result of part 1
    print(f'Result for part 2: {sum(products_part_2)}')

if __name__ == '__main__':
    main()