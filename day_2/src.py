import os
from enum import Enum

class ReportDirection(Enum):
    INCREASING = 1
    DECREASING = -1

def verify_report_direction(element_0, element_1, report_direction):
    current_direction = None
    if element_0 < element_1:
        current_direction = ReportDirection.INCREASING
    else:
        current_direction = ReportDirection.DECREASING

    return current_direction == report_direction

def check_report_safety(report):
    report_direction = None

    # Determine report direction
    if report[0] < report[1]:
        report_direction = ReportDirection.INCREASING
    else:
        report_direction = ReportDirection.DECREASING

    # Iterate through report and check direction stays the same and changes are within reasonable jumps
    for i in range(len(report) - 1):
        if not verify_report_direction(report[i], report[i+1], report_direction):
            return False
        
        if not abs(report[i] - report[i+1]) < 4 or not abs(report[i] - report[i+1]) != 0:
            return False
        
    return True

def main():
    # Part 1
    # Identify path to puzzle input and read in data
    src_dir = os.path.dirname(os.path.realpath(__file__))
    input_data = open(os.path.join(src_dir, 'puzzle_input.txt'), 'r').readlines()

    # Format data for puzzle
    input_data = [line.split() for line in input_data]
    reports = [[int(x) for x in report] for report in input_data]

    # Check report safety for each report
    safety_list = [check_report_safety(report) for report in reports]

    # Calculate total number of safe reports
    number_of_safe_reports = sum(safety_list)
    print(f'Result for part 1: {number_of_safe_reports}')

if __name__ == '__main__':
    main()