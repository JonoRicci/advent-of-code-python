"""
jono_aoc_helpers.load_input
---------------------------

This module contains methods for loading advent of code puzzle input from an existing file.
"""

import os
from typing import List
import logging

logger = logging.getLogger(__name__)


def get_puzzle_file_path(year: int, day: int) -> str:
    """
    Get the file path for the specified year and day.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: Path to the puzzle input file
    """
    file_name = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        str(year),
        f"day_{day}",
        "puzzle-input",
    )
    if not os.path.isfile(file_name):
        logger.error(f"Input file not found for year {year}, day {day}: {file_name}")
        raise FileNotFoundError(
            f"Input file not found for year {year}, day {day}: {file_name}"
        )
    return file_name


def load_puzzle_input_as_list(year: int, day: int) -> List[str]:
    """
    Load the puzzle input for the specified year and day as a list of strings.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: List of strings, where each element represents a line of the input
    """
    # Define the file path relative to the root directory of the year folder
    file_name = get_puzzle_file_path(year, day)

    try:
        with open(file_name) as file:
            return file.read().splitlines()
    except Exception as e:
        logger.error(f"Error reading input file for year {year}, day {day}: {e}")
        raise


def load_puzzle_input_as_string(year: int, day: int) -> str:
    """
    Load the entire puzzle input as a single string.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: The entire puzzle input as a string
    """
    # Define the file path relative to the root directory of the year folder
    file_name = get_puzzle_file_path(year, day)

    try:
        with open(file_name) as file:
            return file.read().strip()
    except Exception as e:
        logger.error(f"Error reading input file for year {year}, day {day}: {e}")
        raise


def load_puzzle_input_as_int_list(year: int, day: int) -> List[int]:
    """
    Load the puzzle input as a list of integers, assuming each line contains one integer.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :return: List of integers, where each element represents a line of the input parsed as an int
    """
    # Define the file path relative to the root directory of the year folder
    file_name = get_puzzle_file_path(year, day)

    try:
        with open(file_name) as file:
            return [int(line.strip()) for line in file.readlines()]
    except ValueError as e:
        logger.error(
            f"Error parsing input file as integers for year {year}, day {day}: {e}"
        )
        raise
    except Exception as e:
        logger.error(f"Error reading input file for year {year}, day {day}: {e}")
        raise
