"""
Day 08

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

# Set up helpers
args = get_arguments()
logger = initiate_logging(args.level)


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Request input from AoC via curl
    get_puzzle_input(2015, 8)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 8)

    # Calculate results and log it
    try:
        part_1_result = part_1(puzzle_input)
        logger.info(f"Part 1: {part_1_result}")
    except Exception as e:
        logger.error(f"Error during Part 1: {e}")

    try:
        part_2_result = part_2(puzzle_input)
        logger.info(f"Part 2: {part_2_result}")
    except Exception as e:
        logger.error(f"Error during Part 2: {e}")


@timed()
def part_1(puzzle_input: list[str]) -> int:
    """
    Calculate the difference between the number of characters in the code
    representation of the string literals and the number of characters in memory
    for the values of the strings.

    :param puzzle_input: List of string literals from the input
    :return: The calculated difference
    """
    code_characters = 0
    memory_characters = 0

    for line in puzzle_input:
        # Calculate the number of characters in code (including quotes and escape sequences)
        code_characters += len(line)

        # Decode the string to find the actual number of characters in memory
        memory_characters += len(eval(line))

    return code_characters - memory_characters


@timed()
def part_2(puzzle_input: list[str]) -> int:
    """
    Calculate the difference between the number of characters in the newly encoded representation
    of the string literals and the number of characters in the original code representation.

    :param puzzle_input: List of string literals from the input
    :return: The calculated difference
    """
    code_characters = 0
    encoded_characters = 0

    for line in puzzle_input:
        # Calculate the number of characters in code (including quotes and escape sequences)
        code_characters += len(line)

        # Encode the string and calculate the number of characters in the encoded version
        encoded_line = line.replace("\\", "\\\\").replace('"', '\\"')
        encoded_line = f'"{encoded_line}"'
        encoded_characters += len(encoded_line)

    return encoded_characters - code_characters


if __name__ == "__main__":
    main()
