"""
Day 3

"""

# Add jono_aoc_helpers (local pip module)
import sys
import os

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
    get_puzzle_input(2015, 3)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_string(2015, 3)

    # Calculate results and log it
    part_1_result = part_1(puzzle_input)
    logger.info(f"Part 1: {part_1_result}")
    part_2_result = part_2(puzzle_input)
    logger.info(f"Part 2: {part_2_result}")


@timed()
def part_1(puzzle_input: str) -> int:
    """
    Calculate the number of houses that receive at least one present.

    :param puzzle_input: String containing directions
    :return: Number of houses that receive at least one present
    """
    visited_houses = set()
    x, y = 0, 0
    visited_houses.add((x, y))

    for direction in puzzle_input:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        visited_houses.add((x, y))
    return len(visited_houses)


@timed()
def part_2():
    pass


if __name__ == "__main__":
    main()
