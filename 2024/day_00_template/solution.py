"""
Day 00

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

YEAR = 2024  # YYYY
DAY = 0  # D

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
    # puzzle_input = load_input.<choose function>(YEAR, DAY)

    # Calculate results and log it
    try:
        part_1_result = part_1(puzzle_input)
        logger.info(f"Part 1: {part_1_result}")
    except Exception as e:
        logger.error(f"Error during Part 1: {e}")

    # try:
    #     part_2_result = part_2(puzzle_input)
    #     logger.info(f"Part 2: {part_2_result}")
    # except Exception as e:
    #     logger.error(f"Error during Part 2: {e}")


@timed()
def part_1():
    pass


@timed()
def part_2():
    pass


if __name__ == "__main__":
    main()
