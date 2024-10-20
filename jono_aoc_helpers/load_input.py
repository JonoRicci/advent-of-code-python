"""
Helper functions for loading Advent of Code Puzzle Input.
"""

import os
from typing import List, Any


def load_puzzle_input_as_list(year: int, day: int) -> List[str]:
    """
    Load the puzzle input for the specified year and day as a list of strings.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: List of strings, where each element represents a line of the input
    """
    # Define the file path relative to the root directory of the year folder
    file_name = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        str(year),
        f"day_{day}",
        "puzzle-input",
    )
    if not os.path.exists(file_name):
        raise FileNotFoundError(
            f"Input file not found for year {year}, day {day}: {file_name}"
        )

    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]


def load_puzzle_input_as_string(year: int, day: int) -> str:
    """
    Load the entire puzzle input as a single string.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: The entire puzzle input as a string
    """
    # Define the file path relative to the root directory of the year folder
    file_name = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        str(year),
        f"day_{day}",
        "puzzle-input",
    )
    if not os.path.exists(file_name):
        raise FileNotFoundError(
            f"Input file not found for year {year}, day {day}: {file_name}"
        )

    with open(file_name, "r") as file:
        return file.read().strip()


def load_puzzle_input_as_int_list(year: int, day: int) -> List[int]:
    """
    Load the puzzle input as a list of integers, assuming each line contains one integer.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: List of integers, where each element represents a line of the input parsed as an int
    """
    # Define the file path relative to the root directory of the year folder
    file_name = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        str(year),
        f"day_{day}",
        "puzzle-input",
    )
    if not os.path.exists(file_name):
        raise FileNotFoundError(
            f"Input file not found for year {year}, day {day}: {file_name}"
        )

    with open(file_name, "r") as file:
        return [int(line.strip()) for line in file.readlines()]
