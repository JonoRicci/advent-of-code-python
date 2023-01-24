"""
Day 02

"""


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    planned_course_list = import_list()

    multiply_final = calculate_multiply_final(planned_course_list)
    print(f"Part 01: The multiple is {multiply_final}")

    aim_multiply_final = calculate_aim_multiply_final(planned_course_list)
    print(f"Part 02: The aim multiple is {aim_multiply_final}")


def import_list() -> list:
    """
    Import the puzzle input and return a list.

    :return: Puzzle input text file as list
    :rtype: list
    """
    file = open("puzzle-input", "r")
    string_list = file.read().splitlines()
    file.close()
    return string_list


def calculate_multiply_final(course: list) -> int:
    """
    Read the course of commands and calculate horizontal and depth positions.
    Multiply this value and return.

    :param course: List of commands
    :return: Multiple of horizontal and depth
    :rtype: int
    """
    horizontal = 0
    depth = 0

    for command in course:
        direction, distance = command.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        elif direction == "up":
            depth -= distance
        else:
            depth += distance
    multiple = horizontal * depth
    return int(multiple)


def calculate_aim_multiply_final(course: list) -> int:
    """
    Read the course of commands and calculate horizontal, depth and aim
    positions. Multiply this value and return.

    :param course: List of commands
    :return: Multiple of horizontal and depth
    :rtype: int
    """
    horizontal = 0
    depth = 0
    aim = 0

    for command in course:
        direction, distance = command.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += distance * aim
        elif direction == "up":
            aim -= distance
        else:
            aim += distance
    multiple = horizontal * depth
    return int(multiple)


if __name__ == "__main__":
    main()
