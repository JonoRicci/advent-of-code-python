"""
Day 1

"""

import sys
import os

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Set up helpers
    args = get_arguments()
    logger = initiate_logging(args.level)

    # Request input from AoC via curl
    get_puzzle_input(2015, 1)

    # Load the puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_string(2015, 1)

    # Calculate results and log it
    part_1_result = part_1(puzzle_input)
    logger.info(f"Part 1: Santa ends up on floor: {part_1_result}")
    part_2_result = part_2(puzzle_input)
    logger.info(f"Part 2: Santa enters the basement at position: {part_2_result}")


@timed()
def part_1(puzzle_input: str) -> int:
    """
    Calculate the resulting floor based on the given puzzle_input.

    :param puzzle_input: String containing the sequence of parentheses
    :return: The floor number that Santa ends up on
    """
    floor = 0
    for char in puzzle_input:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor


@timed()
def part_2(puzzle_input: str) -> int:
    """
    Find the position of the first character that causes Santa to enter the basement floor (floor -1).

    :param puzzle_input: String containing the sequence of parentheses
    :return: The position of the character that causes Santa to first enter the basement
    """
    floor = 0
    for index, char in enumerate(puzzle_input, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            return index
    return -1  # Return -1 if Santa never enters the basement


if __name__ == "__main__":
    main()
