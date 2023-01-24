"""
Day 00

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list()
    logger.debug(puzzle_input)


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


if __name__ == "__main__":
    main()
