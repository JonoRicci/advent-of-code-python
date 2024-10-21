"""
Day 04

"""

import sys
import os
import hashlib

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
    get_puzzle_input(2015, 4)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_string(2015, 4).strip()

    # Calculate results and log it
    part_1_result = part_1(puzzle_input)
    logger.info(f"Part 1: {part_1_result}")
    part_2_result = part_2(puzzle_input)
    logger.info(f"Part 2: {part_2_result}")


@timed()
def part_1(puzzle_input: str) -> int:
    """
    Find the lowest positive number that, when appended to the secret key, produces an MD5 hash starting with five zeroes.

    :param puzzle_input: The secret key (input string)
    :return: The lowest positive number that produces the required hash
    """
    number = 0
    while True:
        test_string = f"{puzzle_input}{number}"
        hash_result = hashlib.md5(test_string.encode()).hexdigest()
        if hash_result.startswith("00000"):
            return number
        number += 1


@timed()
def part_2(puzzle_input: str) -> int:
    """
    Find the lowest positive number that, when appended to the secret key, produces an MD5 hash starting with six zeroes.

    :param puzzle_input: The secret key (input string)
    :return: The lowest positive number that produces the required hash
    """
    number = 0
    while True:
        test_string = f"{puzzle_input}{number}"
        hash_result = hashlib.md5(test_string.encode()).hexdigest()
        if hash_result.startswith("000000"):
            return number
        number += 1


if __name__ == "__main__":
    main()
