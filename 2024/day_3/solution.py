"""
Day 3

"""

import sys
import os
import re

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input

YEAR = 2024  # YYYY
DAY = 3  # D

# Set up helpers
args = get_arguments()
logger = initiate_logging(args.level)


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Request input from AoC via curl
    get_puzzle_input(YEAR, DAY)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_string(YEAR, DAY)

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
def part_1(puzzle_input: str) -> int:
    """
    Extract valid mul(X,Y) instructions and calculate the sum of their results.
    X and Y can be 1 to 3 digits.

    :param puzzle_input: The corrupted memory as a string.
    :return: Sum of the results of all valid mul instructions.
    """
    # Use regex to match mul(X,Y)
    pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")

    matches = re.findall(pattern, puzzle_input)
    logger.debug(f"Found matches: {matches}")

    total_sum = 0
    for x, y in matches:
        result = int(x) * int(y)
        logger.debug(f"Multiplying {x} * {y} = {result}")
        total_sum += result

    return total_sum


@timed()
def part_2(puzzle_input: str) -> int:
    """
    Handle do() and don't() instructions to enable/disable mul instructions.
    Calculate the sum.

    :param puzzle_input: The corrupted memory as a string.
    :return: Sum of the results of all enabled mul instructions.
    """
    # Regex patterns to match instructions
    instruction_pattern = re.compile(
        r"(do\(\)|don't\(\)|mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\))"
    )

    mul_enabled: bool = True
    total_sum: int = 0

    # Process all instructions in order of appearance
    for match in re.finditer(instruction_pattern, puzzle_input):
        instruction = match.group(1)

        if instruction == "do()":
            logger.debug("Found do(): Enabling mul instructions.")
            mul_enabled = True
        elif instruction == "don't()":
            logger.debug("Found don't(): Disabling mul instructions.")
            mul_enabled = False
        elif instruction.startswith("mul("):
            if mul_enabled:
                x, y = int(match.group(2)), int(match.group(3))
                result = x * y
                logger.debug(f"Multiplying {x} * {y} = {result}")
                total_sum += result

    return total_sum


if __name__ == "__main__":
    main()
