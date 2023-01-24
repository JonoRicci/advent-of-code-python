"""
Day 07

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list()
    logger.debug(puzzle_input)
    fuel_spent = fuel_to_align(puzzle_input)
    logger.info(f"Part 01: They must spend {fuel_spent} of fuel to align.")


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


def fuel_to_align(puzzle_input: list) -> int:
    """
    Extract the positions from the puzzle input.
    To calculate the best position, find the smallest distance each crab can
    travel. One way to do this is to find the median then calculate fuel spent
    for each crab to get to the median.

    :param puzzle_input: One list list of comma separated values.
    :return: Fuel spent from each crab submarine
    :rtype: int

    """
    horizontal_positions = [int(crab) for crab in puzzle_input[0].split(",")]
    horizontal_positions.sort()
    logger.debug(horizontal_positions)

    fuel_spent = 0
    median_distance = horizontal_positions[len(horizontal_positions) // 2]
    logger.info(f"Medium distance is: {median_distance}")

    for crab in horizontal_positions:
        fuel_spent += abs(crab - median_distance)

    return fuel_spent


if __name__ == "__main__":
    main()
