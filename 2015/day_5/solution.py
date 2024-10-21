"""
Day 05

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
    get_puzzle_input(2015, 5)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 5)

    # Calculate results and log it
    part_1_result = part_1(puzzle_input)
    logger.info(f"Part 1: {part_1_result}")
    part_2_result = part_2(puzzle_input)
    logger.info(f"Part 2: {part_2_result}")


@timed()
def part_1(puzzle_input: list) -> int:
    """
    Calculate the number of nice strings in the input.

    :param puzzle_input: List of strings to evaluate
    :return: Number of nice strings
    """
    nice_count = 0
    for string in puzzle_input:
        if is_nice_string(string):
            nice_count += 1
    return nice_count


def is_nice_string(string: str) -> bool:
    """
    Determine if a string is nice based on given rules.

    :param string: The string to evaluate
    :return: True if the string is nice, False otherwise
    """
    vowels = set("aeiou")
    disallowed = ["ab", "cd", "pq", "xy"]

    # Rule 1: At least three vowels
    vowel_count = sum(1 for char in string if char in vowels)
    if vowel_count < 3:
        return False

    # Rule 2: At least one letter that appears twice in a row
    has_double = any(string[i] == string[i + 1] for i in range(len(string) - 1))
    if not has_double:
        return False

    # Rule 3: Does not contain disallowed substrings
    if any(bad in string for bad in disallowed):
        return False

    return True


@timed()
def part_2(puzzle_input: list) -> int:
    """
    Calculate the number of strings in the input based on the new rules.

    :param puzzle_input: List of strings to evaluate
    :return: Number of nice strings
    """
    nice_count = 0
    for string in puzzle_input:
        if is_nice_string_part_2(string):
            nice_count += 1
    return nice_count


def is_nice_string_part_2(string: str) -> bool:
    """
    Determine if a string is nice based on the new set of rules.

    :param string: The string to evaluate
    :return: True if the string is nice, False otherwise
    """
    # Rule 1: Contains a pair of any two letters that appears at least twice without overlapping
    has_repeated_pair = any(
        string[i : i + 2] in string[i + 2 :] for i in range(len(string) - 1)
    )
    if not has_repeated_pair:
        return False

    # Rule 2: Contains at least one letter which repeats with exactly one letter between them
    has_repeating_letter = any(
        string[i] == string[i + 2] for i in range(len(string) - 2)
    )
    if not has_repeating_letter:
        return False

    return True


if __name__ == "__main__":
    main()
