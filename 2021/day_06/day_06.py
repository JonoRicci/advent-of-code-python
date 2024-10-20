"""
Day 06

"""

import timeit
from collections import defaultdict, Counter
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    start_time = timeit.default_timer()

    puzzle_input = import_list()
    logger.debug(puzzle_input)

    logger.info(
        f"Part 1: 80 days gives a total of "
        f"{new_lanternfish(puzzle_input, 80)} fish."
    )

    logger.info(
        f"Part 2: 256 days gives a total of "
        f"{new_lanternfish(puzzle_input, 256)} fish."
    )

    stop_time = timeit.default_timer()

    logger.info(f"Execution time: {stop_time - start_time} seconds.")


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


def new_lanternfish(puzzle_input: list, days: int) -> int:
    """
    Extract the list of fish ages from the puzzle input.
    Rather than add to the existing list with new numbers, instead create a new
    dictionary where each key is the days left (0 to 8) and the value
    is the total count of fish at that age.

    Then iterate over each day adding fish to the dictionary.

    :param puzzle_input: Single list of comma separated numbers.
    :param days: Number of days to run simulation for.
    :return: total number of fish
    :rtype: int
    """

    list_of_ages = []

    for line in puzzle_input:
        line = line.split(",")
        for number in line:
            list_of_ages.append(int(number))

    logger.debug(list_of_ages)
    list_of_ages = Counter(list_of_ages)

    for day in range(days):
        # Dict key = age, value = fish of that age
        lanternfish_age_tracker = defaultdict(int)
        for fish_age, count in list_of_ages.items():
            if fish_age == 0:
                lanternfish_age_tracker[6] += count
                lanternfish_age_tracker[8] += count
            else:
                lanternfish_age_tracker[fish_age - 1] += count
        list_of_ages = lanternfish_age_tracker

    return sum(list_of_ages.values())


if __name__ == "__main__":
    main()
